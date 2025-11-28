import tkinter as tk
from tkinter import messagebox
from operaciones import suma, resta, multiplicacion, division


def on_sum():
	a = entry_a.get()
	b = entry_b.get()
	try:
		resultado = suma(a, b)
		label_result.config(text=f"Resultado: {resultado}")
	except ValueError as e:
		messagebox.showerror("Error", str(e))


def on_sub():
	a = entry_a.get()
	b = entry_b.get()
	try:
		resultado = resta(a, b)
		label_result.config(text=f"Resultado: {resultado}")
	except ValueError as e:
		messagebox.showerror("Error", str(e))


def on_mul():
	a = entry_a.get()
	b = entry_b.get()
	try:
		resultado = multiplicacion(a, b)
		label_result.config(text=f"Resultado: {resultado}")
	except ValueError as e:
		messagebox.showerror("Error", str(e))


def on_div():
	a = entry_a.get()
	b = entry_b.get()
	try:
		resultado = division(a, b)
		label_result.config(text=f"Resultado: {resultado}")
	except ValueError as e:
		messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Calculadora")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="A:").grid(row=0, column=0)
entry_a = tk.Entry(frame)
entry_a.grid(row=0, column=1)

tk.Label(frame, text="B:").grid(row=1, column=0)
entry_b = tk.Entry(frame)
entry_b.grid(row=1, column=1)

btn_sum = tk.Button(frame, text="Sumar", width=12, command=on_sum)
btn_sum.grid(row=2, column=0, pady=5)
btn_sub = tk.Button(frame, text="Restar", width=12, command=on_sub)
btn_sub.grid(row=2, column=1, pady=5)
btn_mul = tk.Button(frame, text="Multiplicar", width=12, command=on_mul)
btn_mul.grid(row=3, column=0, pady=5)
btn_div = tk.Button(frame, text="Dividir", width=12, command=on_div)
btn_div.grid(row=3, column=1, pady=5)

label_result = tk.Label(frame, text="Resultado: ")
label_result.grid(row=4, column=0, columnspan=2, pady=(10,0))

if __name__ == "__main__":
	root.mainloop()

