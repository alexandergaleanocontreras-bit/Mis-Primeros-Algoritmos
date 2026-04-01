# Nombres: ALEXANDER CASAMACHIN GALEANO
# DANIEL FERNANDO MONTAÑO

import tkinter as tk
from tkinter import messagebox

# Listas de productos
codigos = ["P001", "P002", "P003", "P004", "P005"]
nombres = ["Cuaderno", "Lapiz", "Mochila", "Goma", "Pluma"]
precios = [25.0, 5.0, 320.0, 3.0, 18.0]
stocks = [30, 100, 15, 50, 40]

# Listas para ventas
ventas_totales = []
ventas_cantidades = []
ventas_productos = []

# Funciones

def buscar_producto_por_codigo(codigo):
    if codigo in codigos:
        return codigos.index(codigo)
    return -1

def registrar_venta():
    codigo = entrada_codigo.get().strip()
    cantidad_txt = entrada_cantidad.get().strip()

    if codigo == "" or cantidad_txt == "":
        messagebox.showerror("Error", "Debe llenar todos los campos.")
        return

    if not cantidad_txt.isdigit():
        messagebox.showerror("Error", "La cantidad debe ser un número entero.")
        return

    cantidad = int(cantidad_txt)
    if cantidad <= 0:
        messagebox.showerror("Error", "La cantidad debe ser mayor que cero.")
        return

    indice = buscar_producto_por_codigo(codigo)
    if indice == -1:
        messagebox.showerror("Error", "El código ingresado no existe.")
        return

    if cantidad > stocks[indice]:
        messagebox.showerror("Error", "No hay suficiente stock disponible.")
        return

    total = precios[indice] * cantidad
    stocks[indice] -= cantidad

    ventas_totales.append(total)
    ventas_cantidades.append(cantidad)
    ventas_productos.append(nombres[indice])

    messagebox.showinfo(
        "Venta registrada",
        f"Producto: {nombres[indice]}\nCantidad: {cantidad}\nTotal: ${total:.2f}"
    )

    entrada_codigo.delete(0, tk.END)
    entrada_cantidad.delete(0, tk.END)

def ver_inventario():
    salida.delete("1.0", tk.END)
    salida.insert(tk.END, "INVENTARIO:\n\n")
    for i in range(len(codigos)):
        salida.insert(tk.END,
                      f"Código: {codigos[i]}\n"
                      f"Nombre: {nombres[i]}\n"
                      f"Precio: ${precios[i]:.2f}\n"
                      f"Stock: {stocks[i]}\n\n")

def buscar_productos():
    termino = entrada_busqueda.get().strip().lower()
    salida.delete("1.0", tk.END)

    if termino == "":
        messagebox.showerror("Error", "Ingrese un texto para buscar.")
        return

    salida.insert(tk.END, f"Resultados para '{termino}':\n\n")
    encontrado = False
    for i in range(len(nombres)):
        if termino in nombres[i].lower():
            encontrado = True
            salida.insert(tk.END,
                          f"{codigos[i]} - {nombres[i]} - ${precios[i]} - Stock: {stocks[i]}\n")
    if not encontrado:
        salida.insert(tk.END, "No se encontraron productos.\n")

def ver_reporte():
    salida.delete("1.0", tk.END)
    salida.insert(tk.END, "REPORTE DE VENTAS:\n\n")

    if len(ventas_totales) == 0:
        salida.insert(tk.END, "No hay ventas registradas.\n")
        return

    total_ventas = len(ventas_totales)
    total_recaudado = sum(ventas_totales)

    conteo = {}
    for p in ventas_productos:
        conteo[p] = conteo.get(p, 0) + 1

    mas_vendido = max(conteo, key=conteo.get)

    salida.insert(tk.END, f"Ventas realizadas: {total_ventas}\n")
    salida.insert(tk.END, f"Total recaudado: ${total_recaudado:.2f}\n")
    salida.insert(tk.END, f"Producto más vendido: {mas_vendido}\n")

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Sistema de Ventas - Tienda Universitaria")
ventana.geometry("650x500")

# Registro de venta
frame_venta = tk.LabelFrame(ventana, text="Registrar Venta", padx=10, pady=10)
frame_venta.pack(fill="x", padx=10, pady=5)

tk.Label(frame_venta, text="Código:").grid(row=0, column=0)
entrada_codigo = tk.Entry(frame_venta)
entrada_codigo.grid(row=0, column=1)

tk.Label(frame_venta, text="Cantidad:").grid(row=1, column=0)
entrada_cantidad = tk.Entry(frame_venta)
entrada_cantidad.grid(row=1, column=1)

btn_registrar = tk.Button(frame_venta, text="Registrar Venta", command=registrar_venta)
btn_registrar.grid(row=0, column=3, rowspan=2, padx=20)

# Búsqueda
frame_busqueda = tk.LabelFrame(ventana, text="Buscar Productos", padx=10, pady=10)
frame_busqueda.pack(fill="x", padx=10, pady=5)

tk.Label(frame_busqueda, text="Nombre:").grid(row=0, column=0)
entrada_busqueda = tk.Entry(frame_busqueda)
entrada_busqueda.grid(row=0, column=1)

btn_buscar = tk.Button(frame_busqueda, text="Buscar", command=buscar_productos)
btn_buscar.grid(row=0, column=2, padx=10)

# Botones secundarios
frame_botones = tk.Frame(ventana)
frame_botones.pack(fill="x", padx=10, pady=5)

btn_inventario = tk.Button(frame_botones, text="Ver Inventario", command=ver_inventario)
btn_inventario.pack(side="left", padx=10)

btn_reporte = tk.Button(frame_botones, text="Reporte de Ventas", command=ver_reporte)
btn_reporte.pack(side="left", padx=10)

# Área de salida
salida = tk.Text(ventana, width=80, height=15)
salida.pack(padx=10, pady=10)

ventana.mainloop()