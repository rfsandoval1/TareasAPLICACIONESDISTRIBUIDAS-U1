# Simulación de Ejecución Secuencial: Preparación de Café

Este proyecto demuestra un proceso de la vida diaria (**preparar una taza de café paso a paso**) utilizando Python bajo un modelo de **ejecución secuencial**, donde ninguna acción puede iniciar hasta que la anterior finalice por completo.

## Requisitos previos

- [Docker](https://www.docker.com/) instalado en tu equipo.
- [Docker Compose](https://docs.docker.com/compose/) instalado.
- Docker Desktop iniciado con el motor Linux disponible.

## ¿Cómo ejecutar el script con Docker Compose?

Sigue estos pasos en tu terminal:

1. Clona este repositorio o descarga los archivos en una carpeta.
2. Abre tu terminal en la raíz del proyecto.
3. Ejecuta el siguiente comando para construir y correr el contenedor:

```bash
docker compose up --build
```

En Windows, si aparece un error como `failed to connect to the Docker API` o
`dockerDesktopLinuxEngine ... no se puede encontrar`, inicia Docker Desktop,
espera a que indique que el motor está ejecutándose y vuelve a ejecutar el
comando. Puedes comprobar el estado con:

```powershell
docker info
```

Si Docker Desktop ya está abierto y el error continúa, reinicia Docker Desktop
y verifica que esté seleccionado el modo **Linux containers**.
