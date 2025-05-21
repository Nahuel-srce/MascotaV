Algoritmo calculadoraSimple
	
	definir numero1, numero2, resultado Como real
	definir operacion Como Caracter
	
	Escribir "Ingresa los valores pára una operacón simple:"
	Leer numero1
	leer numero2
	
	escribir "Ingresa el símbolo de la operación a realizar (+,-,/,*)"
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
					Escribir "Ingrese una operación válida"
				FinSi
			FinSi
		FinSi
		
	FinSi
FinAlgoritmo