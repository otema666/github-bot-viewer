from selenium import webdriver
import time
from threading import Thread

# Función que ejecuta cada instancia del navegador
def run_browser():
    # Configuración del driver de Firefox
    driver = webdriver.Firefox()

    # Carga la página
    driver.get(f"https://github.com/{profile_name}")

    # Espera 5 segundos
    time.sleep(5)

    # Autorecarga la página cada 5 segundos
    while True:
        driver.refresh()
        time.sleep(0.5)

# Crea una lista de hilos para ejecutar cada instancia del navegador
threads = []
profile_name = str(input("Nombre de usuario de github: "))
num = int(input("Cuantos navegadores quieres abrir a la vez?: "))
for i in range(num):
    t = Thread(target=run_browser)
    threads.append(t)
    t.start()

# Espera a que todos los hilos terminen antes de salir del programa
for t in threads:
    t.join()