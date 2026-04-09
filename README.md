# First term exam - Practical

Para activar nuestra api ejecutaremos:


source venv/bin/activate
pip install fastapi uvicorn sqlmodel requests
uvicorn main:app --reload

Toda la documentacion esta en: http://127.0.0.1:8000/docs

## Usuarios quemados en código
admin = admin
user = user
guest = guest

## Prueba de Fuerza Bruta

Con la API corriendo, debemos abrir otra terminal y ejecutamos:

source venv/bin/activate
python3 bruteforce.py


El script genera todas las combinaciones posibles de letras minúsculas (a-z) y las envía al endpoint /login hasta encontrar la contraseña.

## Resultados

lopez@Oliver:~/api$ python3 bruteforce.py
Contraseña encontrada: abd
Intentos: 732
Tiempo: 35.16 segundos

## Conclusión

La contraseña "abd" fue encontrada en solo 732 intentos y 35 segundos, lo que demuestra que contraseñas cortas y simples son vulnerables a fuerza bruta. 
Para mitigar esto se recomienda usar contraseñas largas con mayúsculas, números y símbolos, además de implementar límite de intentos y bloqueo de cuenta.
