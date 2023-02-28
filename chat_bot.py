import pyperclip
import pyautogui
import time
import os


# Ruta del directorio actual
dir_actual = os.getcwd()
# Ruta del archivo que se quiere abrir (relativa al directorio actual)
ruta_txt = os.path.join(dir_actual, 'opciones.txt')

print("\n\tCHAT PARA DAR INFORMES A LOS POSIBLES ARRENDATARIOS\n")
def cambio_sexo():
    print("[M = Hombre | W = Mujer] \n")
    sexo = input("Opcion:   ")
    file = open(ruta_txt, "r+")
    if sexo == "W" or sexo == "w":
# Mover el puntero de escritura a la posición 10 (cuenta letras y espacios)
        file.seek(19)
# Escribir los datos en la posición actual del puntero
        file.write("a.")
# Cambiar la que me va a estar indicando para que genero va dirigido el mensaje
        file.seek(424)
        file.write("W")
    elif sexo == "M" or sexo == "m":
        file.seek(19)
        file.write("o.")
        file.seek(424)
        file.write("M")
    file.close()

def direccion():
    with open('opciones.txt', 'r') as file:
        row1 = file.readline()
        row2 = file.readline()
        row3 = file.readline()
        opcion = row1 + row2 +row3
        pyperclip.copy(opcion)
# Obtener el texto del portapapeles
    text = pyperclip.paste()
    time.sleep(2)
# Escribir el texto en la posición actual del cursor
    pyautogui.typewrite(text)

def requisitos():
    with open('opciones.txt', 'r') as file:
        file.seek(184)
        opcion = file.readline()
        pyperclip.copy(opcion)

    text = pyperclip.paste()
    time.sleep(2)
    pyautogui.typewrite(text)

def visita():
    with open('opciones.txt', 'r') as file:
        file.seek(258)
        opcion = file.readline()
        pyperclip.copy(opcion)
                
    text = pyperclip.paste()
    time.sleep(2)
    pyautogui.typewrite(text)

def numero():
    with open('opciones.txt', 'r') as file:
        file.seek(341)
        opcion = file.readline()
        pyperclip.copy(opcion)
                
    text = pyperclip.paste()
    time.sleep(2)
    pyautogui.typewrite(text)

def animales():
    with open('opciones.txt', 'r') as file:
        file.seek(384)
        opcion = file.readline()
        pyperclip.copy(opcion)
    
    text = pyperclip.paste()
    time.sleep(2)
    pyautogui.typewrite(text)

def moveto():
    print("Mandando el mensaje al posible inquilino...")
    pyautogui.moveTo(600, 1020)
    pyautogui.click()

# def bomba():
#     for i in range(3, -1, -1):
#         print(i, end='\r')
#         time.sleep(1)
#     print("\n¡Listo!")

pyautogui.moveTo(1375, 12)
pyautogui.click()
pyautogui.moveTo(1375, 55)
pyautogui.click()
pyautogui.moveTo(1370, 570)
pyautogui.click()

while True:
    with open('opciones.txt', 'r') as file:
        file.seek(424)
        genero = file.read()

    print("\n0-Cambiar de sexo -> "+"["+genero+"]"+"\n1-direccion \n2-requisitos \n3-visita \n4-numero\n5-animales\n6-EXIT")
    chose = input("Opcion:   ")
    os.system("cls" if os.name == "nt" else "clear")
    if chose == '0':
        cambio_sexo()
    elif chose == '1':
        moveto()
        direccion()
    elif chose == '2':
        moveto()
        requisitos()
    elif chose == '3':
        moveto()
        visita()
    elif chose == '4':
        moveto()
        numero()
    elif chose == '5':
        moveto()
        animales()
    elif chose == '6':
        pyautogui.moveTo(1375, 12)
        pyautogui.click()
        pyautogui.moveTo(1375, 40)
        pyautogui.click()
        break
    else: print("\nOPCION INVALIDA\n")