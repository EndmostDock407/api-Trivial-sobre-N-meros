from flask import Flask, jsonify
import json

# Crear la aplicación Flask
app = Flask(__name__)

# Cargar los datos curiosos desde el archivo JSON
with open('datos.json', 'r', encoding='utf-8') as f:
    datos = json.load(f)

# Definir la ruta para obtener la curiosidad de un número
@app.route('/dato/<int:numero>', methods=['GET'])
def obtener_dato(numero):
    numero_str = str(numero)  # Convertir el número a string para buscar en el diccionario
    if numero_str in datos:
        # Si el número existe en los datos, devolver la curiosidad y la categoría
        return jsonify({
            "number": numero,
            "categoria": datos[numero_str]["categoria"],
            "curiosidad": datos[numero_str]["curiosidad"]
        })
    else:
        # Si el número no existe, devolver un mensaje de error
        return jsonify({
            "number": numero,
            "mensaje": "No hay datos curiosos para este número."
        })

# Ejecutar la aplicación si el archivo se ejecuta directamente
if __name__ == '__main__':
    app.run(debug=True)
