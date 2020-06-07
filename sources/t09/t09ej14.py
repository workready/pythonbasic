import asyncio

async def snooze(i):
    print("Corrutina {} durmiendo 5 segundos".format(i))
    
    # En este punto, snooze se detiene durante 5 segundos, hasta que asyncio.sleep vuelve.
    await asyncio.sleep(5)

    print("Corrutina {} despierta".format(i))


loop = asyncio.get_event_loop()

# Vamos a esperar a un conjunto de tareas que se ejecutarán en un bucle
tasks = []

for i in range(10):
    # Metemos la tarea en una estructura de datos que nos asegura que se va a mantener viva 
    # hasta que la tarea se complete. Podría compararse a una promesa en JavaScript
    tasks.append(asyncio.ensure_future(snooze(i)))  # <1>

# Ejecutamos el bucle de eventos hasta que terminen todas las tareas
loop.run_until_complete(asyncio.wait(tasks))

# Cerramos
loop.close()

