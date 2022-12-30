import csv
import requests
import time

# Tu clave de API de Pipedrive
api_key = "Tu clave de API de Pipedrive"

# La URL de la API de leads de Pipedrive
url = "https://api.pipedrive.com/v1/leads"

# Los parámetros de la solicitud, incluyendo la clave de API
query_params = {
    "api_token": api_key,
    "start": 0,  # Iniciar en la primera página de resultados
    "limit": 500
}

# La lista completa de leads
all_leads = []

# Bandera para indicar si hay más páginas de resultados
more_results = True

while more_results:
    # Hacer la solicitud a la API
    response = requests.get(url, params=query_params)

    # Comprobar si la solicitud tuvo éxito
    if response.status_code == 200:
        # Obtener los datos de la respuesta en formato JSON
        leads = response.json()["data"]

        # Añadir los leads a la lista completa
        all_leads.extend(leads)

        # Añadir un tiempo de espera antes de comprobar si hay más páginas de resultados
        time.sleep(1)

        print (len(leads))

        # Comprobar si hay más páginas de resultados
        if len(leads) < query_params["limit"]:
            more_results = False
        else:
            query_params["start"] += query_params["limit"]
    else:
        print("Error al hacer la solicitud")
        more_results = False

# Mostrar la lista completa de leads
print(all_leads)

# Abrir un archivo CSV para escribir
with open("leads.csv", "w", newline="") as csv_file:
    # Crear un objeto de escritor CSV
    writer = csv.DictWriter(csv_file, fieldnames=all_leads[0].keys())

    # Escribir el encabezado de columna
    writer.writeheader()

    # Iterar sobre cada lead y escribir cada fila en el archivo CSV
    for lead in all_leads:
        writer.writerow(lead)


