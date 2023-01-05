import sqlite3

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
import requests
import json

def crerBase():


    # Conecta a la base de datos (se creará automáticamente si no existe)
    conn = sqlite3.connect("mi_base_de_datos.db")

    # Crea un cursor para ejecutar las consultas
    cursor = conn.cursor()

    # Crea la tabla
    cursor.execute("CREATE TABLE tabla_colores (color_1 INTEGER, color_2 INTEGER)")

    # Agrega algunos datos a la tabla
    cursor.execute("INSERT INTO tabla_colores VALUES (50, 20)")
    cursor.execute("INSERT INTO tabla_colores VALUES (20, 30)")
    cursor.execute("INSERT INTO tabla_colores VALUES (60, 80)")
    cursor.execute("INSERT INTO tabla_colores VALUES (60, 23)")

    # Guarda los cambios en la base de datos
    conn.commit()

    # Cierra el cursor y la conexión
    cursor.close()
    conn.close()

def ver():
    # Conecta a la base de datos
    conn = sqlite3.connect("mi_base_de_datos.db")

    # Crea un cursor para ejecutar la consulta
    cursor = conn.cursor()

    # Ejecuta la consulta y obtiene los resultados
    cursor.execute("SELECT * FROM tabla_colores")
    results = cursor.fetchall()

    # Cierra el cursor y la conexión
    cursor.close()
    conn.close()

    # Crea una lista de tuplas con los resultados
    # Obtiene el nombre de la columna
    nombre_columna_1 = cursor.description[0][0]
    nombre_columna_2 = cursor.description[1][0]
    columna_1 = [(row[0]) for row in results]
    columna_2 = [(row[1]) for row in results]

    cliente="Banco Pichincha"
    entorno = "Test"
    asunto = "Tablas"

    # Grafica los datos

    fig = plt.figure(figsize=(8,4))
    fig.tight_layout()
    ax1 = fig.add_subplot(1,2,2)
    ax2 = fig.add_subplot(1,2,1)

    ax1.bar(range(1, len(columna_1) + 1), columna_1, width=0.4, label=nombre_columna_1)
    ax1.plot(range(1, len(columna_2) + 1), columna_2, color="orange", label=nombre_columna_2)

    # Agrega etiquetas a los ejes y un título al gráfico

    ax1.set_xlabel("Índices")
    ax1.set_ylabel("Valores")
    ax1.set_title("Reporte")

    # Agrega una leyenda
    ax1.legend()

    # Configura el eje x para que solo muestre enteros
    plt.xticks(range(1, len(columna_1) + 1))

    # Crea una tabla con los datos de las columnas
    ax2.table(cellText=results, colLabels=[nombre_columna_1, nombre_columna_2], loc='upper center')
    ax2.axis('off')
    ax2.axis('tight')
    ax2.text(0, -0.03, "Cliente: "+str(cliente) + "\nEntorno: "+str(entorno)+"\nAsunto: "+str(asunto))


    plt.subplots_adjust(wspace=0.4)

    # Muestra el gráfico
    plt.show()

def mandarTelegra():


    # Tu token de bot
    bot_token = "5818144839:AAFfOzq7Qo2ynP0XOnCqOOJQsfaeQqXwMLY"

    # La ID del chat donde quieres enviar la imagen
    chat_id = "-875581438"

    # El nombre del archivo de la imagen que quieres enviar
    image_file = "/content/FIFA.png"

    # Crea el URL para enviar la imagen
    url = "https://api.telegram.org/bot{}/sendPhoto".format(bot_token)

    # Sube el archivo de la imagen
    files = {"photo": open(image_file, "rb")}
    data = {"chat_id": chat_id}
    response = requests.post(url, files=files, data=data)

    # Verifica que el envío haya sido exitoso
    if response.status_code != 200:
        raise Exception("Error al enviar la imagen: {}".format(response.status_code))

    print("Imagen enviada con éxito!")

if __name__ == '__main__':
    #crerBase()
    ver()
