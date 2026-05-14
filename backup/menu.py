import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

class Menu:
    def mostrar_menu(self):
        print("Calculadora Pro")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")
        print("6. Raíz cuadrada")
        print("7. Logaritmo")
        print("8. Seno")
        print("9. Coseno")
        print("10. Tangente")
        print("11. Factorial") 
        print("12. Salir")