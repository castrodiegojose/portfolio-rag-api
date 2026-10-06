# Portfolio RAG API

API en FastAPI para el chat del portfolio de Diego Castro. Recupera fragmentos del CV en Markdown (Chroma + embeddings locales) y genera la respuesta con Ollama en la máquina. No usa OpenAI ni otras APIs de pago.

Flujo:

1. Los `.md` de `md-resume/corpus` se parten por headings (`#` / `##`).
2. Cada chunk se embeddea con SentenceTransformer (`all-MiniLM-L6-v2`, 384 dimensiones).
3. Los vectores se guardan en Chroma persistente (`data/chroma`).
4. `POST /chat` embeddea el mensaje, trae los `k` vecinos más cercanos (distancia L2: **menor = más parecido**) y le pide a Ollama un resumen en `es` o `en`.

## Stack

| Pieza | Uso |
|---|---|
| FastAPI + Uvicorn | HTTP, CORS, routers |
| Pydantic / pydantic-settings | Request/response y `.env` |
| langchain-text-splitters | `MarkdownHeaderTextSplitter` |
| sentence-transformers | Embeddings locales |
| Chroma | Índice vectorial persistente |
| Ollama (`llama3.2`) | Generación |
| python-slugify | IDs de chunk (`archivo.md#seccion`) |

## Requisitos

- Python 3.12+ (probado con 3.14)
- [Ollama](https://ollama.com) instalado y corriendo
- Modelo de chat bajado una vez:

```bash
ollama pull llama3.2
```

Comprobá que responde:

```bash
ollama run llama3.2 "hola"
```

El primer `POST /debug/ingest` o `/chat` puede tardar: descarga el modelo de embeddings de Hugging Face y carga pesos en RAM.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

Editá `.env` si hace falta (orígenes CORS, modelo de Ollama). Para desarrollar, poné `ENABLE_DEBUG_ROUTERS=true`.

## Variables de entorno

La app **no arranca** si falta el `.env` o una variable requerida. Copiá el example; no commitees `.env` (está en `.gitignore`).

| Variable | Qué es | Valor local |
|---|---|---|
| `ALLOWED_ORIGINS` | Orígenes CORS (JSON array). El front del portfolio tiene que coincidir. | `["http://localhost:3000","http://127.0.0.1:3000"]` |
| `DOCUMENTS_DIR` | Carpeta de Markdown. Path relativo a la raíz del repo, o absoluto. | `md-resume/corpus` |
| `EMBEDDING_MODEL` | Nombre Hugging Face para SentenceTransformer. | `all-MiniLM-L6-v2` |
| `CHROMA_PATH` | Directorio del índice. Gitignorado. | `data/chroma` |
| `CHROMA_COLLECTION` | Nombre de la colección. El ingest la borra y la recrea. | `portfolio` |
| `OLLAMA_HOST` | Base URL del daemon Ollama. | `http://127.0.0.1:11434` |
| `OLLAMA_MODEL` | Tag de `ollama pull`. | `llama3.2` |
| `ENABLE_DEBUG_ROUTERS` | Si `true`, monta `/debug/*`. En prod: `false`. | `true` en local |
| `RETRIEVE_K` | Vecinos que pide a Chroma. | `5` |
| `RETRIEVE_MAX_DISTANCE` | Tope L2: hits más lejos no van al LLM. | `1.05` |

`pydantic-settings` lee `.env` al importar `app.core.config`. CORS: `allow_credentials=False`, métodos `GET` / `POST` / `OPTIONS`, header `Content-Type`.

## Correr

Desde la raíz del repo, con el venv activo y Ollama levantado:

```bash
fastapi dev main.py
```

Equivalente:

```bash
uvicorn main:app --reload
```

Health check:

```bash
curl http://127.0.0.1:8000/health
```

Respuesta: `{"ok":true}`.

Playground local (HTML estático, same-origin): abrí [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Llama a `POST /chat`. No es el widget del portfolio en `:3000`. Ingestá antes si el índice está vacío.

## Corpus e ingest

Los documentos viven en `md-resume/corpus/` (experiencia, about, proyectos). Solo se indexan archivos regulares que no empiezan con `.`. El splitter usa `##` como sección; si un chunk no tiene `##`, cae a `#` o a `"body"`.

El texto que se embeddea va prefijado con archivo y sección (`experience-opendev.md Storage. …`) para que retrieve por nombre de empresa o heading funcione mejor.

Con debug encendido, construí el índice **antes** del primer chat:

```bash
curl -X POST http://127.0.0.1:8000/debug/ingest
```

Respuesta típica: `{"chunks": <n>, "collection": "portfolio"}`. Cada ingest **borra** la colección y la vuelve a cargar. Si cambiaste un `.md`, ingest de nuevo.

Sin índice, `/chat` y `/debug/retrieve` fallan (colección inexistente).

`data/` no se versiona. En un clone limpio hay que ingest otra vez.

## API pública

### `GET /health`

Sin auth. Para load balancer o un ping del front.

### `POST /chat`

Body JSON (`ChatRequest`):

| Campo | Tipo | Notas |
|---|---|---|
| `sessionId` | string | Lo ecoea la respuesta. Hoy no hay historial de sesión. |
| `locale` | `"es"` \| `"en"` | Idioma de la respuesta de Ollama. |
| `message` | string | Pregunta o keywords (`OpenDev`, `Stripe`, `quién sos`). |

Ejemplo:

```bash
curl -s http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"sessionId":"demo","locale":"es","message":"OpenDev"}'
```

`ChatResponse`:

```json
{
  "reply": "…",
  "citations": [
    {
      "id": "experience-opendev.md#storage",
      "source": "experience-opendev.md",
      "section": "Storage"
    }
  ],
  "sessionId": "demo"
}
```

Errores:

| Status | Cuándo |
|---|---|
| 422 | Body inválido (Pydantic). |
| 404 | No hay índice (si el service tira `FileNotFoundError`). |
| 503 | Ollama no está accesible (`ConnectionError`). |
| 500 | Cualquier otro fallo de chat (detalle genérico, sin traceback). |

Ollama usa `temperature=0`. El prompt trata `message` como keywords, no exige match literal, y no inventa empleadores.

## Rutas debug

Solo existen si `ENABLE_DEBUG_ROUTERS=true`. En prod (`false`) son **404**: el router ni se monta.

Usalas con Bruno o `curl`. Sirven para ingest y para inspeccionar retrieve **sin** pasar por Ollama.

### `GET /debug/corpus`

Lista archivos en `DOCUMENTS_DIR`.

```json
{
  "directory": "corpus",
  "files": [{ "name": "about.md", "suffix": ".md", "size": 1234 }]
}
```

`404` si la carpeta no existe.

### `GET /debug/chunks`

Chunking en caliente (no lee Chroma). Query opcional `source`: **solo el nombre del archivo** (`experience-opendev.md`). Se rechaza path traversal, `..`, `/`, `\`, hidden files y cualquier cosa que no termine en `.md`.

| Llamada | Status |
|---|---|
| sin `source` | 200, todos los chunks |
| `?source=experience-opendev.md` | 200 |
| `?source=foo.txt` o `../.env` | **400** |
| `?source=no-existe.md` | **404** |

### `POST /debug/ingest`

Reconstruye Chroma. No lleva body.

### `GET /debug/retrieve`

Retrieve solo (hits + citations, sin LLM).

```
GET /debug/retrieve?question=OpenDev&k=5
```

`k` default 5. Distancia L2: el primer hit es el de menor `distance`.

## Layout

```
main.py                 # app, CORS, GET /, /health, routers
static/chat.html        # playground local (POST /chat)
app/core/config.py      # Settings desde .env
app/routers/chat.py     # POST /chat
app/routers/corpus.py   # /debug/* (flag)
app/schemas/            # ChatRequest/Response, corpus, chunks
app/services/
  list_documents.py
  chunking.py           # split + pipeline ingest
  embeddings.py
  store.py              # Chroma save/query
  questions.py          # retrieve → hits + citations
  generate.py           # prompt + Ollama
md-resume/corpus/       # fuente Markdown
data/                   # Chroma (gitignored)
```

Routers traducen excepciones a HTTP. Services no importan `HTTPException`.

## Notas

- **MiniLM es sesgado a inglés.** Queries en español tipo “almacenamiento” pueden rankear peor que el nombre del archivo o keywords en inglés (`OpenDev`, `storage`). Prefijo de chunk + queries concretas ayudan.
- **L2, no cosine “más alto gana”.** En retrieve, `0.8` es mejor que `1.1`.
- **Dos procesos uvicorn** (sin `--reload` mal usado, o dos terminales) duplican la carga del modelo y parecen “timeout” en el primer request.
- No hay fine-tuning. Mejorar respuestas = corpus, chunking, query y prompt; no entrenar `llama3.2`.
- El ingest debug es deliberado: en local indexás; en prod el flag apaga esas rutas. El índice tiene que existir en el volumen de `CHROMA_PATH`.
