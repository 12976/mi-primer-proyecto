import tkinter as tk
import math

AZUL = "#0033A0"
BLANCO = "white"

def click(valor):
    entrada.insert(tk.END, valor)

def borrar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

ventana = tk.Tk()
ventana.title("honorAIno_Fdez2 - Circular Calculator")
ventana.geometry("520x620")
ventana.config(bg=AZUL)

tk.Label(ventana, text="SESE - ABRERA", bg=AZUL, fg=BLANCO,
         font=("Arial", 22, "bold")).pack(pady=8)

tk.Label(ventana, text="SQA", bg=AZUL, fg=BLANCO,
         font=("Arial", 18, "bold")).pack()

tk.Label(ventana, text="€ from Suppliers to SESE ABRERA", bg=AZUL, fg=BLANCO,
         font=("Arial", 12)).pack(pady=5)

entrada = tk.Entry(ventana, font=("Arial", 22), justify="right")
entrada.pack(padx=30, pady=15, fill="x", ipady=10)

canvas = tk.Canvas(ventana, width=500, height=420, bg=AZUL, highlightthickness=0)
canvas.pack()

centro_x = 250
centro_y = 210
radio = 140

botones = ["7", "8", "9", "/", "*", "6", "3", "+", "=", "0", "C", "1", "4", "5", "2", "-"]

def crear_boton(texto, x, y):
    boton = tk.Button(
        ventana,
        text=texto,
        font=("Arial", 16, "bold"),
        width=4,
        height=2,
        bg=BLANCO,
        fg=AZUL,
        command=calcular if texto == "=" else borrar if texto == "C" else lambda t=texto: click(t)
    )
    canvas.create_window(x, y, window=boton)

for i, texto in enumerate(botones):
    angulo = 2 * math.pi * i / len(botones)
    x = centro_x + radio * math.cos(angulo)
    y = centro_y + radio * math.sin(angulo)
    crear_boton(texto, x, y)

canvas.create_oval(centro_x-55, centro_y-55, centro_x+55, centro_y+55,
                   fill=BLANCO, outline=BLANCO)

canvas.create_text(centro_x, centro_y, text="SQA", fill=AZUL,
                   font=("Arial", 22, "bold"))

ventana.mainloop()