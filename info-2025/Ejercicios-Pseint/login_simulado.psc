Algoritmo login_simulado
		Definir  usuario, contrasenia Como Cadena
		
		Para i = 1 Hasta 3 Con Paso 1 Hacer
			Escribir "Ingrese su usuario"
			Leer usuario
			Escribir "Ingrese su contrase�a"
			Leer contrasenia
			
			// usuario -> admin  contrase�a -> 123
			Si usuario = "admin" y contrasenia = "123" Entonces
				Escribir 'Login exitoso. Bienvenido!'
				i = 3
			SiNo
				Escribir 'Usuario o contrase�a incorrectos!'
			Fin Si
		Fin Para
	
FinAlgoritmo
