# Clase 01 — Proyecto Base (Python)

Este repositorio es un punto de partida para enseñar **estructura de proyecto**, **gestión de dependencias**, 
**bitácora de incidencias** y **pruebas básicas** en Python usando **VS Code**.

## Estructura
```txt
Clase-01-Proyecto-Base-Python/
├─ .vscode/              # Configuración de VS Code para el proyecto
├─ bitacora/             # Registros de incidencias de la clase
├─ data/                 # Archivos de datos de ejemplo
├─ docs/                 # Material de apoyo y guiones
├─ src/                  # Código fuente de la aplicación
│  └─ main.py
├─ tests/                # Pruebas (pytest)
│  └─ test_main.py
├─ requirements.txt      # Dependencias
└─ README.md
```

## Pasos rápidos
1. Crear y activar entorno virtual
   - Windows PowerShell:
     ```ps1
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     ```
   - macOS / Linux:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecutar el programa:
   ```bash
   python src/main.py
   ```
4. Ejecutar pruebas:
   ```bash
   pytest -q
   ```
