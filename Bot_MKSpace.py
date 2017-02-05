import telepot
import time
import string
import re
from pprint import pprint

Statomacchina = 0

def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	
	global Statomacchina

	chat_id = msg['chat']['id']
	command_input = msg['text']
	
	print(chat_id, content_type, chat_type)
	
	if Statomacchina == 0:
		if command_input == '/risolvi' or command_input == '/risolvi@CompitatorBot':
			risolvi_str = "Illustrami l'addizione che vorresti risolvere"
			bot.sendMessage(chat_id, risolvi_str)
			Statomacchina = 1
		else:
			bot.sendMessage(chat_id, "Non mi conosci, puoi chiedermi soltanto /risolvi")
		
	elif Statomacchina == 1:
		check = string.find(command_input, '+')
		if check == -1:
			risposta = "Stai cercando di fregarmi, maledetto!"
		else:
			a, b = command_input.split('+')
			a1 = int(a.split()[0])
			b1 = int(b.split()[0])
			#if a1.isdigit() and  b1.isdigit():
			a1 = int(a1)
			b1 = int(b1)
			c = a1 + b1
			risposta = ("L addizione tra i due numeri e: %s" % c)
			#else:
				#risposta = ("Sei un cretino! %s %s" %a1  %b1) 
		Statomacchina = 0
		bot.sendMessage(chat_id, risposta)
		
		
bot = telepot.Bot('309693128:AAH4TGkBXegyVLykKklS9P44emEgv56K9BM')

bot.message_loop(handle)

print("ASCOLTO LA VOSTRA VOCE")

while 1:
	time.sleep(10)
