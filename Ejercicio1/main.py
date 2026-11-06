import time

def ejecutar_paso(paso, segundos):
    print(f"👉 Iniciando: {paso}...")
    time.sleep(segundos) # Simula el tiempo que toma cada tarea
    print(f"✅ Completado: {paso}\n")

if __name__ == "__main__":
    print("=== PREPARACIÓN DE CAFÉ (EJECUCIÓN SECUENCIAL) ===")
    print("es un ejmplo par hacer cafe.\n")
    
    inicio = time.perf_counter()

    # Epasos para hacer cafe
    ejecutar_paso("Hervir agua", 2)
    ejecutar_paso("Moler los granos de café", 2)
    ejecutar_paso("Filtrar el café", 3)
    ejecutar_paso("Servir en la taza", 1)

    fin = time.perf_counter()
    print("=== ¡CAFÉ LISTO QUE RICO! ===")
    print(f"Tiempo total de ejecución secuencial: {fin - inicio:.2f} segundos")