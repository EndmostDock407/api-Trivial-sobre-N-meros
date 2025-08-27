# Trivia de Números - Proyecto Python

Este proyecto consiste en una aplicación de trivia sobre números, desarrollada en Python. Incluye una API local con Flask, un cliente que consulta la API y un conjunto de tests automáticos.

## Estructura del proyecto

- **app.py**  
  API local desarrollada con Flask. Expone una ruta `/dato/<int:numero>` que devuelve curiosidades sobre el número consultado, usando los datos de `datos.json`.

- **datos.json**  
  Archivo con curiosidades y categorías para varios números.

- **main.py**  
  Cliente que solicita al usuario un número, consulta la API local y muestra la curiosidad correspondiente.

- **test_.py**  
  Archivo de pruebas automáticas que verifica que la función `trivia_fetch` retorna correctamente el número consultado.

## Detalles técnicos

- Toda la lógica interactiva debe estar dentro de la función `main()`.
- La función principal debe estar protegida con el *boilerplate* estándar de Python:
  ```python
  def main():
      # lógica interactiva aquí

  if __name__ == "__main__":
      main()
  ```
- La función `trivia_fetch(num)` debe recibir un número y devolver un diccionario con la trivia correspondiente.
- Los datos de trivia se obtienen desde la API local, que a su vez lee de `datos.json`.
- Los tests automáticos verifican que la clave `"number"` en el diccionario devuelto por `trivia_fetch` coincide con el número consultado.

## Cómo ejecutar el proyecto

1. **Instala las dependencias**  
   Abre la terminal y ejecuta:
   ```
   pip install flask requests
   ```

2. **Inicia la API local**  
   Ejecuta en la terminal:
   ```
   python app.py
   ```
   Esto iniciará el servidor Flask en `http://127.0.0.1:5000`.

3. **Ejecuta el cliente**  
   En otra terminal, ejecuta:
   ```
   python main.py
   ```
   Ingresa un número cuando se te solicite y verás la curiosidad correspondiente.

4. **Ejecuta los tests**  
   Para verificar el correcto funcionamiento, ejecuta:
   ```
   pytest --cov
   ```

## Ejemplo de uso

```
Ingresa un número para obtener su curiosidad local: 42
Número: 42
Categoría: Cultura pop
Curiosidad: Es la respuesta a la vida, el universo y todo, según Douglas Adams.
```

## Personalización

- Puedes agregar más curiosidades editando el archivo `datos.json`.
- Puedes modificar la lógica de la API en `app.py` para cambiar el formato de respuesta o agregar nuevas rutas.
- Puedes ampliar los tests en `test_.py` para cubrir más casos y mejorar la cobertura.

## Uso de IA en el desarrollo

- Se utilizó IA para investigar sobre APIs públicas de trivia de números, como [numbersapi.com](http://numbersapi.com/), y sobre cómo crear una API propia con Flask.
- La IA ayudó a identificar buenas prácticas de desarrollo, como el uso de funciones, separación de lógica interactiva y estructuración de pruebas automáticas.
- Se empleó IA para generar ejemplos de código, sugerir mejoras y asegurar la compatibilidad con sistemas de evaluación automática.
