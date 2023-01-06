import sqlite3
import os
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
import requests
from flask import Flask, render_template, request, redirect, url_for, send_file

app = Flask(__name__)


def graficar(columna_1, columna_2, nombre_columna_1, nombre_columna_2):
    # Grafica los datos

    fig = plt.figure(figsize=(8,4))
    fig.tight_layout()


    plt.bar(range(1, len(columna_1) + 1), columna_1, width=0.4, label=nombre_columna_1)
    plt.plot(range(1, len(columna_2) + 1), columna_2, color="orange", label=nombre_columna_2)

    # Agrega etiquetas a los ejes y un título al gráfico

    plt.xlabel("Índices")
    plt.ylabel("Valores")
    plt.title("Reporte")

    # Agrega una leyenda
    plt.legend()

    # Configura el eje x para que solo muestre enteros
    plt.xticks(range(1, len(columna_1) + 1))

    # Muestra el gráfico
    #plt.show()

    # Elimina la imagen anterior si existe
    if os.path.exists("images/imagen_web.png"):
        os.remove("images/imagen_web.png")

    # Guarda la figura en la carpeta "imágenes" con el nombre "mi_imagen.png"
    fig.savefig("images/imagen_web.png")


@app.route('/')
def index():
    # Conecta a la base de datos
    conn = sqlite3.connect("mi_base_de_datos.db")

    # Crea un cursor para ejecutar la consulta
    cursor = conn.cursor()

    # Verifica si la tabla existe
    #if 'tabla_colores' in cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall():
    try:
        cursor.execute("SELECT * FROM tabla_colores")
        results = cursor.fetchall()
    except sqlite3.OperationalError:
        cursor.execute(
            "CREATE TABLE tabla_colores (id INTEGER PRIMARY KEY AUTOINCREMENT, color_1 INTEGER, color_2 INTEGER)")
        results = []
        # Ejecuta la consulta y obtiene los resultados
    if cursor.execute("SELECT * FROM tabla_colores").fetchone():

        # Crea una lista de tuplas con los resultados
        # Obtiene el nombre de la columna
        nombre_columna_1 = cursor.description[1][0]
        nombre_columna_2 = cursor.description[2][0]
        columna_1 = [(row[1]) for row in results]
        columna_2 = [(row[2]) for row in results]
        graficar(columna_1, columna_2, nombre_columna_1, nombre_columna_2)

        # Cierra el cursor y la conexión
    cursor.close()
    conn.close()
    return render_template("index.html", datos=results)

@app.route('/mi_grafico')
def mostrar_grafico():
    return send_file('images/imagen_web.png', mimetype='image/png')

@app.route('/insertar', methods=["POST"])
def insertar():
    # Obtiene los datos del formulario
    columna_1 = request.form["columna_1"]
    columna_2 = request.form["columna_2"]

    # Conecta a la base de datos
    conn = sqlite3.connect("mi_base_de_datos.db")
    cursor = conn.cursor()

    # Actualiza la tabla con los nuevos datos
    cursor.execute("INSERT INTO tabla_colores (color_1, color_2) VALUES (?, ?)", (columna_1, columna_2))
    conn.commit()

    # Cierra la conexión a la base de datos
    conn.close()

    # Redirige al usuario a la página principal
    return redirect(url_for("index"))

@app.route("/actualizar", methods=["POST"])
def actualizar():
    # Obtiene los datos del formulario
    id = request.form["id"]
    columna_1 = request.form["columna_1"]
    columna_2 = request.form["columna_2"]

    # Conecta a la base de datos
    conn = sqlite3.connect("mi_base_de_datos.db")
    cursor = conn.cursor()

    # Actualiza los datos de la tabla
    cursor.execute("UPDATE tabla_colores SET color_1=?, color_2=? WHERE id=?", (columna_1, columna_2, id))
    conn.commit()

    # Cierra la conexión a la base de datos
    conn.close()

    # Redirige al usuario a la página principal
    return redirect(url_for("index"))

@app.route("/borrar", methods=["POST"])
def borrar():
    # Obtiene el valor de la solicitud POST
    id = request.form["id"]

    # Crea una conexión a la base de datos (si no existe, la crea)
    conn = sqlite3.connect("mi_base_de_datos.db")

    # Crea un cursor
    cursor = conn.cursor()

    # Borra una fila en la tabla "mi_tabla"
    cursor.execute("DELETE FROM tabla_colores WHERE id = ?", (id,))

    # Guarda los cambios en la base de datos
    conn.commit()

    # Cierra la conexión
    conn.close()

    # Redirige a la ruta "/"
    return redirect(url_for("index"))

@app.route("/enviar",methods=["POST"])
def enviar():
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
    nombre_columna_1 = cursor.description[1][0]
    nombre_columna_2 = cursor.description[2][0]
    columna_1 = [(row[1]) for row in results]
    columna_2 = [(row[2]) for row in results]
    cellText = tuple(zip(columna_1, columna_2))

    cliente =  request.form["cliente"]
    entorno =  request.form["entorno"]
    asunto =  request.form["asunto"]

    # Grafica los datos

    fig = plt.figure(figsize=(8, 4))
    fig.tight_layout()
    ax1 = fig.add_subplot(1, 2, 2)
    ax2 = fig.add_subplot(1, 2, 1)

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
    ax2.table(cellText=cellText, colLabels=[nombre_columna_1, nombre_columna_2], loc='upper center')
    ax2.axis('off')
    ax2.axis('tight')
    ax2.text(0, -0.03, "Cliente: " + str(cliente) + "\nEntorno: " + str(entorno) + "\nAsunto: " + str(asunto))

    plt.subplots_adjust(wspace=0.4)

    # Muestra el gráfico
    #plt.show()

    # Elimina la imagen anterior si existe
    if os.path.exists("images/mi_imagen.png"):
        os.remove("images/mi_imagen.png")

    # Guarda la figura en la carpeta "imágenes" con el nombre "mi_imagen.png"
    fig.savefig("images/mi_imagen.png")

    # Tu token de bot
    bot_token = "5818144839:AAFfOzq7Qo2ynP0XOnCqOOJQsfaeQqXwMLY"

    # La ID del chat donde quieres enviar la imagen
    chat_id = "-820972397"

    # El nombre del archivo de la imagen que quieres enviar
    image_file = "images/mi_imagen.png"

    # Crea el URL para enviar la imagen
    url = "https://api.telegram.org/bot{}/sendPhoto".format(bot_token)

    # Sube el archivo de la imagen
    files = {"photo": open(image_file, "rb")}
    data = {"chat_id": chat_id}
    response = requests.post(url, files=files, data=data)

    # Verifica que el envío haya sido exitoso
    if response.status_code != 200:
        raise Exception("Error al enviar la imagen: {}".format(response.status_code))
        return "Error al enviar la imagen"

    print("Imagen enviada con éxito!")

    return render_template('confirmacion.html')

if __name__ == '__main__':
    app.run(port=5500)
