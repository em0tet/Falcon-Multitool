import random
import string
import os
import webbrowser
from colorama import init, Fore, Back, Style

os.system("cls")

yellow = Style.BRIGHT+Fore.YELLOW
green = Style.BRIGHT+Fore.GREEN
cyan = Style.BRIGHT+Fore.CYAN
red = Style.BRIGHT+Fore.RED

print(red+"""
██████╗░██╗░██████╗░█████╗░░█████╗░██████╗░██████╗░  ████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗
██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║
██║░░██║██║╚█████╗░██║░░╚═╝██║░░██║██████╔╝██║░░██║  ░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║
██║░░██║██║░╚═══██╗██║░░██╗██║░░██║██╔══██╗██║░░██║  ░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║
██████╔╝██║██████╔╝╚█████╔╝╚█████╔╝██║░░██║██████╔╝  ░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║
╚═════╝░╚═╝╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░  ░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝

░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░ coded by rexurs
██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗ 
██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝ 
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗ 
╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝\n\n""")

root = os.path.dirname(os.path.abspath(__file__))
tokens = os.path.join(root, "tokens.txt")

quantity = int(input(yellow+"How many tokens: "))

for i in range(quantity):

	def random_char(y):
		return ''.join(random.choice(string.ascii_letters) for x in range(y))

	token = "NzQzMD"+random_char(18)+"."+"XzP"+random_char(3)+"."+random_char(27)

	with open(tokens,"a") as work:
		work.write(token+"\n")

	print(green+token)

print(yellow+"\nGenerated and saved to tokens.txt!")