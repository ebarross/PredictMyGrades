# encoding:utf-8

# Documentação: http://pybrain.org/docs/index.html

from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer
from datetime import datetime
from pybrain.tools.shortcuts import buildNetwork
import pickle

#['STUDENTID', 'SCORE', 'GRADE', 'ASKS_QUESTIONS', 'LEAVES_EARLY', 'PARTICIPATION']

tamanho_entrada = 4

dataset = SupervisedDataSet(tamanho_entrada, 1)

tf = open('M2017_train.csv', 'r')

st_grade = {}
lines = tf.readlines()


def testing_cases():
	resultado = open('resultado.txt','r')
	net = pickle.load(resultado)
	
	cases = open('M2017_test_students.csv', 'r')
	lines = cases.readlines()
	
	for i in range(1, len(lines)):
		data = [x for x in lines[i].strip().split(',') if x != '']
		
		studentId = data[0]
		score = float(data[1])
		ask_questions = data[2]
		leaves_early = data[3]
		participation = float(data[4])
		
		resultados_teste = open("resultado_teste.txt", "a")
		
		
		saida = ""
		
		
		saida += "==================\n"

		saida += "ID do aluno: " + str(studentId) + "\n"
		saida +=  "Score: " + str(score) + "\n"
		saida += "Frequencia com que o aluno faz perguntas: " + ask_questions + "\n"
		saida += "Frequencia com que o aluno sai da aula cedo: " + leaves_early + "\n"
		saida += "Participacao do aluno: " +  str(participation) + "\n"
		
		if ask_questions == 'always':
			ask_questions = 0.9
		elif ask_questions == 'sometimes':
			ask_questions = 0.4
		elif ask_questions == 'never':
			ask_questions = 0.1
			
		if leaves_early == 'never':
			leaves_early = 0.9
		elif leaves_early == 'rarely':
			leaves_early = 0.4
		elif leaves_early == 'always':
			leaves_early = 0.1
		
		myGrade = float(net.activate((score, ask_questions, leaves_early, participation))[0])
		
		
		if(myGrade <= 0.2):
			myGrade = 'F'
		elif(myGrade <= 0.4):
			myGrade = 'D'
		elif(myGrade <= 0.6):
			myGrade = 'C'
		elif(myGrade <= 0.8):
			myGrade = 'B'
		else:
			myGrade = 'A'
		
		

		saida += "Previsao de nota do aluno: " + myGrade + "\n"
		
		resultados_teste.write(saida)


testing_cases()

'''	
for i in range(1, len(lines)):
	data = [x for x in lines[i].strip().split(',') if x != '']
	
	grade = data[2]
	studentId = data[0]
	
	st_grade[data[0]] = grade
	
	
	if(i <= 588):
		score = float(data[1])
		ask_questions = data[3]
		leaves_early = data[4]
		participation = float(data[5])
	
	
		if grade == 'A':
			grade = 1
		elif grade == 'B':
			grade = 0.8
		elif grade == 'C':
			grade = 0.6
		elif grade == 'D':
			grade = 0.4
		elif grade == 'F':
			grade = 0.2
		
		if ask_questions == 'always':
			ask_questions = 0.9
		elif ask_questions == 'sometimes':
			ask_questions = 0.4
		elif ask_questions == 'never':
			ask_questions = 0.1
		
		
		if leaves_early == 'never':
			leaves_early = 0.9
		elif leaves_early == 'rarely':
			leaves_early = 0.4
		elif leaves_early == 'always':
			leaves_early = 0.1
		
		myset = (score, ask_questions, leaves_early, participation)
		dataset.addSample(myset, grade)
	
	
nn = buildNetwork(4, 4, 1, bias=True)
momentum = 0.2
lrdecay =1.0
learning_rate = 0.01

trainer = BackpropTrainer(nn, dataset, learning_rate, lrdecay, momentum)

for i in xrange(3000):
	print (trainer.train())


resultado = open('resultado.txt', 'w')
pickle.dump(nn, resultado)

resultado.close()


'''


'''
line_index = 0
total = 0
acertos = 0


for i in range(589, 840):
	testData = [x for x in lines[i].strip().split(',') if x != '']
	
	total += 1
	
	studentId = testData[0]
	score = float(testData[1])
	ask_questions = testData[3]
	leaves_early = testData[4]
	participation = float(testData[5])
	
	if ask_questions == 'always':
		ask_questions = 0.9
	elif ask_questions == 'sometimes':
		ask_questions = 0.4
	elif ask_questions == 'never':
		ask_questions = 0.1
		
	if leaves_early == 'never':
		leaves_early = 0.9
	elif leaves_early == 'rarely':
		leaves_early = 0.4
	elif leaves_early == 'always':
		leaves_early = 0.1
	
	myGrade = float(nn.activate((score, ask_questions, leaves_early, participation))[0])
	
	if(myGrade <= 0.2):
		myGrade = 'F'
	elif(myGrade <= 0.4):
		myGrade = 'D'
	elif(myGrade <= 0.6):
		myGrade = 'C'
	elif(myGrade <= 0.8):
		myGrade = 'B'
	else:
		myGrade = 'A'
	
	if(st_grade[studentId] == myGrade):
		acertos += 1
			
	line_index += 1


perc_acertos = (acertos * 100.0) / total


print("Porcentagem de Acertos: ", perc_acertos)
'''

