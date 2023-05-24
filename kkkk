import msvcrt

def obtener_opciones_comida_rapida():
    opciones = ["Hamburguesa", "Pizza", "Hot Dog", "Pollo frito", "Tacos"]
    print("Opciones de comida rápida:")
    for opcion in opciones:
        print("- " + opcion)

# Función para esperar la tecla "r"
def esperar_tecla_r():
    while True:
        if msvcrt.kbhit():
            tecla = msvcrt.getch().decode("utf-8").lower()
            if tecla == "r":
                break

# Esperar la tecla "r" y mostrar las opciones de comida rápida
print("Presiona la tecla 'r' para ver las opciones de comida rápida.")
esperar_tecla_r()
obtener_opciones_comida_rapida()
