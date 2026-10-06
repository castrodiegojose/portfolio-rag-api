# Microservicio de Almacenamiento en la Nube (OpenDev Pro)

## Context

Trabajo como Backend Developer en OpenDev Pro (Julio 2022 - Febrero 2024). Plataforma basada en microservicios para estudios contables.

## Problem

- Estudios contables necesitaban una estructura de carpetas compartida entre todos los usuarios de un mismo estudio.
- Se requería soporte de carpetas privadas por usuario dentro de esa estructura compartida.
- La estructura debía emular la organización de carpetas de Windows, a partir de metadata.
- Control de acceso por roles y permisos sobre el servicio de almacenamiento.

## Architecture

- **Arquitectura de microservicios** desplegada con Docker y AWS (S3).
- **Servicio de almacenamiento:** a partir de metadata en MongoDB, genera una estructura de carpetas similar a la de Windows.
- **Estructura compartida por estudio** con soporte de carpetas privadas por usuario.
- **Comunicación asíncrona entre servicios** con RabbitMQ.
- **Autenticación y autorización** con JWT y control de acceso basado en roles (RBAC).
- **Persistencia:** MongoDB y PostgreSQL.

## My Responsibilities

- Construir y mantener múltiples microservicios.
- Diseñar y desarrollar el servicio de almacenamiento (foco principal).
- Diseñar capas de control de acceso basadas en roles y permisos.
- Desarrollar servicios backend con Node.js (Express), MongoDB y PostgreSQL.
- Construir y mantener la arquitectura de microservicios (Docker, AWS S3).
- Implementar autenticación y autorización (JWT, RBAC).
- Usar RabbitMQ para comunicación asíncrona entre servicios.

## Technologies

- Node.js
- Express
- MongoDB
- PostgreSQL
- Docker
- AWS S3
- RabbitMQ
- JWT
- RBAC

## Technical Challenges

- **Estructura tipo Windows desde metadata:** generar una jerarquía de carpetas compartida y consistente a partir de metadata en MongoDB.
- **Compartición + privacidad:** un mismo árbol de carpetas compartido por todos los usuarios del estudio, con carpetas privadas por usuario.
- **Control de acceso granular:** roles y permisos aplicados al servicio de almacenamiento.
- **Comunicación asíncrona:** desacoplar servicios vía RabbitMQ para evitar acoplamiento directo.
- **Autenticación y autorización:** JWT + RBAC en un entorno multi-tenant (varios estudios).

## Results

- Servicio de almacenamiento con estructura de carpetas tipo Windows, compartida por estudio y con carpetas privadas por usuario.
- Capas de control de acceso basadas en roles y permisos.
- Arquitectura de microservicios containerizada y desplegada en AWS.
- Comunicación asíncrona entre servicios con RabbitMQ.
- Autenticación y autorización implementadas con JWT y RBAC.

## Que no hice

- **Kafka ni event-driven con Kafka:** la mensajería asíncrona fue solo con RabbitMQ.
- **NestJS, TypeScript ni GraphQL:** el stack backend fue Node.js con Express.
- **Pagos ni Stripe:** no trabajé con checkout, fulfillment ni procesamiento de pagos.
- **GCP, Kubernetes ni CI/CD multi-cloud:** el despliegue fue con Docker y AWS (S3).
