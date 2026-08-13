""""
El objetivo es crear un juego simple en la consola donde la computadora elige un número secreto y el usuario tiene que adivinarlo. El programa dará pistas para ayudar al usuario a encontrar el número.

Este ejercicio es ideal para practicar bucles, condicionales, entrada de usuario y el uso de módulos.

📋 Instructivo: Pasos a seguir
Generar el número secreto:

El programa debe elegir un número entero al azar entre 1 y 50.

Bucle del juego:

El programa debe pedir al usuario que ingrese un número para adivinar.

Este proceso debe repetirse hasta que el usuario adivine el número correcto.

Dar pistas:

Si el número del usuario es mayor que el número secreto, el programa debe imprimir un mensaje como "¡Demasiado alto! Intenta de nuevo.".

Si el número del usuario es menor que el número secreto, debe imprimir "¡Demasiado bajo! Intenta de nuevo.".

Fin del juego:

Cuando el usuario adivine el número correctamente, el programa debe imprimir un mensaje de felicitación (ej: "¡Correcto! ¡Has adivinado el número!") y terminar.

💡 Pistas y Consejos
Pista 1: Para generar un número al azar, primero debes importar el módulo random al inicio de tu archivo. Después, la función random.randint(1, 50) te dará un número aleatorio en ese rango.

Pista 2: Recuerda que la función input() siempre devuelve el texto que el usuario escribe. Para poder compararlo con el número secreto, necesitarás convertir la entrada del usuario a un número entero usando la función int().

Pista 3: Un bucle while es perfecto para este juego. Puedes hacer que el bucle se repita mientras la suposición del usuario sea diferente al número secreto.
"""
from random import randint

numero_secreto = randint(1,50)
intentos = 0


print("¡Bienvenido al juego de adivinar el número!")
print("He elegido un número entre 1 y 50. ¿Puedes adivinar cuál es?")   

while True:
    try:

        # Pedir al usuario que ingrese un número
        guess = int(input("\n¿Cuál crees que es el número? "))
        intentos += 1
        
        # Verificar si adivinó
        if guess == numero_secreto:
            print(f"🎉 ¡Correcto! ¡Has adivinado el número {numero_secreto} en {intentos} intentos!")
            break
        
        # Dar pistas
        elif guess > numero_secreto:
            print("¡Demasiado alto! Intenta con un número más bajo.")
        else:
            print(" ¡Demasiado bajo! Intenta con un número más alto.")
            
    except ValueError:
        print("Por favor, ingresa solo números enteros.")

print("\n¡Gracias por jugar! ")        
 