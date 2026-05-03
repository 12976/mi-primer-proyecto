import tkinter as tk
import math

VERDE_OSCURO = "#1B5E20"
VERDE = "#2E7D32"
VERDE_CLARO = "#A5D6A7"
NEGRO = "#1C1C1C"
BLANCO = "#FFFFFF"


def click(valor):
    entrada.insert(tk.END, valor)


def borrar():
    entrada.delete(0, tk.END)


def borrar_uno():
    texto_actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, texto_actual[:-1])


def calcular():
    expresion = entrada.get()
    entorno_seguro = {
        "__builtins__": None,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "log": math.log10,
        "ln": math.log,
        "sqrt": math.sqrt,
        "pi": math.pi,
        "e": math.e,
        "pow": pow,
        "abs": abs,
    }

    try:
        resultado = eval(expresion, entorno_seguro)
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")


ventana = tk.Tk()
ventana.title("Calculadora Científica Verde")
ventana.geometry("520x700")
ventana.config(bg=VERDE_OSCURO)

encabezado = tk.Frame(ventana, bg=VERDE_OSCURO)
encabezado.pack(fill="x")

tk.Label(
    encabezado,
    text="Calculadora Científica",
    bg=VERDE_OSCURO,
    fg=BLANCO,
    font=("Arial", 24, "bold"),
).pack(pady=(12, 4))

tk.Label(
    encabezado,
    text="Tema en color verde",
    bg=VERDE_OSCURO,
    fg=VERDE_CLARO,
    font=("Arial", 13, "bold"),
).pack(pady=(0, 12))

cuerpo = tk.Frame(ventana, bg=VERDE_CLARO)
cuerpo.pack(fill="both", expand=True, padx=16, pady=16)

entrada = tk.Entry(
    cuerpo,
    font=("Arial", 24, "bold"),
    justify="right",
    bg=BLANCO,
    fg=NEGRO,
    relief="flat",
)
entrada.pack(padx=12, pady=16, fill="x", ipady=14)

panel_botones = tk.Frame(cuerpo, bg=VERDE_CLARO)
panel_botones.pack(padx=12, pady=(0, 12), fill="both", expand=True)

botones = [
    ["sin(", "cos(", "tan(", "sqrt("],
    ["log(", "ln(", "pi", "e"],
    ["(", ")", "^", "⌫"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
]


def comando_boton(texto):
    if texto == "=":
        return calcular
    if texto == "C":
        return borrar
    if texto == "⌫":
        return borrar_uno
    if texto == "^":
        return lambda: click("**")
    return lambda t=texto: click(t)


for fila_idx, fila in enumerate(botones):
    for col_idx, texto in enumerate(fila):
        boton = tk.Button(
            panel_botones,
            text=texto,
            font=("Arial", 14, "bold"),
            bg=VERDE,
            fg=BLANCO,
            activebackground=VERDE_OSCURO,
            activeforeground=BLANCO,
            relief="flat",
            command=comando_boton(texto),
        )
        boton.grid(row=fila_idx, column=col_idx, sticky="nsew", padx=4, pady=4, ipady=10)

igual = tk.Button(
    panel_botones,
    text="=",
    font=("Arial", 16, "bold"),
    bg=VERDE_OSCURO,
    fg=VERDE_CLARO,
    activebackground="#0F3D12",
    activeforeground=VERDE_CLARO,
    relief="flat",
    command=calcular,
)
igual.grid(row=len(botones), column=0, columnspan=4, sticky="nsew", padx=4, pady=(10, 4), ipady=12)

for i in range(4):
    panel_botones.columnconfigure(i, weight=1)

for i in range(len(botones) + 1):
    panel_botones.rowconfigure(i, weight=1)

ventana.mainloop()
