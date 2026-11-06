import threading
import time
import random


asientos_disponibles = [1, 2, 3]


lock = threading.Lock()

def intentar_reservar(nombre_persona, asiento_deseado):
    global asientos_disponibles
    print(f"[{nombre_persona}] Intenta reservar el asiento #{asiento_deseado}...")
    
    # Simulamos un pequeño retraso de red o procesamiento
    time.sleep(random.uniform(0.1, 0.3))

    # SECCIÓN CRÍTICA: Protegida por el Lock para que un hilo a la vez verifique y modifique los asientos
    with lock:
        print(f"[{nombre_persona}] -> Verificando disponibilidad...")
        if asiento_deseado in asientos_disponibles:
            time.sleep(0.1) 
            asientos_disponibles.remove(asiento_deseado)
            print(f"[{nombre_persona}]  Reserva exitosa que chevere  #{asiento_deseado}! Asientos libres: {asientos_disponibles}\n")
        else:
            print(f"[{nombre_persona}] Lo siento, el asiento #{asiento_deseado} ya fue ocupado ya nadota. Asientos libres: {asientos_disponibles}\n")

if __name__ == "__main__":
    print("=== (RESERVA DE CINE) ===")
    print(f"Asientos libres iniciales de la sala: {asientos_disponibles}\n")

    hilos = []
    
    intentos = [
        ("Ana", 2),
        ("Carlos", 2), 
        ("Lucía", 1),
        ("Mateo", 3)
    ]

   
    for nombre, asiento in intentos:
        hilo = threading.Thread(target=intentar_reservar, args=(nombre, asiento))
        hilos.append(hilo)
        hilo.start()

    
    for hilo in hilos:
        hilo.join()

    print("=== PROCESAMIENTO FINALIZADO ===")
    print(f"Asientos libres finales de la sala: {asientos_disponibles}")