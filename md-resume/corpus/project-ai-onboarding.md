# Onboarding de Integraciones de Partners Asistido por IA

## Context
Proyecto educativo de AI Engineering para un **Gym Management Assistant** (FitCore Gym). El objetivo fue construir, de forma progresiva, un agente de IA capaz de responder preguntas sobre políticas del gimnasio y consultar datos operativos de socios en tiempo real, desde un CLI hasta un servicio desplegable.

## Problem
Los asistentes basados solo en LLM alucinan políticas y no tienen acceso a datos vivos (estado del socio, pagos, vencimientos). Separar documentación y datos operativos en flujos manuales obliga al usuario a elegir el camino. Se necesitaba un agente que:
- Responda con grounding sobre el manual del gimnasio (RAG)
- Consulte datos en vivo vía tools tipadas (MCP + Supabase)
- Combine ambas fuentes cuando la pregunta lo requiera (Hybrid)
- Sea trazable y desplegable en producción

## Architecture

Flujo de 12 fases: LLM → LangChain → Embeddings → ChromaDB → RAG → Reranker → MCP → Supabase → LangGraph → Hybrid → LangSmith → Docker/K8s.

## My Responsibilities

- Diseñar e implementar el pipeline RAG (chunking, embeddings, ChromaDB, prompts con grounding)
- Construir el servidor MCP local con tools tipadas (Zod) y adapters mock/Supabase
- Orquestar el agente con LangGraph (router RAG/MCP/Hybrid + estado compartido)
- Instrumentar observabilidad con LangSmith y callbacks locales
- Empaquetar el servicio como API HTTP con health/readiness, Dockerfile multi-stage y manifiestos Kubernetes
- Documentar el proyecto (README, decisiones técnicas, guía de despliegue)

## Technologies

TypeScript (ESM) · LangChain · LangGraph · Hugging Face (LLM, embeddings, reranker) · ChromaDB · MCP · Zod · Supabase · LangSmith · Docker · Kubernetes · Node.js (`node:http`)

## Technical Challenges

- **Router predecible sin LLM extra:** clasificación por reglas (keywords + DNI) para evitar latencia y coste en cada pregunta
- **Hybrid grounding:** sintetizar políticas documentales y datos en vivo sin mezclar fuentes ni inventar información
- **MCP dual mock/Supabase:** mismo contrato de tools con repository pattern para desarrollar sin DB y operar con datos reales
- **Producción mínima:** health vs readiness, bootstrap con wait/auto-index de Chroma, imagen Alpine multi-stage sin framework HTTP pesado

## Results

- Agente funcional con 3 rutas (`rag` / `mcp` / `hybrid`) y trazabilidad de ejecución
- 3 MCP tools (`getMemberByDni`, `getPendingPayments`, `getExpiringMemberships`)
- CLI completa + API HTTP (`/health`, `/ready`, `/api/ask`)
- Stack desplegable con Docker Compose y Kubernetes
- Documentación lista para portfolio y demos

## Qué no hice

- Frontend / UI web
- Autenticación y autorización de usuarios
- Tests automatizados (unit/e2e) y CI/CD
- Evaluaciones formales de calidad RAG (datasets, métricas offline)
- Multi-tenancy, rate limiting o cola de jobs
- Fine-tuning de modelos
