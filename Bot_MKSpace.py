import telepot
import time
import string
import re
from pprint import pprint

Statomacchina = 0


def operazione(a,b,op):

	if op == 1:
		try:
			a1 = int(a.split()[0])
			b1 = int(b.split()[0])
			c = a1 + b1
			risposta = ("L addizione tra i due numeri e: %s" % c)

		except ValueError:
			risposta = ("Sei un cretino! che razza di numeri sarebbero questi?!")
	elif op == 2:
		try:
			a1 = int(a.split()[0])
			b1 = int(b.split()[0])
			c = a1 - b1
			risposta = ("L addizione tra i due numeri e: %s" % c)

		except ValueError:
			risposta = ("Sei un cretino! che razza di numeri sarebbero questi?!")
	elif op == 3:
		try:
			a1 = int(a.split()[0])
			b1 = int(b.split()[0])
			c = a1 * b1
			risposta = ("L addizione tra i due numeri e: %s" % c)

		except ValueError:
			risposta = ("Sei un cretino! che razza di numeri sarebbero questi?!")
	elif op == 4:
		try:
			a1 = float(a.split()[0])
			b1 = float(b.split()[0])
			c = a1 / b1
			risposta = ("L addizione tra i due numeri e: %s" % c)

		except ValueError:
			risposta = ("Sei un cretino! che razza di numeri sarebbero questi?!")
	return risposta

def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)

	global Statomacchina
	ver1 = 0


	chat_id = msg['chat']['id']
	command_input = msg['text']

	print(chat_id, content_type, chat_type)

	response = bot.getUpdates()
	print "msg:"
	pprint(msg)
	if Statomacchina == 0:
		if command_input == '/risolvi' or command_input == '/risolvi@CompitatorBot':
			risolvi_str = "Illustrami l'operazione che vorresti risolvere "
			bot.sendMessage(chat_id, risolvi_str)
			Statomacchina = 1
		else:
			bot.sendMessage(chat_id, "Non mi conosci, puoi chiedermi soltanto /risolvi")

	elif Statomacchina == 1:

		#addizione
		check = command_input.find('+')
		if check == -1 :
				ver1 = -1
		else :
				ver1 = 1
				a, b = command_input.split('+')
				risposta=operazione(a,b,ver1)


		#sottrazione
		check = command_input.find('-')
		if check == -1:
				ver1 = -1

		else :
				ver1 = 2
				a, b = command_input.split('+')
				risposta=operazione(a,b,ver1)

		#moltiplicazione
		check = command_input.find('*')
		if check == -1:
				ver1 = -1

		else :
				ver1 = 3
				a, b = command_input.split('+')
				risposta=operazione(a,b,ver1)
		#divisione
		check = command_input.find('/')
		if check == -1:
				ver1 = -1

		else :
				ver1 = 4
				a, b = command_input.split('+')
				risposta=operazione(a,b,ver1)



		if ver1 == -1:
			risposta= "ti ho chiesto di propormi un' operazione scemo"


		Statomacchina = 0
		bot.sendMessage(chat_id, risposta)


bot = telepot.Bot('token')

bot.message_loop(handle)

print("ASCOLTO LA VOSTRA VOCE")

while 1:
	time.sleep(10)
