# Software Engineering Portfolio - RPG Core Modules

Este repositorio funciona como un portafolio profesional que demuestra la evolución y aplicación de conceptos avanzados de Ingeniería de Software en Python, escalando desde la programación estructurada básica hasta la arquitectura modular interconectada utilizando Programación Orientada a Objetos (POO).

## 🚀 Módulos del Proyecto y Evolución

El proyecto está diseñado de forma modular, permitiendo que múltiples scripts interactúen entre sí reutilizando código de manera eficiente:

1. **`motor_atributos.py` (Nivel 1 - Estructurado):** * Módulo interactivo de consola para la asignación y validación estricta de atributos base (rango 1-100) utilizando control de excepciones (`try-except`).
   * Calcula de forma estática estadísticas derivadas como Vida (Fuerza × 10), Maná (Inteligencia × 5) y Stamina (Agilidad × 2).

2. **`simulador_combate.py` (Nivel 2 - POO Clásico):**
   * Migración de la lógica hacia el paradigma de **Programación Orientada a Objetos**.
   * Implementación de la clase `Personaje` con encapsulamiento de estados (HP, Fuerza, Agilidad, Inteligencia).
   * Sistema de combate automático por turnos basado en el paso de mensajes entre objetos (`atacar` y `recibir_danio`), donde la prioridad de ataque se decide dinámicamente mediante la Agilidad de los combatientes.

3. **`habilidades.py` (Nivel 3 - Arquitectura Modular Interconectada):**
   * Demuestra la **reutilización de código e importación de dependencias** en Python al importar la clase `Personaje` desde `simulador_combate.py` sin duplicar lógica.
   * Inyecta un sistema de habilidades especiales (`lanzar_bola_fuego`) que calcula el impacto basándose en variables de estado dinámicas e introduce un factor de aleatoriedad matemática.

## 🛠️ Tecnologías y Conceptos de Ingeniería Aplicados

* **Lenguaje:** Python 3.x
* **Paradigma Principal:** Programación Orientada a Objetos (POO)
* **Conceptos de Arquitectura:** Modularidad, Reutilización de Código, Encapsulamiento, Manejo de Dependencias.
* **Buenas Prácticas:** Estilo de código limpio guiado por PEP 8, Control de Versiones con Git.

## 📁 Estructura del Repositorio

```text
├── README.md               # Documentación general del portafolio
├── motor_atributos.py      # Script de validación de entrada de datos
├── simulador_combate.py    # Clase base del Personaje y ciclo de turnos
└── habilidades.py          # Módulo de extensión de habilidades (Punto de entrada actual)