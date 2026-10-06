import ollama
from app.core.config import settings

client = ollama.Client(host=settings.ollama_host)

def build_prompt(question: str, hits: list[dict], locale: str ):
    blocks = []    
    for i, h in enumerate(hits, start=1):
        blocks.append(f"[{i}] ({h["source"]} / {h["section"]}) \n {h["text"]}")
    context = "\n\n".join(blocks)
    lang = "Spanish" if locale == "es" else "English"
    system = f"""
    You are Diego's portfolio assistant. Answer in {lang}.
    Answer using the context. The user message may be keywords, not a full question.
    If the context is about that topic, summarize it (role, company, what was built, stack).
    Do not require the message to appear verbatim.
    Say you don't know only if the context is about a different project or person.
    Do not invent jobs, dates, or employers.
    Never ask the user for more context or details.
    If the context mentions that company or those technologies (even in different chunks), summarize; do not say you lack information.
    """
    user=f"""
    Context:
    {context}

    Keywords: {question}
    Write a short answer about Diego's work.
    """
    return system, user

def generate_reply(question: str, hits: list[dict], locale: str ):
    system, user = build_prompt(question, hits, locale)
    response = client.chat(
        model= settings.ollama_model,
        messages= [{"role": "system", "content": system}, {"role": "user", "content": user }],
        options={"temperature": 0}
    )
    return response["message"]["content"]

    