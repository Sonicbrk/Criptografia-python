import os

def criptografar():
	alfabeto='abcdefghijklmnopqrstuvwxyzàáãâéêẽèóòôõìîĩíúùûũç!?*#$%&*+=-_/@'
	tamAlfa = len(alfabeto)
	chave= int(input('Digite a sua chave - Digite a sua Chave - valor entre 1 e {0}: '.format (tamAlfa)))
	frase = input('Digite a frase que sera criptografada: ')
	frase = frase.lower()
	txtconvert =''
	txtsaida=''
	for c in frase:
		if c in alfabeto:
			indice=alfabeto.find(c)
			indice=indice+chave
			if indice>=len(alfabeto):
				indice= indice-len(alfabeto)
			txtsaida += alfabeto[indice]
		else:
			txtsaida += c
	print (txtsaida)
def decriptografar():
	alfabeto='abcdefghijklmnopqrstuvwxyzàáãâéêẽèóòôõìîĩíúùûũç!?*#$%&*+=-_/@'
	tamAlfa = len(alfabeto)
	chave= int(input('Digite a sua chave - Digite a sua Chave - valor entre 1 e {0}: '.format (tamAlfa)))
	frase = input('Digite a frase que sera decriptografada: ')
	frase = frase.lower()
	txtconvert = ''
	txtsaida=''
	for c in frase:
		if c in alfabeto:
			indice= alfabeto.find(c)
			indice=indice-chave
			if indice<0:
				indice=indice+len(alfabeto)
			txtsaida += alfabeto[indice]
		else:
			txtsaida += c
	print (txtsaida)
			
escolha = ''
while (escolha!=0):
	os.system('cls')
	print('        CRIPTOGRAFIA EM CESAR \n\n')
	print('Escolha uma opçao abaixo!\n')
	print('1 - CRIPTOGRAFAR')
	print('2 - DECRIPTOGRAFAR')
	print('0 - SAIR \n')
	escolha = int(input())
	if escolha < 0 or escolha > 2:
		os.system('cls')
		print('OPCAO INVALIDA!!!!!')
		input()
	elif escolha == 1:
		os.system('cls')
		criptografar()
		input()
	elif escolha == 2:
		os.system('cls')
		decriptografar()
		input()
	elif escolha == 0:
		os.system('cls')
		print ('encerrando...')
		input()
	
