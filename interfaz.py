import tkinter as tk
from calculadora import Calculadora

# =========================
# VENTANA
# =========================
ventana = tk.Tk()
ventana.title("Calculadora Pro")
ventana.geometry("400x550")
ventana.config(bg="lightgray")

calc = Calculadora()

# =========================
# ESTADO
# =========================
texto_pantalla = tk.StringVar()
expresion = ""


# =========================
# PANTALLA
# =========================
pantalla = tk.Entry(
    ventana,
    textvariable=texto_pantalla,
    font=("Arial", 24),
    bd=10,
    relief=tk.RIDGE,
    justify="right",
    bg="white"
)
pantalla.pack(padx=10, pady=10, ipady=10, fill="x")


# =========================
# FUNCIONES
# =========================
def agregar(valor):
    global expresion
    expresion += str(valor)
    texto_pantalla.set(expresion)


def limpiar():
    global expresion
    expresion = ""
    texto_pantalla.set("")


def set_operacion(op):
    global expresion

    if expresion == "":
        return

    expresion += f" {op} "
    texto_pantalla.set(expresion)


def igual():
    global expresion

    try:
        partes = expresion.split()

        if len(partes) != 3:
            return

        num1 = float(partes[0])
        op = partes[1]
        num2 = float(partes[2])

        if op == "+":
            resultado = calc.sumar(num1, num2)

        elif op == "-":
            resultado = calc.restar(num1, num2)

        elif op == "*":
            resultado = calc.multiplicar(num1, num2)

        elif op == "/":
            resultado = calc.dividir(num1, num2)

        else:
            resultado = "Error"

        expresion = str(resultado)
        texto_pantalla.set(expresion)

    except:
        expresion = ""
        texto_pantalla.set("Error")


# =========================
# FUNCIONES CIENTÍFICAS
# =========================
def raiz():
    global expresion
    try:
        num = float(expresion)
        expresion = str(calc.raiz_cuadrada(num))
        texto_pantalla.set(expresion)
    except:
        expresion = ""
        texto_pantalla.set("Error")


def potencia():
    global expresion
    try:
        num = float(expresion)
        expresion = str(calc.potencia(num, 2))
        texto_pantalla.set(expresion)
    except:
        expresion = ""
        texto_pantalla.set("Error")


def logaritmo():
    global expresion
    try:
        num = float(expresion)
        expresion = str(calc.logaritmo(num))
        texto_pantalla.set(expresion)
    except:
        expresion = ""
        texto_pantalla.set("Error")


def seno():
    global expresion
    try:
        num = float(expresion)
        expresion = str(calc.seno(num))
        texto_pantalla.set(expresion)
    except:
        expresion = ""
        texto_pantalla.set("Error")


def coseno():
    global expresion
    try:
        num = float(expresion)
        expresion = str(calc.coseno(num))
        texto_pantalla.set(expresion)
    except:
        expresion = ""
        texto_pantalla.set("Error")


def tangente():
    global expresion
    try:
        num = float(expresion)
        expresion = str(calc.tangente(num))
        texto_pantalla.set(expresion)
    except:
        expresion = ""
        texto_pantalla.set("Error")


# =========================
# BOTONES CENTRALIZADOS
# =========================
def manejar_boton(b):

    if b == "C":
        limpiar()

    elif b == "=":
        igual()

    elif b == "√":
        raiz()

    elif b == "x²":
        potencia()

    elif b == "log":
        logaritmo()

    elif b == "sin":
        seno()

    elif b == "cos":
        coseno()

    elif b == "tan":
        tangente()

    elif b in ["+", "-", "*", "/"]:
        set_operacion(b)

    else:
        agregar(b)


# =========================
# BOTONES
# =========================
frame = tk.Frame(ventana, bg="lightgray")
frame.pack()

lista_botones = [
    "tan", "cos", "sin", "log",
    "√", "x²", "C", "/",
    "7", "8", "9", "*",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "0", ".", "=", ")"
]

fila = 0
columna = 0

for boton in lista_botones:

    btn = tk.Button(
        frame,
        text=boton,
        font=("Arial", 16),
        width=5,
        height=2,
        command=lambda b=boton: manejar_boton(b)
    )

    btn.grid(row=fila, column=columna, padx=5, pady=5)

    columna += 1

    if columna > 3:
        columna = 0
        fila += 1


ventana.mainloop()