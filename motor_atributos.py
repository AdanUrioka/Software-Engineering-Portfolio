def crear_personaje():
    print("--- Generador de atributos de personaje ---")

    # 1. Entrada de datos
    nombre = input("Ingrese el nombre de su personaje: ")

    try:
        fuerza = int(input("Fuerza (1-100): "))
        agilidad = int(input("Agilidad (1-100): "))
        inteligencia = int(input("Inteligencia (1-100): "))

        # 2. Validación de rango
        if not (1 <= fuerza <= 100 and 1 <= agilidad <= 100 and 1 <= inteligencia <= 100):
            print("Error: Los atributos deben estar dentro del rango indicado.")
            return

        # 3. Cálculo de estadísticas derivadas
        vida = fuerza * 10
        mana = inteligencia * 5
        stamina = agilidad * 2

        # 4. Resumen formateado (usando f-strings)
        print(f"\n--- Resumen del personaje: {nombre} ---")
        print(f"Vida: {vida}")
        print(f"Mana: {mana}")
        print(f"Stamina: {stamina} SP")
        print("-----------------------------")

    except ValueError:
        print("Error: Por favor, ingrese solo números enteros.")

#4. Ejecutar la función para crear el personaje
if __name__ == "__main__":
    crear_personaje()