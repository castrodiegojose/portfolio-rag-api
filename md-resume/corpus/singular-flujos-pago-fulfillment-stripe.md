# Flujos de Pago y Fulfillment con Stripe (Singular Innovation)

## Context

Trabajo como Software Developer en Singular Innovation (Febrero 2024 - Actualidad), participando en proyectos para clientes de Estados Unidos. En este proyecto trabajé sobre un producto con flujo de compra y fulfillment, desarrollando el backend que conecta pagos con Stripe, procesamiento de órdenes e integraciones con proveedores externos de impresión, logística y envíos.

## Problem

- El procesamiento de pagos estaba acoplado al flujo principal de la aplicación, por lo que los picos de actividad podían impactar al resto del backend.
- El flujo de checkout requería manejar sesiones de Stripe, validación de cupones y eventos posteriores al pago.
- El sistema debía sincronizar el estado de las órdenes con proveedores externos de impresión y envío.
- Las actualizaciones de fulfillment y tracking llegaban mediante eventos externos y debían procesarse de forma confiable.
- Parte del procesamiento debía ejecutarse de manera asíncrona para evitar bloquear el flujo principal.

## Architecture

- **Backend APIs:** APIs REST implementadas con NestJS y FastAPI para exponer la lógica del producto.
- **Stripe:** integración para checkout, pagos, validación de cupones y procesamiento de eventos mediante webhooks.
- **Supabase Edge Functions:** procesamiento desacoplado de determinadas operaciones de pago, permitiendo manejar eventos de forma asíncrona y no bloqueante.
- **Fulfillment providers:** integración backend con proveedores externos de impresión, logística y envíos para procesar órdenes y recibir actualizaciones.
- **Webhooks:** recepción y procesamiento de eventos provenientes de servicios externos para mantener actualizado el flujo de órdenes.
- **PostgreSQL:** persistencia utilizada por los servicios backend involucrados en el producto.
- **Docker + Cloud:** servicios containerizados y desplegados en AWS y GCP.
- **CI/CD:** automatización de builds y despliegues mediante GitHub Actions, Google Cloud Build y AWS CodePipeline.

## My Responsibilities

- Diseñar e implementar APIs REST con NestJS, FastAPI y PostgreSQL.
- Construir e integrar flujos de pago y fulfillment end-to-end con Stripe.
- Implementar checkout, validación de cupones y procesamiento de eventos mediante webhooks.
- Desacoplar el procesamiento de pagos del flujo principal mediante Supabase Edge Functions.
- Integrar el backend con proveedores externos de impresión, logística y envíos.
- Implementar el procesamiento de órdenes y actualizaciones de tracking provenientes de servicios externos.
- Implementar procesamiento asíncrono basado en webhooks y tareas en background.
- Configurar y mantener pipelines de CI/CD.
- Containerizar servicios con Docker y participar en despliegues sobre AWS y GCP.

## Technologies

- NestJS
- FastAPI
- PostgreSQL
- Stripe
- Supabase Edge Functions
- Docker
- GitHub Actions
- Google Cloud Build
- AWS CodePipeline
- AWS
- GCP

## Technical Challenges

- **Pagos acoplados al flujo principal:** el procesamiento de pagos podía impactar al backend principal durante picos de actividad. Se desacopló parte del procesamiento mediante Supabase Edge Functions y manejo asíncrono de eventos.
- **Eventos de Stripe:** el flujo requería procesar correctamente checkout, cupones y eventos posteriores al pago. Se implementó integración basada en webhooks para reaccionar a los eventos de Stripe.
- **Fulfillment externo:** el estado de una orden dependía de proveedores externos de impresión y envío. Se integraron sus APIs y eventos para procesar órdenes y actualizaciones de tracking.
- **Procesamiento asíncrono:** determinados eventos externos no debían bloquear las operaciones principales. Se utilizaron webhooks y procesamiento en background para manejar esos eventos de forma independiente.
- **Despliegues en distintos entornos cloud:** los servicios debían mantenerse desplegables en AWS y GCP. Se utilizaron Docker y pipelines de CI/CD para automatizar el proceso.

## Results

- 2 flujos de pago/fulfillment end-to-end construidos e integrados, incluyendo Stripe.
- Procesamiento de pagos desacoplado del flujo principal mediante Supabase Edge Functions.
- Integración funcional con proveedores externos de impresión, logística y envíos.
- Procesamiento de órdenes y actualizaciones de tracking mediante integraciones y webhooks.
- Pipelines de CI/CD configurados con GitHub Actions, Google Cloud Build y AWS CodePipeline.
- Servicios containerizados y desplegados en AWS y GCP.

## Qué no hice

- No trabajé con Kafka en este proyecto.
- No trabajé con Kubernetes en este proyecto.
- No trabajé con MySQL en este proyecto.
- No trabajé con GraphQL en este proyecto.
- No corresponde mezclar aquí la arquitectura de microservicios, RabbitMQ o el servicio de almacenamiento con S3 desarrollado en OpenDev Pro.
