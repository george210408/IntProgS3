Algoritmo calcularimpuesto
	// calcular el impuesto añadido
	Definir precio, porc_impuesto, valor_imp, total_pago Como Real
	Escribir 'dime el precio del producto en dolares: '
	Leer precio
	Escribir "dime el porcentaje del producto con impuesto: "
	Leer porc_impuesto
	porc_impuesto = porc_impuesto / 100
	Escribir "nuevo impuesto", porc_impuesto
	valor_imp = precio * porc_impuesto
	total_pago = precio + valor_imp
	Escribir "total de precio sin impuesto: " precio
	Escribir "impuesto a aplicar: ", porc_impuesto
	Escribir "valor del impuesto a aplicar: " valor_imp
	Escribir "precio final con impuesto: ", total_pago
FinAlgoritmo
