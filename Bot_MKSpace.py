import telepot
import time
import string
import re
from pprint import pprint



def operazione(a,b,op):
	try:
		if op == 1:
				risposta = ("L addizione tra i due numeri e: %s" % (int(a.split()[0]) + int(b.split()[0])))
		elif op == 2:
				risposta = ("L addizione tra i due numeri e: %s" % (int(a.split()[0]) - int(b.split()[0])))
		elif op == 3:
				risposta = ("L addizione tra i due numeri e: %s" % (int(a.split()[0]) * int(b.split()[0])))
		elif op == 4:
				risposta = ("L addizione tra i due numeri e: %s" % (int(a.split()[0]) / int(b.split()[0])))

	except ValueError:
			risposta = ("Sei un cretino! che razza di numeri sarebbero questi?!")
	return risposta

Statomacchina = 0
def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	global Statomacchina
	ver1 = 0
	chat_id = msg['chat']['id']
	command_input = msg['text']
	print(chat_id, content_type, chat_type)
	print "msg:"
	pprint(msg)
	if Statomacchina == 0:
		if command_input == '/risolvi' or command_input == '/risolvi@CompitatorBot':
			 
			Statomacchina = 1
			risolvi_str = "Illustrami l'operazione che vorresti risolvere" 
			bot.sendMessage(chat_id, risolvi_str)
			
		else:
			bot.sendMessage(chat_id, "Non mi conosci, puoi chiedermi soltanto /risolvi")
	
	elif Statomacchina == 1:

		#addizione
		if command_input.find('+') != -1 :
				a, b = command_input.split('+')
				risposta=operazione(a,b,1)
				ver1 = 1

		#sottrazione
		if command_input.find('-') != -1 :
				a, b = command_input.split('-')
				risposta=operazione(a,b,2)
				ver1 = 1

		#moltiplicazione
		if command_input.find('*') != -1 :
				a, b = command_input.split('*')
				risposta=operazione(a,b,3)
				ver1 = 1
		#divisione
		if command_input.find('/') != -1 :
				a, b = command_input.split('/')
				risposta=operazione(a,b,4)
				ver1 = 1



		if ver1 == 0:
			risposta= "ti ho chiesto di propormi un' operazione scemo"


		Statomacchina = 0
		bot.sendMessage(chat_id, risposta)


bot = telepot.Bot('487365523:AAGyY9FrLZK_Mo42MQwTCMgzd_L6KVit0bI')

bot.message_loop(handle)

print("ASCOLTO LA VOSTRA VOCE")

while 1:
	time.sleep(10)
