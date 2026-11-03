from pathlib import Path
import csv
import matplotlib.pyplot as plt

Path("outputs").mkdir(parents=True, exist_ok=True)

def explorar_directorio():
    carpeta = Path(input("Ruta de la carpeta: "))
    if carpeta.exists():
        for a in carpeta.iterdir():
            if str(a).endswith(".txt") or str(a).endswith(".csv"):
                print("-", a)
    else:
        print("La carpeta no existe.")

def contar_palabras(lineas):
    conectores = ["el", "la", "los", "las", "un", "una", "de", "del", "a", "en", "con", "por", "para", "y", "o", "que", "se", "es", "al"]
    conteo = {}
    for linea in lineas:
        for p in linea.lower().split():
            w = p.strip(".,;:!?()[]{}\"'0123456789-")
            if w != "" and w not in conectores:
                conteo[w] = conteo.get(w, 0) + 1
    pares = []
    for w in conteo:
        pares.append([conteo[w], w])
    pares.sort(reverse=True)
    return pares

def resumen_txt(lineas):
    pal = 0
    con_esp = 0
    sin_esp = 0
    for l in lineas:
        pal = pal + len(l.split())
        con_esp = con_esp + len(l)
        sin_esp = sin_esp + len(l.replace(" ", "").replace("\n", ""))
    print("Lineas:", len(lineas), "| Palabras:", pal, "| Con esp:", con_esp, "| Sin esp:", sin_esp)
    print("Top 5 palabras mas repetidas:")
    for item in contar_palabras(lineas)[:5]:
        print("-", item[1], ":", item[0])

def patrones_txt(lineas):
    pat = input("Fecha o patron a buscar: ")
    err, e404, busq = 0, 0, 0
    for l in lineas:
        if "ERROR" in l: err = err + 1
        if "404" in l: e404 = e404 + 1
        if pat != "" and pat in l: busq = busq + 1
    print("ERROR:", err, "| 404:", e404, "| Patron buscado:", busq)

def grafico_barh(lineas):
    pal, cant = [], []
    for item in contar_palabras(lineas)[:10]:
        cant.append(item[0])
        pal.append(item[1])
    plt.barh(pal, cant)
    plt.title("Top 10 Palabras Clave")
    plt.xlabel("Frecuencia")
    plt.ylabel("Palabras")
    plt.savefig(Path("outputs") / "grafico1_frecuencia.png")
    plt.show()

def grafico_hist(lineas):
    largos = []
    for l in lineas:
        largos.append(len(l.strip("\n")))
    plt.hist(largos, bins=[0, 50, 100, 150, 200])
    plt.title("Distribucion de Longitud de Lineas")
    plt.xlabel("Caracteres por linea")
    plt.ylabel("Cantidad de lineas")
    plt.savefig(Path("outputs") / "grafico2_longitud.png")
    plt.show()

def submenu_txt():
    try:
        with open(Path(input("Ruta del archivo .txt: ")), "r", encoding="utf-8") as f:
            lineas = f.readlines()
    except FileNotFoundError:
        return print("Error: Archivo no encontrado.")
    op = ""
    while op != "5":
        op = input("\n1.Resumen  2.Patrones  3.Grafico barh  4.Grafico hist  5.Volver: ")
        if op == "1": resumen_txt(lineas)
        elif op == "2": patrones_txt(lineas)
        elif op == "3": grafico_barh(lineas)
        elif op == "4": grafico_hist(lineas)

def elegir_col(enc):
    for i in range(len(enc)):
        print(i, "->", enc[i])
    return int(input("Numero de columna: "))

def estadisticas_csv(enc, filas):
    col = elegir_col(enc)
    datos = []
    for f in filas:
        try:
            datos.append(float(f[col]))
        except ValueError:
            pass
    datos.sort()
    n = len(datos)
    if n == 0:
        return print("No hay datos numericos.")
    med = datos[n // 2] if n % 2 == 1 else (datos[n // 2 - 1] + datos[n // 2]) / 2
    print("Validos:", n, "| Promedio:", round(sum(datos) / n, 2), "| Mediana:", med)
    print("Maximo:", max(datos), "| Minimo:", min(datos))

def grafico_plot(enc, filas):
    cx, cy = elegir_col(enc), elegir_col(enc)
    x, y = [], []
    for f in filas:
        try:
            y.append(float(f[cy]))
            x.append(f[cx])
        except ValueError:
            pass
    plt.plot(x, y)
    plt.title("Tendencia de " + enc[cy])
    plt.xlabel(enc[cx])
    plt.ylabel(enc[cy])
    plt.savefig(Path("outputs") / "grafico3_tendencia.png")
    plt.show()

def grafico_pie(enc, filas):
    col = elegir_col(enc)
    conteo = {}
    for f in filas:
        if f[col] != "":
            conteo[f[col]] = conteo.get(f[col], 0) + 1
    plt.pie(list(conteo.values()), labels=list(conteo.keys()), autopct="%1.1f%%")
    plt.title("Participacion por " + enc[col])
    plt.savefig(Path("outputs") / "grafico4_pastel.png")
    plt.show()

def grafico_scatter(enc, filas):
    cx, cy = elegir_col(enc), elegir_col(enc)
    x, y = [], []
    for f in filas:
        try:
            x.append(float(f[cx]))
            y.append(float(f[cy]))
        except ValueError:
            pass
    plt.scatter(x, y)
    plt.title(enc[cx] + " vs " + enc[cy])
    plt.xlabel(enc[cx])
    plt.ylabel(enc[cy])
    plt.savefig(Path("outputs") / "grafico5_dispersion.png")
    plt.show()

def submenu_csv():
    try:
        with open(Path(input("Ruta del archivo .csv: ")), "r", encoding="utf-8", newline="") as f:
            lector = csv.reader(f, delimiter=",")
            enc = next(lector)
            filas = list(lector)
    except FileNotFoundError:
        return print("Error: Archivo no encontrado.")
    op = ""
    while op != "6":
        op = input("\n1.Vista Previa  2.Estadisticas  3.Grafico plot  4.Grafico pie  5.Grafico scatter  6.Volver: ")
        if op == "1":
            print("Columnas:", enc, "\nPrimeras 10:", filas[:10], "\nUltimas 5:", filas[-5:])
        elif op == "2": estadisticas_csv(enc, filas)
        elif op == "3": grafico_plot(enc, filas)
        elif op == "4": grafico_pie(enc, filas)
        elif op == "5": grafico_scatter(enc, filas)

op_p = ""
while op_p != "4":
    op_p = input("\n=== MENU PRINCIPAL ===\n1.Explorar directorio  2.Procesar TXT  3.Analizar CSV  4.Salir: ")
    if op_p == "1": explorar_directorio()
    elif op_p == "2": submenu_txt()
    elif op_p == "3": submenu_csv()