# Integraciones de IA y Automatización Backend (Singular Innovation)


## Context

Trabajo como Software Developer en Singular Innovation (Febrero 2024 - Actualidad), participando en proyectos para clientes de Estados Unidos. Dentro de estos proyectos desarrollé integraciones backend con APIs de modelos LLM, principalmente utilizando OpenAI, y funcionalidades basadas en prompts para automatizar procesos y mejorar la experiencia de los usuarios.

## Problem

- Algunos productos necesitaban incorporar capacidades de procesamiento mediante modelos de lenguaje.
- Las funcionalidades de IA debían integrarse dentro de sistemas backend existentes.
- Era necesario controlar desde el backend cómo se enviaban los datos y prompts a los modelos.
- Las respuestas de los modelos debían incorporarse al flujo funcional del producto.
- Determinados procesos podían automatizarse mediante integraciones entre servicios backend y herramientas externas.

## Architecture

- **Backend APIs:** APIs desarrolladas con NestJS y FastAPI que gestionan la lógica de las aplicaciones.
- **OpenAI API:** integración desde el backend para incorporar capacidades basadas en modelos de lenguaje.
- **Prompt-based workflows:** lógica backend que construye y ejecuta flujos basados en prompts para funcionalidades específicas.
- **External services:** integración de los resultados de IA dentro de los procesos existentes de los productos.
- **Cloud Functions / Edge Functions:** funciones serverless utilizadas en los productos cuando determinadas operaciones requerían ejecución independiente.

## My Responsibilities

- Integrar APIs de modelos LLM utilizando OpenAI.
- Implementar funcionalidades backend basadas en prompts.
- Integrar las respuestas de los modelos dentro de los flujos de los productos.
- Desarrollar APIs y lógica backend necesaria para soportar las funcionalidades de IA.
- Implementar automatizaciones backend utilizando servicios externos.
- Trabajar con funciones serverless cuando la funcionalidad requería ejecución independiente.

## Technologies

- OpenAI API
- NestJS
- FastAPI
- TypeScript
- Python
- Firebase Cloud Functions
- Supabase Edge Functions
- n8n

## Technical Challenges

- **Integración de LLMs con productos existentes:** las capacidades de IA debían formar parte de flujos backend ya existentes. Se integró la API de OpenAI desde los servicios backend y se diseñaron funcionalidades basadas en prompts.
- **Automatización de procesos:** algunas funcionalidades requerían conectar diferentes servicios y ejecutar acciones automáticamente. Se utilizaron integraciones backend y herramientas de automatización para incorporar estos flujos al producto.

## Results

- Integraciones con OpenAI implementadas en aplicaciones reales de clientes.
- Funcionalidades basadas en prompts incorporadas a flujos backend.
- Procesos de producto automatizados mediante integraciones entre servicios.
- Capacidades de IA integradas dentro de aplicaciones backend existentes.

## Qué no hice

- No desarrollé en Singular un sistema RAG de producción como el proyecto educativo de AI Engineering.
- No corresponde atribuir a Singular la implementación del agente LangGraph del proyecto educativo.
- No trabajé con Kafka en estas integraciones.
- No trabajé con Kubernetes en estas integraciones.
- No corresponde mezclar estas funcionalidades con los sistemas de Walmart/BDG.
