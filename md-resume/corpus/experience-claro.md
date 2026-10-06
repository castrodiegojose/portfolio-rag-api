# Claro

## Context

**Rol:** Ingeniero de Soporte IT y Virtualización  

**Fechas:** 01/2022 – 07/2022

**De qué se trataba:**  

Soporte y operación de una infraestructura virtualizada multi-vendor en un entorno de telecomunicaciones. La plataforma combinaba VMware, Red Hat OpenStack Platform (OSP), Nokia TelcoCloud y Cisco OSP, corriendo sobre servidores Dell y almacenamiento PureStorage. Además, desarrollé el backend de una página web interna para centralizar consultas, monitoreo y tareas de automatización, usando Python (Flask) y MongoDB.

## Problem

La infraestructura estaba fragmentada en múltiples orquestadores y hypervisores, lo que dificultaba la visibilidad centralizada, el troubleshooting y el aprovisionamiento de recursos. Los procesos eran en gran parte manuales, lo que generaba lentitud, errores humanos y altos tiempos de respuesta en soporte. No existía una herramienta interna que unificara la consulta de estado ni que automatizara validaciones o tareas repetitivas.

## Architecture

- **Virtualización:** VMware vSphere (clusters, hosts, VMs).

- **Nubes privadas / Telco Cloud:** Red Hat OSP, Nokia TelcoCloud, Cisco OSP.

- **Hardware:** Servidores Dell, almacenamiento PureStorage.

- **Backend:** Python + Flask, exponiendo una API REST.

- **Base de datos:** MongoDB (NoSQL) para métricas, configuraciones, logs y datos de la herramienta interna.

- **Integraciones:** APIs de VMware, OpenStack, Nokia y Cisco; scripts de automatización.

## My Responsibilities

- Soporte L2/L3 a la infraestructura virtualizada y cloud multi-vendor.

- Administración de VMware: clusters, hosts, VMs, templates y recursos.

- Operación y soporte de Red Hat OSP, Nokia TelcoCloud y Cisco OSP.

- Gestión de almacenamiento Dell y PureStorage.

- Diagnóstico y resolución de incidentes en entornos Telco/Cloud.

- Desarrollo backend de la página interna: API con Flask, modelado en MongoDB, endpoints para consultas y automatización.

- Documentación técnica y soporte a otros equipos.

## Technologies

`VMware` · `Red Hat OSP` · `Nokia TelcoCloud` · `Cisco OSP` · `Dell` · `PureStorage` · `Python` · `Flask` · `MongoDB` · `REST APIs` · `Linux` · `Git`

## Technical Challenges

- Integrar APIs heterogéneas de distintos fabricantes (VMware, OpenStack, Nokia, Cisco) con autenticaciones y versiones dispares.

- Optimizar consultas a MongoDB para métricas y configuraciones en tiempo real.

- Garantizar alta disponibilidad y rendimiento del backend en un entorno crítico.

- Troubleshooting en infraestructuras Telco/Cloud complejas y poco documentadas.

- Balancear las tareas de soporte operativo con el desarrollo de la herramienta interna.

## Results

- Centralización del monitoreo y la gestión de recursos multi-vendor.

- Disminución de incidentes por errores manuales.

- Mejora en la visibilidad y trazabilidad de la infraestructura.

- Herramienta interna adoptada por el equipo de operaciones.

## Qué no hice

- No diseñé la arquitectura de red desde cero.

- No administré equipos de red Cisco (routers/switches) fuera de Cisco OSP.

- No desarrollé el frontend de la página web interna.

- No gestioné presupuesto ni compras de hardware.

- No lideré equipo de trabajo.

- No implementé seguridad perimetral ni firewalls.

- No configuré backups empresariales (aunque pude haber participado en su operación).