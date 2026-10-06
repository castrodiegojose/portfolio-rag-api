# Plataforma eCommerce Walmart (BDG)

## Context

Trabajo como Software Developer en BDG (Febrero 2025 - Junio 2026, en paralelo con Singular Agency). Desarrollo backend para la plataforma de eCommerce de Walmart, un sistema de retail de gran escala que procesa millones de pedidos mensuales.

## Problem

- Plataforma de retail de gran escala con millones de transacciones mensuales.
- Necesidad de servicios backend escalables y de alta disponibilidad.
- Latencia y rendimiento a optimizar en un sistema con patrones de consulta ineficientes.
- Procesamiento orientado a eventos que requería mayor throughput.

## Architecture

- **Microservicios backend** construidos con NestJS.
- **APIs REST y GraphQL** como parte de los servicios de la plataforma.
- **Arquitectura orientada a eventos** con Kafka para procesamiento asíncrono.
- **Orquestación con Kubernetes** para despliegue y escalado.
- **Base de datos MySQL** con índices y optimización de queries.

## My Responsibilities

- Diseñar y desarrollar servicios backend escalables.
- Construir y consumir endpoints GraphQL y REST.
- Optimizar rendimiento y latencia del sistema.
- Escalar pipelines orientados a eventos (tópicos de Kafka, consumers).
- Colaborar en equipo multidisciplinario de 8 personas (backend, DevOps, producto).
- Contribuir a sistemas de alta disponibilidad con tráfico crítico.

## Technologies

- NestJS
- TypeScript
- Node.js
- MySQL
- Kafka
- Kubernetes
- GraphQL
- REST

## Technical Challenges

- **Patrones N+1:** consultas ineficientes que degradaban el rendimiento. Se resolvió optimizando queries SQL y agregando índices en base de datos.
- **Latencia en sistemas de alto tráfico:** optimización de queries y estructura de datos para sostener millones de transacciones mensuales.
- **Throughput en pipelines de eventos:** incorporación de nuevos tópicos de Kafka y escalado horizontal de consumers para aumentar el throughput y reducir demoras de procesamiento.
- **Alta disponibilidad:** sostener operaciones críticas con grandes volúmenes de tráfico.

## Results

- Reducción de latencia mediante optimización de queries SQL, índices y eliminación de patrones N+1.
- Aumento de throughput en pipelines de eventos (nuevos tópicos Kafka + más consumers).
- Reducción de demoras de procesamiento.
- Servicios backend escalables que soportan millones de pedidos mensuales.


## Qué no hice
- No diseñé Kafka desde cero; trabajé sobre pipelines ya existentes.
- No fui tech lead del equipo de 8.
- No toqué el frontend de eCommerce.
