import sys
import os

# agrega la carpeta raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from calculadora import Calculadora
from menu import Menu

calc= Calculadora()
menu = Menu()

operaciones = {
    1: calc.sumar,
    2: calc.restar,
    3: calc.multiplicar,
    4: calc.dividir,
    5: calc.potencia,
    6: calc.raiz_cuadrada,
    7: calc.logaritmo,
    8: calc.seno,
    9: calc.coseno,
    10: calc.tangente,
    11: calc.factorial
}

while True:
    menu.mostrar_menu()
    opc= int(input("Seleccione una opción: "))
    if opc == 12:
        print("Saliendo de la calculadora...")
        break
    if opc not in operaciones:
        print("Opción no válida, intente de nuevo.")
        continue
    
    a=float(input("Ingrese el primer número: "))
    b=float(input("Ingrese el segundo número: "))
    r=operaciones[opc](a, b)
    print(f"El resultado es: {r}")
    
    