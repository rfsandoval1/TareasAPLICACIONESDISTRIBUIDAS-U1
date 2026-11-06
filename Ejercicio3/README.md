# Ejercicio3 de Ejecución con Hilos y Lock - Reserva de Cine

Este proyecto demuestra el uso de **hilos (`threading`)** y el mecanismo de exclusión mutua (**`Lock`**) en Python utilizando un ejemplo **múltiples usuarios intentando reservar asientos en una misma sala de cine al mismo tiempo**, evitando que un mismo asiento sea asignado a dos personas distintas debido a una condición de carrera.

## Requisitos previos

- [Docker](https://www.docker.com/) instalado en tu equipo.
- [Docker Compose](https://docs.docker.com/compose/) instalado.

## ¿Cómo ejecutar el script con Docker?

Sigue estos pasos en tu terminal:

1. Clona este repositorio o descarga los archivos en una carpeta.
2. Abre tu terminal en la raíz del proyecto.
3. Ejecuta el siguiente comando para construir y correr el contenedor:

```bash
docker compose up --build
```
