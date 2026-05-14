import math

class Calculadora:
    def sumar(self, a, b):
        return a + b
    def restar(self, a, b):
        return a - b
    def multiplicar(self, a, b):
        return a * b
    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b
    def potencia(self, a, b):
        return math.pow(a, b)
    def raiz_cuadrada(self, a):
        if a < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
        return math.sqrt(a) 
    def logaritmo(self, a, base=math.e):
        if a <= 0:
            raise ValueError("No se puede calcular el logaritmo de un número no positivo")
        if base <= 1:
            raise ValueError("La base del logaritmo debe ser mayor que 1")
        return math.log(a, base)
    def seno(self, a):
        return math.sin(a)
    def coseno(self, a):
        return math.cos(a)
    def tangente(self, a):
        return math.tan(a)  
    def factorial(self, a):
        if a < 0:
            raise ValueError("No se puede calcular el factorial de un número negativo")
        return math.factorial(a)
    