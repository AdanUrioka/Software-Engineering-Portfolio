# Software Engineering Portfolio - Motor de Atributos

Este repositorio contiene un módulo interactivo desarrollado en Python para la creación y gestión inicial de atributos de personajes. Es ideal para comprender las bases conceptuales del desarrollo de videojuegos de rol (RPG) o sistemas basados en estadísticas.

## 🚀 Características del Proyecto

* **Entrada Dinámica de Datos:** Permite al usuario asignar valores personalizados a los atributos principales del personaje mediante la consola.
* **Validación de Rangos:** Control de flujos que asegura que los atributos principales (Fuerza, Agilidad e Inteligencia) se mantengan estrictamente en un rango de 1 a 100.
* **Manejo de Excepciones:** Implementación de bloques `try-except` (`ValueError`) para evitar que el programa falle si el usuario introduce caracteres no numéricos.
* **Cálculo de Estadísticas Derivadas:** Generación automática de estadísticas secundarias basadas en los atributos base:
  * **Vida:** Fuerza $\times$ 10
  * **Maná:** Inteligencia $\times$ 5
  * **Stamina:** Agilidad $\times$ 2
* **Salida Formateada:** Uso de *f-strings* en Python para entregar un resumen limpio y legible del personaje creado.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Conceptos Aplicados:** Validación de datos, manejo de excepciones, lógica condicional, f-strings.

## 📁 Estructura del Repositorio

```text
├── README.md               # Documentación del proyecto
└── motor_atributos.py      # Script principal con la lógica del motor