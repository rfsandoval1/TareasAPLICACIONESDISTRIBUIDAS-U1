import asyncio
import time

async def preparar_tarea(tarea, segundos):
    print(f"Iniciando: {tarea}...")
    # Simula una tarea concurrente de forma asíncrona sin bloquear el programa completo
    await asyncio.sleep(segundos)
    print(f"✅ Completado: {tarea}")

async def main():
    print("=== SIMULACIÓN DE PREPARACIÓN DE UN DESAYUNO  CONCURRENTE ===")
    
    
    inicio = time.perf_counter()

    # Ejecución concurrente: todas las tareas corren "a la vez"
    await asyncio.gather(
        preparar_tarea("Tostar pan", 2),
        preparar_tarea("Licuar jugo de fruta", 3),
        preparar_tarea("Hervir huevos", 4)
    )

    fin = time.perf_counter()
    print("\n=== ¡DESAYUNO LISTO QUE RICO Y CREO CHEVERE! ===")
    print(f"Tiempo total de ejecución concurrente: {fin - inicio:.2f} segundos")
    
if __name__ == "__main__":
    asyncio.run(main())