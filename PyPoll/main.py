import csv
import os
import random

Total_of_Votes = 0
candidates=["Khan","Correy","Li","O'Tooley"]
candidate1_Total=0
candidate2_Total=0
candidate3_Total=0
candidate4_Total=0
Valor_presente=0
Winner=0


election_data = os.path.join('election_data.csv')

with open(election_data, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')

	for x in csvreader:
		Total_of_Votes += 1
		
		if candidates[0] == x[2]:
			candidate1_Total += 1
		elif candidates[1]==x[2]:
			candidate2_Total+=1
		elif candidates[2]==x[2]:
			candidate3_Total+=1
		elif candidates[3]==x[2]:
			candidate4_Total+=1

	Per_can1= ((candidate1_Total/Total_of_Votes) * 100)
	Per_can2= ((candidate2_Total/Total_of_Votes) * 100)
	Per_can3= ((candidate3_Total/Total_of_Votes) * 100)
	Per_can4= ((candidate4_Total/Total_of_Votes) * 100)

	candidates2 = [candidate1_Total, candidate2_Total, candidate3_Total, candidate4_Total]




	Ganador={"Khan": candidate1_Total, "Correy": candidate2_Total, "Li": candidate3_Total, "O'Tooley":candidate4_Total}	
	
	maxvotes = max(Ganador.values())
	winner2 = [key for key, value in Ganador.items() if value == maxvotes][0]


print(f'Total of Votes: {Total_of_Votes}')
print(f'Candidate1: {candidates[0]} ({round(Per_can1,1)}%) {candidate1_Total}')
print(f'Candidate2: {candidates[1]} ({round(Per_can2,1)}%) {candidate2_Total}')
print(f'Candidate3: {candidates[2]} ({round(Per_can3,1)}%) {candidate3_Total}')
print(f'Candidate4: {candidates[3]} ({round(Per_can4,1)}%) {candidate4_Total}')
print(f'Winner: {winner2}')




output_path= os.path.join("TextExport.txt")

with open(output_path, 'w') as txtFile:
	print(f'Total of Votes: {Total_of_Votes}', file = txtFile)
	print(f'Candidate: {candidates[0]} ({round(Per_can1,1)}%) {candidate1_Total}', file = txtFile)
	print(f'Candidate: {candidates[1]} ({round(Per_can2,1)}%) {candidate2_Total}', file = txtFile)
	print(f'Candidate: {candidates[2]} ({round(Per_can3,1)}%) {candidate3_Total}', file = txtFile)
	print(f'Candidate: {candidates[3]} ({round(Per_can4,1)}%) {candidate4_Total}', file = txtFile)
	print(f'Winner: {winner2}', file = txtFile)
