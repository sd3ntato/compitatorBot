import telepot
import time
import string
import re
from pprint import pprint

Statomacchina = 0
ver1 = 0

def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)

	global Statomacchina
	global ver1
	

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
		check = string.find(command_input, '+')
		if check == -1 :
				ver1 = 1
		else :
				a, b = command_input.split('+')

				try:
					a1 = int(a.split()[0])
                    			b1 = int(b.split()[0])
					c = a1 + b1
					risposta = ("L addizione tra i due numeri e: %s" % c)

				except ValueError:
					risposta = ("Sei un cretino! che razza di numeri sarebbero questi?!")

		#sottrazione
		check =string.find(command_input, '-')
		if check == -1:
				ver1 = 1

		else :
				a, b = command_input.split('-')

				try:
					a1 = int(a.split()[0])
                   			b1 = int(b.split()[0])
					c = a1 - b1
					risposta = ("La sottrzione tra i due numeri e: %s" % c)

				except ValueError:
					risposta = ("Sei un cretino! che razza di numeri sarebbero questi?!")
		#moltiplicazione
		check =string.find(command_input, '*')
		if check == -1:
				ver1 = 1

		else :
				a, b = command_input.split('*')

				try:
					a1 = int(a.split()[0])
                   			b1 = int(b.split()[0])
					c = a1 * b1
					risposta = ("il prodotto tra i due numeri e: %s" % c)

				except ValueError:
					risposta = ("Sei un cretino! che razza di numeri sarebbero questi?!")
		#divisione
		check =string.find(command_input, '/')
		if check == -1:
				ver1 = 1

		else :
				a, b = command_input.split('/')

				try:
					a1 = float(a.split()[0])
                   			b1 = float(b.split()[0])
					c = a1 / b1
					risposta = ("il rapporto tra i due numeri e: %s" % c)

				except ValueError:
					risposta = ("Sei un cretino! che razza di numeri sarebbero questi?!")




		if ver1 == 0:
			risposta= "ti ho chiesto di propormi un' operazione scemo"
			

		Statomacchina = 0
		bot.sendMessage(chat_id, risposta)


bot = telepot.Bot('309693128:AAH4TGkBXegyVLykKklS9P44emEgv56K9BM')

bot.message_loop(handle)

print("ASCOLTO LA VOSTRA VOCE")

while 1:
	time.sleep(10)
