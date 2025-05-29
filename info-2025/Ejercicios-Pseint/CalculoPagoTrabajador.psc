Algoritmo CalculoPagoTrabajador
	Definir sueldo, horasExtras, categoria, pagoHorasExtras, totalPagar Como Real
	Escribir 'Ingrese el sueldo base del trabajador:'
	Leer sueldo
	Escribir 'Ingrese la cantidad de horas extras trabajadas:'
	Leer horasExtras
	Escribir 'Ingrese la categoría del trabajador (1 o 2):'
	Leer categoria
	Si horasExtras>30 Entonces
		horasExtras <- 30
	FinSi
	Según categoria Hacer
		1:
			pagoHorasExtras <- horasExtras*9000
		2:
			pagoHorasExtras <- horasExtras*10000
		De Otro Modo:
			Escribir 'Categoría inválida. Debe ser 1 o 2.'
	FinSegún
	totalPagar <- sueldo+pagoHorasExtras
	Escribir 'El total a pagar al trabajador es: $', totalPagar
FinAlgoritmo
