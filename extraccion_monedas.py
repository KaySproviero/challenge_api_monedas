import requests
from datetime import datetime
import csv


pares = ["USD-BRL", "EUR-BRL", "BTC-BRL"]

url = f"https://economia.awesomeapi.com.br/json/last/{','.join(pares)}"

respuesta = requests.get(url)


if respuesta.status_code == 200:
    datos = respuesta.json()

   
    filas = []

   
    for clave in datos:
        info = datos[clave]

        moneda_base = info["code"]
        moneda_destino = info["codein"]
        valor_compra = float(info["bid"])
        valor_venta = float(info["ask"])
        timestamp = int(info["timestamp"])
        fecha_hora = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

       
        fila = [
            moneda_base,
            moneda_destino,
            valor_compra,
            valor_venta,
            fecha_hora
        ]
        filas.append(fila)

    
    nombre_archivo = "cotizacion_monedas.csv"
    with open(nombre_archivo, mode="w", newline='', encoding='utf-8') as archivo_csv:
        escritor = csv.writer(archivo_csv, delimiter=';')
        escritor.writerow(["moneda_base", "moneda_destino", "valor_compra", "valor_venta", "data_hora"])
        escritor.writerows(filas)

    print(f" Los datos se guardaron en el archivo '{nombre_archivo}'")

else:
    print(f" Se produjo un Error al acceder a la API. Código de estado: {respuesta.status_code}")
