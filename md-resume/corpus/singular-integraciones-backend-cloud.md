# Integraciones Backend y Cloud para Productos de Clientes de EE. UU. (Singular Innovation)


## Context

Trabajo como Software Developer en Singular Innovation (Febrero 2024 - Actualidad), participando en múltiples proyectos para clientes de Estados Unidos. Además del trabajo específico de pagos y fulfillment, desarrollé APIs backend e integraciones para productos que utilizaban Firebase y Supabase para autenticación, almacenamiento y lógica serverless, participando en la implementación y despliegue de funcionalidades backend.

## Problem

- Los productos requerían APIs backend para exponer y procesar lógica de negocio.
- Algunas funcionalidades necesitaban integrarse con servicios administrados como Firebase y Supabase.
- Determinadas operaciones debían ejecutarse mediante funciones serverless en lugar de depender exclusivamente de un backend tradicional.
- Los proyectos requerían despliegues automatizados para reducir operaciones manuales.
- Los servicios debían poder ejecutarse de forma consistente en diferentes entornos cloud.

## Architecture

- **REST APIs:** servicios backend desarrollados con NestJS y FastAPI.
- **Firebase:** servicios utilizados para autenticación, almacenamiento y lógica backend mediante Cloud Functions.
- **Supabase:** plataforma utilizada para almacenamiento y lógica backend mediante Edge Functions.
- **Serverless Functions:** funcionalidades backend ejecutadas como Cloud Functions o Edge Functions según el producto.
- **Docker:** containerización de aplicaciones y servicios backend.
- **CI/CD:** GitHub Actions, Google Cloud Build y AWS CodePipeline utilizados para automatizar procesos de build y deployment.
- **Cloud infrastructure:** despliegues de servicios sobre AWS y GCP.

## My Responsibilities

- Diseñar e implementar APIs REST con NestJS y FastAPI.
- Implementar lógica backend integrada con Firebase y Supabase.
- Trabajar con Firebase Authentication, almacenamiento y Cloud Functions.
- Implementar funcionalidades backend utilizando Supabase Edge Functions.
- Containerizar aplicaciones y servicios con Docker.
- Configurar y mantener pipelines de CI/CD.
- Realizar despliegues de servicios sobre AWS y GCP.
- Integrar servicios backend con APIs y servicios externos requeridos por los productos.

## Technologies

- NestJS
- FastAPI
- Firebase
- Firebase Authentication
- Firebase Cloud Functions
- Supabase
- Supabase Edge Functions
- Docker
- GitHub Actions
- Google Cloud Build
- AWS CodePipeline
- AWS
- GCP

## Technical Challenges

- **Lógica distribuida entre backend y servicios administrados:** algunas funcionalidades no residían únicamente en un servidor backend tradicional. Se implementaron funciones serverless mediante Firebase Cloud Functions y Supabase Edge Functions según las necesidades de cada producto.
- **Despliegues repetibles:** los proyectos requerían evitar procesos manuales de deployment. Se configuraron pipelines de CI/CD utilizando GitHub Actions, Google Cloud Build y AWS CodePipeline.
- **Diferentes plataformas cloud:** los productos utilizaban servicios de AWS y GCP. Se trabajó con Docker y pipelines específicos para mantener un proceso de despliegue reproducible.

## Results

- APIs REST implementadas para distintos productos de clientes de Estados Unidos.
- Funcionalidades backend integradas con Firebase y Supabase.
- Lógica serverless implementada mediante Cloud Functions y Edge Functions.
- Aplicaciones containerizadas con Docker.
- Pipelines de CI/CD configurados para automatizar builds y despliegues.
- Servicios desplegados en AWS y GCP.

## Qué no hice

- No administré Kubernetes en estos proyectos.
- No trabajé con Kafka en estos proyectos.
- No trabajé con MySQL en estos proyectos.
- No trabajé con RabbitMQ en estos proyectos.
- No corresponde mezclar aquí el servicio de almacenamiento con S3 desarrollado en OpenDev Pro.
