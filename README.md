Sistema de Ventas con Interfaz Gráfica (Python/Tkinter)
Sales and Inventory System - University Store 🚀
This project is a desktop application developed in Python using the Tkinter library. It allows managing sales and inventory control of a stationery store efficiently, with real-time data validation.

Inventory and Product Details
The system includes the following preloaded materials with their respective identification codes and initial stock quantities:

P001 - Notebook: Price $25.00 | Initial stock: 30 units.

P002 - Pencil: Price $5.00 | Initial stock: 100 units.

P003 - Backpack: Price $320.00 | Initial stock: 15 units.

P004 - Eraser: Price $3.00 | Initial stock: 50 units.

P005 - Pen: Price $18.00 | Initial stock: 40 units.

Stock Control Operation
Search by Code: By entering codes such as P001 or P003, the system locates the exact product using the search_product_by_code function.

Stock Validation: Before processing any sale, the program checks that the requested quantity is not greater than the number stored in the stock list. If there is not enough merchandise, the system blocks the sale and displays an error. Real-Time Update: After each successful sale, the program automatically subtracts the sold quantity from the general inventory (stocks[index] -= quantity), keeping track of what remains available in the store. Report Generation: The system allows viewing a final report indicating the total money collected and which product had the highest turnover (the best-selling one).


Sistema de Ventas con Interfaz Gráfica (Python/Tkinter) 🚀
Sistema de Ventas e Inventario - Tienda Universitaria

Este proyecto es una aplicación de escritorio desarrollada en Python utilizando la librería Tkinter. Permite gestionar las ventas y el control de inventario de una papelería de manera eficiente, con validación de datos en tiempo real.

Detalles de Inventario y Productos
El sistema incluye los siguientes materiales precargados con sus respectivos códigos de identificación y cantidades de stock inicial:

P001 - Cuaderno: Precio $25.00 | Stock inicial: 30 unidades.

P002 - Lápiz: Precio $5.00 | Stock inicial: 100 unidades.

P003 - Mochila: Precio $320.00 | Stock inicial: 15 unidades.

P004 - Borrador: Precio $3.00 | Stock inicial: 50 unidades.

P005 - Bolígrafo: Precio $18.00 | Stock inicial: 40 unidades.

Operación del Control de Stock
Búsqueda por Código: Al ingresar códigos como P001 o P003, el sistema localiza el producto exacto utilizando la función buscar_producto_por_codigo.

Validación de Stock: Antes de procesar cualquier venta, el programa verifica que la cantidad solicitada no sea mayor al número almacenado en la lista de existencias. Si no hay suficiente mercancía, el sistema bloquea la venta y muestra un error.

Actualización en Tiempo Real: Después de cada venta exitosa, el programa resta automáticamente la cantidad vendida del inventario general (stocks[indice] -= cantidad), manteniendo el control de lo que queda disponible en la tienda.

Generación de Reportes: El sistema permite visualizar un informe final que indica el dinero total recaudado y qué producto tuvo la mayor rotación (el más vendido).
