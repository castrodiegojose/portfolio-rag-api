# Flujos de Pago y Fulfillment con Stripe (Singular Innovation)

## Context

Trabajo como Software Developer en Singular Innovation (Febrero 2024 - Actualidad). Participación en múltiples proyectos para clientes de Estados Unidos, enfocados en sistemas backend, integraciones y despliegues en la nube.

## Problem

- Clientes necesitaban flujos de pago end-to-end con checkout, validación de cupones y fulfillment.
- El procesamiento de pagos bloqueaba el flujo principal de la aplicación.
- Integración con proveedores externos de logística y envíos.
- Múltiples proyectos requerían pipelines de CI/CD y despliegues multi-cloud.



## Architecture

- **APIs REST** construidas con NestJS, FastAPI y PostgreSQL.
- **Flujos de pago con Stripe:** sesiones de checkout, validación de cupones, procesamiento de eventos vía webhooks.
- **Desacoplamiento con Supabase Edge Functions:** manejo de eventos asíncrono y no bloqueante para el procesamiento de pagos.
- **Integraciones con proveedores externos de logística** para gestión de órdenes y actualizaciones de seguimiento.
- **CI/CD multi-cloud:** GitHub Actions, Google Cloud Build, AWS CodePipeline.
- **Containerización con Docker** y despliegue en AWS y GCP.
- **Firebase y Supabase** para autenticación, almacenamiento y lógica serverless.



## My Responsibilities

- Diseñar e implementar APIs REST con NestJS, FastAPI y PostgreSQL.
- Construir e integrar 2 flujos de pago/fulfillment end-to-end (incluyendo Stripe).
- Desacoplar el procesamiento de pagos del flujo principal.
- Integrar sistemas backend con proveedores externos de logística.
- Configurar y optimizar pipelines de CI/CD.
- Containerizar aplicaciones y desplegar servicios en AWS y GCP.
- Trabajar con Firebase y Supabase.



## Technologies

- NestJS
- FastAPI
- PostgreSQL
- Stripe
- Supabase Edge Functions
- Firebase
- Docker
- GitHub Actions
- Google Cloud Build
- AWS CodePipeline
- AWS
- GCP



## Technical Challenges

- **Pagos bloqueantes:** el procesamiento de pagos frenaba el flujo principal. Se desacopló usando Supabase Edge Functions para manejar eventos de forma asíncrona y no bloqueante.
- **Integración con Stripe:** manejo de sesiones de checkout, validación de cupones y procesamiento de eventos vía webhooks.
- **Proveedores externos de logística:** integración de órdenes y actualizaciones de seguimiento con APIs de terceros.
- **CI/CD multi-cloud:** pipelines con GitHub Actions, Google Cloud Build y AWS CodePipeline para reducir pasos manuales de despliegue.
- **Multi-cloud:** despliegue consistente en AWS y GCP con Docker.



## Results

- 2 flujos de pago/fulfillment end-to-end entregados (incluyendo Stripe).
- Procesamiento de pagos desacoplado y no bloqueante.
- Reducción de pasos manuales de despliegue mediante CI/CD optimizado.
- Integraciones estables con proveedores externos de logística.
- Servicios desplegados y containerizados en AWS y GCP.



## Que no hice

- **Kafka ni RabbitMQ:** el desacoplamiento de pagos fue con Supabase Edge Functions y webhooks.
- **GraphQL ni MySQL:** las APIs fueron REST y la base de datos PostgreSQL.
- **Kubernetes:** el despliegue fue con Docker en AWS/GCP, sin orquestación.
- **Escala Walmart ni MongoDB:** este rol no tocó la plataforma de eCommerce de Walmart ni bases NoSQL.

