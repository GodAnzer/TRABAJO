from datetime import datetime

def saludar(nombre: str) -> str:
    return "👋 Hola, {nombre}. Bienvenido(a) a la Clase 01."

def main():
    print("=== Proyecto Base Python ===")
    nombre = input("¿Cuál es tu nombre? ")
    print(saludar(nombre))
    print("Hora del sistema: {datetime.now()}")

if __name__ == "__main__":
    main()
