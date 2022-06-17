"""
Credits: Webhook spammer made by andy
Discord: !ANDY!#0001
Github: AndyOnTop
"""
print("""
                                                                                                 
 _____ _           _        _ _ _     _   _____         _      _____                             
|   __|_|_____ ___| |___   | | | |___| |_|  |  |___ ___| |_   |   __|___ ___ _____ _____ ___ ___ 
|__   | |     | . | | -_|  | | | | -_| . |     | . | . | '_|  |__   | . | .'|     |     | -_|  _|
|_____|_|_|_|_|  _|_|___|  |_____|___|___|__|__|___|___|_,_|  |_____|  _|__,|_|_|_|_|_|_|___|_|  
              |_|                                                   |_|                          
                                    Made by Andy
                                  Github: AndyOnTop
""")

#imports
from dhooks import Webhook
import time

#prompts
message = input("What do you want to spam?: ")
webhookurl = Webhook(input("Enter webhook: "))
delay = int(input("Enter a delay: "))

#webhook spamming time
while True:
    time.sleep(delay)
    webhookurl.send(message)
    print("Sent.")