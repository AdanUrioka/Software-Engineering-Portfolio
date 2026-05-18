import random
import time

class personaje:
    def __init__(self, nombre, fuerza,  agilidad, inteligencia):
        self.nombre = nombre
        self.fuerza = fuerza
        self.agilidad = agilidad
        self.inteligencia = inteligencia

        # La vida maxima y actual dependera de la fuerza del personaje
        self.vida = fuerza * 10
        self.vida = self.vida

        # El mana maximo y actual dependera de la inteligencia del personaje
        self.mana = inteligencia * 5        

    def esta_vivo(self):
        # TODO: Devuelve True si la vida es mayor que 0, de lo contrario False
        return self.vida > 0
    
    def recibir_daño(self, cantidad):
        # TODO: Resta la cantidad a self.vida y asegura que no sea menor que 0
        # Asegurate de que si la vida baja de 0, se quede en 0 (puedes usae max(0, ...))
        self.vida = max(0, self.vida - cantidad)
        print(f"💥 {self.nombre} recibe {cantidad} de daño. Vida restante: {self.vida}")

    def atacar(self, enemigo):
        # Logica base de ataque: el daño base seria igual a la fuerza
        daño = self.fuerza
        print(f"⚔️ {self.nombre} atacar a {enemigo.nombre} e intenta inflingir {daño} de daño.")
        # TODO: Llama al metodo recibir_daño del 'enemigo' pasandole el 'daño'
        # enemigo.recibir_daño(daño)
        enemigo.recibir_daño(daño)

# ==========================================
# SECCIÓN DE PRUEBA (Fuera de la clase)
# ==========================================
if __name__ == "__main__":
    print("--- ⚔️ INICIANDO SIMULADOR DE COMBATE POR TURNOS ⚔️ ---")
    
    # 1. Instanciamos a los combatientes
    jugador1 = personaje(nombre="Adán El Guerrero", fuerza=15, agilidad=10, inteligencia=5)
    jugador2 = personaje(nombre="Orco Gruñón", fuerza=12, agilidad=12, inteligencia=4)
    
    print(f"{jugador1.nombre} (Vida: {jugador1.vida} | Agilidad: {jugador1.agilidad})")
    print(f"{jugador2.nombre} (Vida: {jugador2.vida} | Agilidad: {jugador2.agilidad})\n")
    print("¡QUE COMIENCE EL DUELO!\n" + "-"*40)
    
    turno = 1
    
    # 2. El bucle se ejecutará MIENTRAS ambos sigan vivos
    while jugador1.esta_vivo() and jugador2.esta_vivo():
        print(f"\n▶️ TURNO {turno}:")
        time.sleep(1) # Pausa de 1 segundo para darle drama a la consola
        
        # 3. Determinar quién ataca primero según su Agilidad
        if jugador1.agilidad >= jugador2.agilidad:
            # Ataca jugador 1 primero
            jugador1.atacar(jugador2)
            # Si el jugador 2 sobrevive, contraataca en el mismo turno
            if jugador2.esta_vivo():
                jugador2.atacar(jugador1)
        else:
            # Ataca jugador 2 primero
            jugador2.atacar(jugador1)
            # Si el jugador 1 sobrevive, contraataca
            if jugador1.esta_vivo():
                jugador1.atacar(jugador2)
                
        # Mostrar estado al final del turno
        print(f"📊 ESTADO: {jugador1.nombre}: {jugador1.vida} HP | {jugador2.nombre}: {jugador2.vida} HP")
        turno += 1
        
    # 4. Fin del combate: Determinar el ganador
    print("\n" + "="*40)
    if jugador1.esta_vivo():
        print(f"🏆 ¡EL GANADOR ES {jugador1.nombre.upper()}!")
    else:
        print(f"💀 {jugador1.nombre} ha caído en combate. ¡EL GANADOR ES {jugador2.nombre.upper()}!")
    print("="*40)