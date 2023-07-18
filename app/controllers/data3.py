import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas

# Datos ficticios de la tabla
data = [
    {
        "nombre_tarea": "Tarea 1",
        "descripcion": "Realizar análisis de requisitos",
        "tiempo_inicio": "08:00",
        "tiempo_termino": "09:30",
        "tiempo_total": 1.5,
        "accion": "Completada"
    },
    {
        "nombre_tarea": "Tarea 2",
        "descripcion": "Desarrollar el componente X",
        "tiempo_inicio": "10:00",
        "tiempo_termino": "12:30",
        "tiempo_total": 2.5,
        "accion": "Completada"
    },
    # Agrega más datos ficticios aquí si es necesario
]

# Obtener los nombres de las tareas y sus tiempos totales
nombres_tareas = [tarea["nombre_tarea"] for tarea in data]
tiempos_totales = [tarea["tiempo_total"] for tarea in data]

# Crear el gráfico de barras
plt.subplot(1, 2, 1)  # Gráfico de barras
plt.bar(nombres_tareas, tiempos_totales)
plt.xlabel("Tarea")
plt.ylabel("Tiempo Total")
plt.title("Gráfico de barras de tiempo total por tarea")
plt.xticks(rotation=90)

# Crear el gráfico de torta
plt.subplot(1, 2, 2)  # Gráfico de torta
plt.pie(tiempos_totales, labels=nombres_tareas, autopct='%1.1f%%')
plt.title("Gráfico de torta de tiempo total por tarea")

# Guardar los gráficos en un archivo PNG
plt.savefig("graficos.png")

# Crear el archivo PDF
pdf = canvas.Canvas("graficos.pdf")
pdf.setPageSize((1000, 400))  # Tamaño personalizado para el PDF

# Agregar la imagen del gráfico de barras al PDF
pdf.drawString(250, 350, "Gráfico de barras de tiempo total por tarea")
pdf.drawInlineImage("graficos.png", 50, 50, width=400, height=300)

# Agregar la imagen del gráfico de torta al PDF
pdf.drawString(750, 350, "Gráfico de torta de tiempo total por tarea")
pdf.drawInlineImage("graficos.png", 500, 50, width=400, height=300)

pdf.save()

# Mostrar los gráficos en una ventana emergente (opcional)
plt.show()
