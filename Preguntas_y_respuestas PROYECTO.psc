Algoritmo Preguntas_y_respuestas
	Definir R1, R2, R3, R4, R5, R6, R7, R8, R9, R10 Como Entero
	Definir P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, Respuestas_correctas, Respuestas_incorrectas Como Real
	
	Escribir "Bienvenidos al test de cultura general"
	Escribir "¿Cual es la capital de Colombia?"
	Escribir "1. Valencia."
	Escribir "2. Cali."
	Escribir "3. Bogota."
	Leer R1 
Segun R1 Hacer
	1:
		P1 <- 0
		Escribir "No es correcto, sigue intentando."
	2:
		P1 <- 0
		Escribir "No es correcto, sigue intentando."
	3:
		P1 <- 1
		Escribir "Es correcto, felicidades."
		
	De Otro Modo:
		Escribir "Esta opcion no es valida."
		
FinSegun

Escribir "¿Quien pinto la famosa obra la ultima cena?"
Escribir "1. Vincent Van Gogh."
Escribir "2. Pablo Picasso."
Escribir "3. Leonardo da Vinci."
Leer R2
Segun R2 Hacer
	1:
		P2 <- 0
		Escribir "No es correcto, sigue intentando."
	2:
		P2 <- 0
		Escribir "No es correcto, sigue intentando."
	3:
		P2 <- 1
		Escribir "Es correcto, felicidades."
		
	De Otro Modo:
		Escribir "Esta opcion no es valida."
		
FinSegun

Escribir "¿Que pais no es de Norte America?"
Escribir "1. Italia."
Escribir "2. Canada."
Escribir "3. Mexico."
Leer R3 
Segun R3 Hacer
	1:
		P3 <- 1
		Escribir "Es correcto, felicidades."
	2:
		P3 <- 0
		Escribir "No es correcto, sigue intentando."
	3:
		P3 <- 0
		Escribir "No es correcto, sigue intentando."
		
	De Otro Modo:
		Escribir "Esta opcion no es valida."
		
FinSegun

Escribir "¿Cual es el planeta mas cercano al sol?"
Escribir "1. Venus"
Escribir "2. Mercurio"
Escribir "3. Marte"
Leer R4
Segun R4 Hacer
	1:
		P4 <- 0
		Escribir "No es correcto, sigue intentando."
	2:
		P4 <- 0
		Escribir "No es correcto, sigue intentando."
	3:
		P4 <- 1
		Escribir "Es correcto, felicidades."
		
	De Otro Modo:
		Escribir "Esta opcion no es valida."
		
FinSegun

Escribir "¿Cual es la capital de Japon?"
Escribir "1. Tokio"
Escribir "2. Kioto"
Escribir "3. Osaka"
Leer R5 
Segun R5 Hacer
	1:
		P5 <- 1
		Escribir "Es correcto, felicidades."
	2:
		P5 <- 0
		Escribir "No es correcto, sigue intentando."
	3:
		P5 <- 0
		Escribir "No es correcto, sigue intentando."
		
	De Otro Modo:
		Escribir "Esta opcion no es valida."
		
FinSegun

Escribir "¿Cual es el elemento quimico con el simbolo O?"
Escribir "1. Oxigeno"
Escribir "2. Oro"
Escribir "3. Osmio"
Leer R6 
Segun R6 Hacer
	1:
		P6 <- 1
		Escribir "Es correcto, felicidades."
	2:
		P6 <- 0
		Escribir "No es correcto, sigue intentando."
	3:
		P6 <- 0
		Escribir "No es correcto, sigue intentando."
		
	De Otro Modo:
		Escribir "Esta opcion no es valida."
		
FinSegun

Escribir "¿Cual es la capital de Italia?"
Escribir "1. Roma"
Escribir "2. Madrid"
Escribir "3. Paris"
Leer R7
Segun R7 Hacer
	1:
		P7 <- 1
		Escribir "Es correcto, felicidades."
	2:
		P7 <- 0
		Escribir "No es correcto, sigue intentando."
	3:
		P7 <- 0
		Escribir "No es correcto, sigue intentando"
		
	De Otro Modo:
		Escribir "Esta opcion no es valida."
		
FinSegun

Escribir "¿Cual es el idioma mas hablado del mundo?"
Escribir "1. Ingles"
Escribir "2. Chino mandarin"
Escribir "3. Español"
Leer R8
Segun R8 Hacer
	1:
		P8 <- 0
		Escribir "No es correcto, sigue intentando."
	2:
		P8 <- 1
		Escribir "Es correcto, felicidades."
	3:
		P8 <- 0
		Escribir "No es correcto, sigue intentando."
		
	De Otro Modo:
		Escribir "Esta opcion no es valida."
		
FinSegun

Escribir "¿Cual es el lugar mas alto de la tierra?"
Escribir "1. Monte Everest"
Escribir "2. Torre Eiffel"
Escribir "3. Burj Khalifa"
Leer R9 
Segun R9 Hacer
	1:
		P9 <- 1
		Escribir "Es correcto, felicidades."
	2:
		P9 <- 0
		Escribir "No es correcto, sigue intentando."
	3:
		P9 <- 0
		Escribir "No es correcto, sigue intentando"
		
	De Otro Modo:
		Escribir "Esta opcion no es valida."
		
FinSegun

Escribir "¿Cuantos huesos tiene el cuerpo humano?"
Escribir "1. 105"
Escribir "2. 225"
Escribir "3. 206"
Leer R10 
Segun R10 Hacer
	1:
		P10 <- 0
		Escribir "No es correcto, sigue intentando."
	2:
		P10 <- 0
		Escribir "No es correcto, sigue intentando."
	3:
		P10 <- 1
		Escribir "Es correcto, felicidades."
		
	De Otro Modo:
		Escribir "Esta opcion no es valida."
		
FinSegun

Respuestas_correctas <- P1 + P2 + P3 + P4 + P5 + P6 + P7 + P8 + P9 + P10
Respuestas_incorrectas <- Respuestas_correctas - 10

Escribir "Este es tu puntaje, gracias por participar."
Escribir "Respuestas correctas: ", Respuestas_correctas
Escribir "Respuestas incorrectas: ", Respuestas_incorrectas


FinAlgoritmo
