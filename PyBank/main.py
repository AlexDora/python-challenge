
import os 
import csv

meses = 0
Total = 0
Valor_anterior = 0
Valor_variacion = 0

Suma_de_Variaciones = 0
Promedio_Variacion = 0
Valor_presente = 0
Valor_Maximo = 0
Valor_Minimo = 0




budget_data = os.path.join('budget_data.csv')

with open(budget_data, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	
	csv_header = next(csvfile)

	print(csv_header)

	for x in csvreader:
		print(x)
		Total += int(x[1])
		
		
		if meses > 0:
			Valor_presente = (int(x[1]))
			Valor_variacion = Valor_presente - Valor_anterior
			Suma_de_Variaciones = Valor_variacion + Suma_de_Variaciones
			Valor_anterior = (int(x[1]))

			if Valor_presente > Valor_Maximo:
				Valor_Maximo = Valor_presente
				MejorMes = x
			if Valor_presente < Valor_Minimo:
				Valor_Minimo = Valor_presente
				PeorMes = x	
		else:
			Valor_anterior = (int(x[1]))






		meses += 1

Promedio_Variacion = round((Suma_de_Variaciones / (meses-1)),2)	
		

print(f'Number of months {meses}')
print(f'Total: ${Total}')
print(f'Average Change: {Promedio_Variacion}')
print(f'Greatest Increase in Profits: {MejorMes}')
print(f'Greatest Decrease in Profits: {PeorMes}')


#Ruta de exporacion de texto

output_path= os.path.join("TextExport.txt")

with open(output_path, 'w') as txtFile:
	print(f'Number of months {meses}', file = txtFile)
	print(f'Total: ${Total}', file = txtFile)
	print(f'Average Change: {Promedio_Variacion}', file = txtFile)
	print(f'Greatest Increase in Profits: {MejorMes}', file = txtFile)
	print(f'Greatest Decrease in Profits: {PeorMes}', file = txtFile)










	