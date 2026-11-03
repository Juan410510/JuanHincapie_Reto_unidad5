# Reto Unidad 5 - Análisis de Datos Reales

Este proyecto es una aplicación de consola en Python para leer, analizar y graficar datos de archivos reales de texto (`.txt`) y tablas (`.csv`), usando la librería `matplotlib`.

## 1. Archivos de datos utilizados (`data/`)

* **`servidor_logs.txt`:**
  Es un archivo de bitácora (log) con 30 registros de un servidor web. Cada línea tiene la fecha, la hora, el tipo de mensaje (`INFO`, `WARNING`, `ERROR`) y la acción que ocurrió (como usuarios iniciando sesión, consultas a la base de datos o errores `404` cuando no se encuentra una página o un archivo).

* **`clima_ventas.csv`:**
  Es una tabla con 18 filas que registra las ventas mensuales de una tienda en 4 ciudades de Colombia (Medellín, Bogotá, Cali y Barranquilla), junto con la temperatura promedio de cada mes. Tiene columnas de Fecha, Ciudad, Temperatura, Ventas e Ingresos, y dejamos una casilla vacía a propósito en la temperatura de Bogotá para verificar que el código limpia los datos nulos sin romperse.

## 2. Conclusiones del análisis visual

Al revisar los 5 gráficos generados por el programa, descubrimos lo siguiente:

### Conclusión 1: El servidor es estable pero tiene enlaces rotos (Gráficos 1 y 2)

Al mirar el gráfico de barras horizontales (`barh`) y el histograma (`hist`), vemos que la palabra que más se repite con diferencia es `INFO` (15 veces), lo que demuestra que el servidor trabaja bien la mayor parte del tiempo. Sin embargo, el error más común es el código `404` (6 apariciones). Esto nos dice que el sistema no se está cayendo, sino que hay enlaces viejos o archivos que ya no existen (como un manual en PDF y una imagen del catálogo) que los usuarios siguen intentando abrir.

### Conclusión 2: Las ventas se concentran en las ciudades cálidas (Gráficos 3 y 4)

En el gráfico de pastel (`pie`) y el de líneas (`plot`) se ve clarito que las ciudades de clima caliente (Barranquilla y Cali) concentran más de la mitad de todas las ventas del año (más del 55%). En cambio, en ciudades frías como Bogotá las ventas se quedan por debajo de las 100 unidades. Además, la tendencia en el tiempo muestra que las ventas se mantienen constantes pero tienen sus picos en los meses de mitad y final de año.

### Conclusión 3: A más calor, mayores ventas e ingresos (Gráfico 5)

Al cruzar la temperatura contra las ventas en el gráfico de dispersión (`scatter`), los puntos muestran una relación directa muy clara: entre más alta es la temperatura de la ciudad, más producto se vende. En Bogotá, con temperaturas alrededor de 14°C, los ingresos no pasan de \$1,900 USD, mientras que en Barranquilla, con más de 31°C, los ingresos superan los $4,200 USD. Esto confirma que el clima de cada región es el factor que más influye en las ventas de este negocio.