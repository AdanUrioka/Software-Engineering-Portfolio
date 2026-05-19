import random
# Aqui ocurre la magia: importamos la clase personaje desde el archivo personaje.py
from simulador_combate import personaje

def lanzar_bola_fuego(lanzador, objetivo):
    """
    Habilidad especial que calcula el daño basado en la Inteligencia.
    Cuesta Mana (Inteligencia *5).
    """
    # Calculamos el costo de mana y el daño usando la Inteligencia del Personaje
    costo_mana = lanzador.inteligencia * 2
    daño_magico = lanzador.inteligencia * 4 + random.randint(1, 5)  # Daño base más un toque de aleatoriedad

    print(f" 🔥{lanzador.nombre} lanza BOLA DE FUEGO a {objetivo.nombre}! (Costo: {costo_mana} MP)")

    # Aplicamos el daño directamente al objetivo usando su metodo recibir_daño
    objetivo.recibir_daño(daño_magico)

if __name__ == "__main__":
    print("--- 🔮 PROBANDO SISTEMA DE HABILIDADES CONECTADAS 🔮 ---")

    # Instanciamos los personajes usando la clase que importamos
    mago = personaje("Adan El Mago", fuerza=5, agilidad=8, inteligencia=20)
    orco = personaje("Gorok El Orco", fuerza=15, agilidad=10, inteligencia=5)

    print(f"{mago.nombre} - HP: {mago.vida} | MP Potencial: {mago.inteligencia * 5}")
    print(f"{orco.nombre} - HP: {orco.vida}\n")

    # Turno1: Ataque normal (viene de simuladoir_combate.py)
    mago.atacar(orco)
    print(f"📊 HP del Orco: {orco.vida}\n")

    # Turno 2: ¡Usamos la nueva habilidad de este archivo!
    lanzar_bola_fuego(mago, orco)
    print(f"📊 HP final del Orco: {orco.vida}")