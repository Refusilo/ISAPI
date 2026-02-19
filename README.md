# ISAPI
Herramientas en Python para interactuar con dispositivos Hikvision mediante la API ISAPI.

## Estructura del proyecto

```
ISAPI/
├── hikvision_cmd.py     # CLI principal (entry point para empaquetar a .exe)
├── src/                 # Código fuente importable (módulos y utilidades)
├── data/
│   ├── inputs/          # JSON de entrada para los distintos comandos
│   └── outputs/         # Registros y resultados generados automáticamente
├── assets/
│   ├── images/          # Recursos gráficos y fotos para enrolar rostros
│   ├── icons/           # Iconografía de la aplicación
│   ├── certs/           # Certificados descargados de los equipos
│   ├── forms/           # Formularios de referencia
│   └── vendor/          # Binarios o archivos externos
├── scripts/             # Wrappers `.bat` para ejecutar comandos frecuentes
├── docs/                # Ayuda y documentación adicional
└── examples/            # Pruebas y scripts experimentales
```

## Ejecución del CLI

1. Activa el entorno virtual si aplica (`.venv\Scripts\activate`).
2. Ejecuta el comando deseado, por ejemplo:

```powershell
python .\hikvision_cmd.py --order listuser --host http://<ip> --user <usuario> --passwd <clave> --json_file li_entrada.json
```

El parámetro `--json_file` busca primero en la ruta indicada y luego en `data/inputs`.  
Los archivos generados se guardan automáticamente dentro de `data/outputs`.
