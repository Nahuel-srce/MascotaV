Algoritmo calculadoraSimple
	
	definir numero1, numero2, resultado Como real
	definir operacion Como Caracter
	
	Escribir "Ingresa los valores p�ra una operac�n simple:"
	Leer numero1
	leer numero2
	
	escribir "Ingresa el s�mbolo de la operaci�n a realizar (+,-,/,*)"
	leer operacion 
	
	si operacion = "+" Entonces
		resultado = numero1 + numero2 		
		
		Escribir  "Resultado:" " " 	resultado
	SiNo
		
		si  operacion = "-" entonces
			
			resultado = numero1 - numero2
			
			Escribir "Resultado:" " " resultado
		SiNo
			si operacion = "*"  Entonces
				resultado = numero1 * numero2
				Escribir "Resultado:" " " resultado
				
			sino 
				si operacion = "/" 
					si numero2 <> 0 Entonces
						resultado = numero1 / numero2
						
						Escribir  "Resultado" " " resultado
					SiNo
						Escribir "SINTAXIS ERROR - (no es posible dividir por 0)"
				        
					FinSi
				siNo
					escribir "SINTAXIS ERROR"  " " operacion " " "no es un carcter valido"
					Escribir "Ingrese una operaci�n v�lida"
				FinSi
			FinSi
		FinSi
		
	FinSi
FinAlgoritmo