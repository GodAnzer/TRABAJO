# Guion docente — "Abran VS Code, vamos a montar un proyecto"

> Objetivo didáctico: que cada estudiante cree un proyecto Python con entorno virtual, dependencias, 
> pruebas y registro de incidencias, entendiendo **para qué sirve cada carpeta**.

## 0) Preparación (2 min)
- "Muchachos, abran **VS Code**. Presionen **Ctrl+Shift+P** y escriban *Terminal: Create New Terminal*."

## 1) Estructura de carpetas (4 min)
- "Aquí tienen una estructura modelo. *src* guarda el **código**, *tests* las **pruebas**, *data* los **archivos de datos**,
  *bitacora* nuestra **bitácora de incidencias** y *docs* los **apuntes de la clase**."
- "La carpeta *.vscode* guarda configuraciones locales del editor para que todo el grupo tenga la misma experiencia."

## 2) Entorno virtual (5 min)
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
- "Si ven `(venv)` al inicio de la línea, está **activado**."

## 3) Dependencias (3 min)
- "Instalen dependencias del archivo `requirements.txt`:"
  ```bash
  pip install -r requirements.txt
  ```
- "Si aparece un error de *pip* o red, lo registramos en `bitacora/plantilla_bitacora.csv`."

## 4) Primer run (3 min)
- "Ejecuten el programa:"
  ```bash
  python src/main.py
  ```
- "Prueben con su nombre y verifiquen la salida."

## 5) Pruebas automáticas (3 min)
- "Corran las pruebas:"
  ```bash
  pytest -q
  ```
- "Si falla, revisamos juntos el archivo `tests/test_main.py`."

## 6) Bitácora de incidencias (4 min)
- "Cada equipo anota un problema real de la sesión, su causa y la solución aplicada."
- "Esto es **oro** para las siguientes clases."

## 7) (Opcional) Git inicial (4 min)
```bash
git init
git add .
git commit -m "Clase 01: estructura base, deps y pruebas"
```
- "El que tenga GitHub sube el repo y me comparte el enlace."

---
## Preguntas guía para cerrar
- ¿Qué gana el equipo al separar *src* de *tests*?
- ¿Qué se debe guardar y qué se debe **excluir** (por ejemplo: `.venv`, `__pycache__`)?
- ¿Cómo nos ayuda la **bitácora** a evitar repetir errores?
