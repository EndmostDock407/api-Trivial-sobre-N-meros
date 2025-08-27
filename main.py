import requests

# Función que consulta la API local y devuelve la curiosidad sobre el número
def trivia_fetch(number):
    url = f"http://127.0.0.1:5000/dato/{number}"  # URL de la API local
    try:
        response = requests.get(url)  # Realiza la petición GET
        if response.status_code == 200:
            return response.json()  # Devuelve la respuesta en formato JSON
        else:
            # Si la API no responde correctamente, devuelve un mensaje de error
            return {"number": number, "mensaje": "Error al conectar con la API."}
    except Exception as e:
        # Si ocurre una excepción (por ejemplo, la API no está disponible), devuelve el error
        return {"number": number, "mensaje": f"Excepción: {str(e)}"}

# Función principal que interactúa con el usuario
def main():
    numero = int(input("Ingresa un número para obtener su curiosidad local: "))  # Solicita un número al usuario
    resultado = trivia_fetch(numero)  # Obtiene la curiosidad usando la función trivia_fetch
    if "categoria" in resultado:
        # Si existe la categoría, muestra la curiosidad y la categoría
        print(f"Número: {resultado['number']}")
        print(f"Categoría: {resultado['categoria']}")
        print(f"Curiosidad: {resultado['curiosidad']}")
    else:
        # Si no existe la categoría, muestra el mensaje de error
        print(resultado["mensaje"])

# Ejecuta la función principal solo si el archivo se ejecuta directamente
if __name__ == "__main__":
    main()
