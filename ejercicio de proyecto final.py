# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AmrMj8ZuhOtDNmvXbkjo7qXN28cC-I8c
"""

questions = [
    {
        "pregunta": "¿Cuál es la capital de Colombia?",
        "opciones": ["a. Valencia", "b. Cali", "c. Bogotá"],
        "respuesta_correcta": "c"
    },
    {
        "pregunta": "¿Quién pintó la famosa obra 'La Última Cena'?",
        "opciones": ["a. Vincent van Gogh", "b. Pablo Picasso", "c. Leonardo da Vinci"],
        "respuesta_correcta": "c"
    },
    {
        "pregunta": "¿Qué país no es de Norteamérica?",
        "opciones": ["a. Italia", "b. Canadá", "c. México"],
        "respuesta_correcta": "a"
    },
    {
        "pregunta": "¿Cuál es el planeta más cercano al Sol?",
        "opciones": ["a. Venus", "b. Mercurio", "c. Marte"],
        "respuesta_correcta": "b"
    },
    {
        "pregunta": "¿Cuál es la capital de Japón?",
        "opciones": ["a. Tokio", "b. Kioto", "c. Osaka"],
        "respuesta_correcta": "a"
    },
    {
        "pregunta": "¿Cuál es el elemento químico con el símbolo O?",
        "opciones": ["a. Oxígeno", "b. Oro", "c. Osmio"],
        "respuesta_correcta": "a"
    },
    {
        "pregunta": "¿Cuál es la capital de Italia?",
        "opciones": ["a. Roma", "b. Madrid", "c. París"],
        "respuesta_correcta": "a"
    },
    {
        "pregunta": "¿Cuál es el idioma más hablado del mundo?",
        "opciones": ["a. Inglés", "b. Chino mandarín", "c. Español"],
        "respuesta_correcta": "b"
    },
    {
        "pregunta": "¿Cuál es el lugar más alto de la Tierra?",
        "opciones": ["a. Monte Everest", "b. Torre Eiffel", "c. El Burj Khalifa"],
        "respuesta_correcta": "a"
    },
    {
        "pregunta": "¿Cuántos huesos tiene el cuerpo humano?",
        "opciones": ["a. 105", "b. 225", "c. 206"],
        "respuesta_correcta": "c"
    }
]
menu= True
score = 0

def triviaGame():
    global score
    for question in questions:
        print(f"\n{question['pregunta']}")
        for option in question['opciones']:
            print(option)

        answer = input("Respuesta: ").lower()

        if answer == question['respuesta_correcta']:
            score += 1
            print("¡Respuesta correcta! +1 punto")
        else:
            print(f"Respuesta incorrecta. La respuesta correcta era: {question['respuesta_correcta']}")

    print(f"\nJuego terminado. Tu puntaje final es: {score} de {len(questions)}")


while menu:
    print(f"""
        =========================
             [TRIVIA PLAY]
        =========================
        [Puntaje: {score}]

        1. Iniciar juego

        2. Instrucciones

        3. Salir
        """)

    menuSelection = input("Selecciona: ")

    match menuSelection:
        case "1":
            triviaGame()
        case "2":
            print("""
                  Objetivo del Juego:
                    Responder correctamente a la mayor cantidad de preguntas posible. Al final, el puntaje se calculará según la cantidad de respuestas correctas.

                    Cómo Jugar:
                    - Para cada pregunta, se presentarán tres opciones de respuesta (a, b o c).
                    - Escribe la letra correspondiente a la opción que crees correcta y presiona Enter.
                    - Las respuestas son insensibles a mayúsculas, por lo que puedes usar letras en minúscula o mayúscula.

                    Puntuación:
                    - Cada respuesta correcta suma un punto al puntaje final.
                    - No se penalizan las respuestas incorrectas, simplemente no suman puntos.

                    Tiempo:
                    - No hay límite de tiempo para responder cada pregunta, así que puedes pensar con calma antes de
                     responder.

                    Ganador:
                    - Al final del juego, se mostrará el puntaje final, junto con la cantidad de preguntas correctas
                     sobre el total.

                    Condiciones de Empate o Puntaje Perfecto:
                    - Si aciertas todas las respuestas, habrás logrado un puntaje perfecto. ¡Felicidades!

                    Repetición:
                    - Puedes jugar el juego las veces que desees para mejorar tu puntaje o desafiar a otros.
                """)
            input("\nPresiona Enter para volver al menú principal...")
        case "3":
            print("¡Nos vemos pronto!")
            menu = False
        case _:
            print("Por favor, selecciona una opción válida")
2