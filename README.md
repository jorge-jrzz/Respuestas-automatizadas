# **Bot para respuestas programadas**

Este es un chat bot que se realizó con python para automatizar de cierta forma las conversaciones con personas interesadas en rentar un inmueble habitacional en la CDMX.

## Desarrollo

El proyecto esta específicamente desarrollado para una MacBook Air M1, y con la aplicación de escritorio de Messenger,  ya que con ayuda de [PyAutoGUI](https://pypi.org/project/PyAutoGUI/) se interactúa con específicos pixeles de la pantalla. Otra biblioteca importante que se ocupa en el programa es la de [pyperclip](https://pypi.org/project/pyperclip/) para su utilidad de comprar cierto texto al portapapeles de la computadora. 

```bash
pip install PyAutoGUI
pip install pyperclip
```

## Demo

Antes de ejecutar el programa, primero se tiene que tener la aplicación de Messenger abierta, al momento de ejecutar el programa, lo primero que se realiza automaticamente es cambiar la fuente de entrada a la distribución Americana, esto se hace para que se respeten los caracteres especiales que se lleguen a encontrar en cualquiera de las respuestas.

![first.gif](/README_media/first.gif)

Después en pantalla se muestra el menú  con  las opciones de los temas que más preguntan las personas interesadas:

![menu](/README_media/menu.png)

En cada una de las opciones (1-5) se lee una parte especifica del archivo de texto “opciones.txt” el cual contiene las respuestas completas, después con ayuda de PyAutoGUI se posiciona automaticamente en barra de dialogo del chat al que se quiere contestar (Previamente abierto y seleccionado); 

Por ejemplo la opción 1, manda el mensaje con la dirección incluyendo el link de google maps:

![direccion](/README_media/direccion.gif)

En la opción 0 lee el último carácter de archivo “opciones.txt” el cual indica a qué sexo van dirigidos los mensajes (si a un hombre o a una mujer) y nos permite cambiar esto dependiendo ellas necesidades actuales. 

![opcion_0.gif](/README_media/opcion_0.gif)

Finalmente, cuando escojamos la opción 6 (EXIT), regresara la fuente de entrada a la distribución Latino Americana.

## Autor

[Jorge Juarez](https://github.com/jorge-jrzz)

## **Estatus**

Este proyecto se realizó para agilizar la respuesta a los mensajes de las personas interesadas en rentar un departamento, el código no presentará actualizaciones mientras el departamento no esté siendo rentado. 

## **Licencia**

[MIT](https://choosealicense.com/licenses/mit/)