import time, json, os
from colorama import Fore
from colorama import Style, Fore
import ctypes
import datetime, time, json, threading, random, httpx, sys, binascii, subprocess, fade
from pathlib import Path
import requests
import hashlib
import platform
import json as jsond
if os.name == 'nt':
    import ctypes
from uuid import uuid4
from colorama import Fore
def cls():
    os.system('cls' if os.name =='nt' else 'clear')
if os.name == "nt":
    ctypes.windll.kernel32.SetConsoleTitleW(f".gg/ezboosts")
else:
    pass
config = json.load(open("config.json", encoding="utf-8"))

def getinviteCode(invite_input):
    if "discord.gg" not in invite_input:
        return invite_input
    if "discord.gg" in invite_input:
        invite = invite_input.split("discord.gg/")[1]
        return invite
    if "https://discord.gg" in invite_input:
        invite = invite_input.split("https://discord.gg/")[1]
        return invite
    if "invite" in invite_input:
        invite = invite_input.split("/invite/")[1]
        return invite
        
config = json.load(open("config.json", encoding="utf-8"))
fingerprints = json.load(open("assets/print.json", encoding="utf-8"))
client_identifiers = ['safari_ios_16_0', 'safari_ios_15_6', 'safari_ios_15_5', 'safari_16_0', 'safari_15_6_1', 'safari_15_3', 'opera_90', 'opera_89', 'firefox_104', 'firefox_102']

def success(msg: str):
    print(f"{timestamp()} \x1b[38;5;120mINF\x1b[0m \x1b[38;5;239m>\x1b[0m {msg}{Fore.RESET}{Style.RESET_ALL}")

def error(msg: str):
    print(f"{timestamp()} \033[1m\x1b[38;5;203mWRN\x1b[0m\033[0m \x1b[38;5;239m>\x1b[0m {msg}{Fore.RESET}{Style.RESET_ALL}")

def warn(msg: str):
    print(f"{timestamp()} \x1b[38;5;203mWRN\x1b[0m \x1b[38;5;239m>\x1b[0m {msg}{Fore.RESET}{Style.RESET_ALL}")

def getinviteCode(invite_input):
    if "discord.gg" not in invite_input:
        return invite_input
    if "discord.gg" in invite_input:
        invite = invite_input.split("discord.gg/")[1]
        return invite
    if "https://discord.gg" in invite_input:
        invite = invite_input.split("https://discord.gg/")[1]
        return invite
    if "invite" in invite_input:
        invite = invite_input.split("/invite/")[1]
        return invite

def menu():
    print(fade.purplepink("""      
     

██████╗  ██████╗  ██████╗ ███████╗████████╗██╗███╗   ██╗ ██████╗ 
╝██╔══██╗██╔═══██╗██╔═══██╗██╔════╝╚══██╔══╝██║████╗  ██║██╔════╝ 
██████╔╝██║   ██║██║   ██║███████╗   ██║   ██║██╔██╗ ██║██║  ███╗
██╔══██╗██║   ██║██║   ██║╚════██║   ██║   ██║██║╚██╗██║██║   ██║
██████╔╝╚██████╔╝╚██████╔╝███████║   ██║   ██║██║ ╚████║╚██████╔╝
╚══════╝╚══════╝╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                                 
                                                                                                          
                                   [1] Boost                            
                                   [2] View Stock
                                  
                                                
                                                                                                                                              
"""))
    
    choice = input(f"{Fore.WHITE}> ")
    if choice == "1":
        invite = getinviteCode(input(f"{Fore.WHITE}> {Fore.LIGHTBLACK_EX}Invite Link/Code (Example: discord.gg/):{Fore.RESET} "))
        amount = input(f"{Fore.WHITE}> {Fore.LIGHTBLACK_EX}How Many Boosts:{Fore.RESET} ")
        while amount.isdigit() != True:
            error("Amount cannot be a string.")
            amount = input(f"{Fore.WHITE}> {Fore.LIGHTBLACK_EX}How Many Boosts:{Fore.RESET} ")
        months = input(f"{Fore.WHITE}> {Fore.LIGHTBLACK_EX}How Many Months:{Fore.RESET} ")
        while amount.isdigit() != True:
            error("Months must be a string")
            months = input(f"{Fore.WHITE}> {Fore.LIGHTBLACK_EX}How Many Months:{Fore.RESET} ")
        start = time.time()
        boosted = tboost(invite, int(amount), int(months), config['nickname'])
        end = time.time()
        print()
        success(f"Successfully boosted https://discord.gg/{invite} {Fore.LIGHTBLACK_EX}duration={Fore.WHITE}{round(end - start, 2)}s {Fore.LIGHTBLACK_EX}success={Fore.WHITE}{len(variables.success_tokens)} {Fore.LIGHTBLACK_EX}failed={Fore.WHITE}{len(variables.failed_tokens)}")
        time.sleep(3)
        os.system('cls')
        menu()
        
    if choice == "2":
        print(f'{Fore.LIGHTBLACK_EX}1 Month Nitro Tokens: {len(open("assets/1m_tokens.txt", "r").readlines())}{Fore.RESET}')
        print(f'{Fore.LIGHTBLACK_EX}1 Month Boosts: {len(open("assets/1m_tokens.txt", "r").readlines())*2}{Fore.RESET}')
        print()
        print(f'{Fore.LIGHTBLACK_EX}3 Month Nitro Tokens: {len(open("assets/3m_tokens.txt", "r").readlines())}{Fore.RESET}')
        print(f'{Fore.LIGHTBLACK_EX}3 Month Boosts: {len(open("assets/3m_tokens.txt", "r").readlines())*2}{Fore.RESET}')
        print()
        time.sleep(3)
        os.system('cls')
        menu()
        
class variables:
    joins = 0; boosts_done = 0; success_tokens = []; failed_tokens = []

def timestamp():
    timestamp = f"{Fore.RESET}{Fore.LIGHTBLACK_EX}{datetime.datetime.now().strftime('%H:%M:%S')}{Fore.RESET}"
    return timestamp

def checkEmpty(filename):
    mypath = Path(filename)
 
    if mypath.stat().st_size == 0:
        return True
    else:
        return False
     
def validateInvite(invite:str):
    client = httpx.Client()
    if 'type' in client.get(f'https://discord.com/api/v10/invites/{invite}?inputValue={invite}&with_counts=true&with_expiration=true').text:
        return True
    else:
        return False 
        
def get_all_tokens(filename:str):
    all_tokens = []
    for j in open(filename, "r").read().splitlines():
        if ":" in j:
            j = j.split(":")[2]
            all_tokens.append(j)
        else:
            all_tokens.append(j)
 
    return all_tokens

def remove(token: str, filename:str):
    tokens = get_all_tokens(filename)
    tokens.pop(tokens.index(token))
    f = open(filename, "w")
    
    for l in tokens:
        f.write(f"{l}\n")
        
    f.close()
              
def getproxy():
    try:
        proxy = random.choice(open("assets/proxies.txt", "r").read().splitlines())
        return {'http': f'http://{proxy}'}
    except Exception as e:
        pass
    
def get_fingerprint(thread):
    try:
        fingerprint = httpx.get(f"https://discord.com/api/v10/experiments", proxies =  {'http://': f'http://{random.choice(open("assets/proxies.txt", "r").read().splitlines())}', 'https://': f'http://{random.choice(open("assets/proxies.txt", "r").read().splitlines())}'} if config['proxyless'] != True else None)
        return fingerprint.json()['fingerprint']
    except Exception as e:
        get_fingerprint(thread)

def get_cookies(x, useragent, thread):
    try:
        response = httpx.get('https://discord.com/api/v10/experiments', headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-type': 'application/json','origin': 'https://discord.com','referer':'https://discord.com','sec-ch-ua': f'"Google Chrome";v="108", "Chromium";v="108", "Not=A?Brand";v="8"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': useragent, 'x-debug-options': 'bugReporterEnabled','x-discord-locale': 'en-US','x-super-properties': x}, proxies = {'http://': f'http://{random.choice(open("assets/proxies.txt", "r").read().splitlines())}', 'https://': f'http://{random.choice(open("assets/proxies.txt", "r").read().splitlines())}'} if config['proxyless'] != True else None)
        cookie = f"locale=en; __dcfduid={response.cookies.get('__dcfduid')}; __sdcfduid={response.cookies.get('__sdcfduid')}; __cfruid={response.cookies.get('__cfruid')}"
        return cookie
    except Exception as e:
        get_cookies(x, useragent, thread)

def get_headers(token,thread):
    x = fingerprints[random.randint(0, (len(fingerprints)-1))]['x-super-properties']
    useragent = fingerprints[random.randint(0, (len(fingerprints)-1))]['useragent']
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': token,
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'referer':'https://discord.com',
        'sec-ch-ua': f'"Google Chrome";v="108", "Chromium";v="108", "Not=A?Brand";v="8"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'cookie': get_cookies(x, useragent, thread),
        'sec-fetch-site': 'same-origin',
        'user-agent': useragent,
        'x-context-properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjY3OTg3NTk0NjU5NzA1NjY4MyIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiIxMDM1ODkyMzI4ODg5NTk0MDM2IiwibG9jYXRpb25fY2hhbm5lbF90eXBlIjowfQ==',
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'en-US',
        'x-super-properties': x,
        'fingerprint': get_fingerprint(thread)
        }
    return headers, useragent

def get_captcha_key(rqdata: str, site_key: str, websiteURL: str, useragent: str):
    task_payload = {
        'clientKey': config['capmonster_key'],
        'task': {
            "type"             :"HCaptchaTaskProxyless",
            "isInvisible"      : True,
            "data"             : rqdata,
            "websiteURL"       : websiteURL,
            "websiteKey"       : site_key,
            "userAgent"        : useragent
                        }
    }
    key = None
    with httpx.Client(headers={'content-type': 'application/json', 'accept': 'application/json'},
                    timeout=30) as client:   
        task_id = client.post(f'https://api.capmonster.cloud/createTask', json=task_payload).json()['taskId']
        get_task_payload = {
            'clientKey': config['capmonster_key'],
            'taskId': task_id,
        }
        
        while key is None:
            response = client.post("https://api.capmonster.cloud/getTaskResult", json = get_task_payload).json()
            if response['status'] == "ready":
                key = response["solution"]["gRecaptchaResponse"]
            else:
                time.sleep(1)
            
    return key
    
#서버 참가
def join_server(session, headers, useragent, invite, token, thread):
    join_outcome = False
    guild_id = 0
    try:
        for i in range(10):
            response = session.post(f'https://discord.com/api/v9/invites/{invite}', json={}, headers = headers)
            if response.status_code == 429:
                error(f"You are being rate limited stopping for 3 seconds.")
                time.sleep(3)
                join_server(session, headers, useragent, invite, token)
            elif response.status_code in [200, 204]:
                join_outcome = True
                guild_id = response.json()["guild"]["id"]
                break
            elif "captcha_rqdata" in response.text:
                warn(f"Captcha detected {Fore.LIGHTBLACK_EX}token={Fore.WHITE}{token[:20]}...{Fore.RESET}")
                r = response.json()
                solution = get_captcha_key(rqdata = r['captcha_rqdata'], site_key = r['captcha_sitekey'], websiteURL = "https://discord.com", useragent = useragent)
                response = session.post(f'https://discord.com/api/v9/invites/{invite}', json={'captcha_key': solution,'captcha_rqtoken': r['captcha_rqtoken']}, headers = headers)
                if response.status_code in [200, 204]:
                    join_outcome = True
                    guild_id = response.json()["guild"]["id"]
                    break
        return join_outcome, guild_id
    except Exception as e:
        join_server(session, headers, useragent, invite, token, thread)
               
#부스팅 1X
def put_boost(session, headers, guild_id, boost_id):
    try:
        payload = {"user_premium_guild_subscription_slot_ids": [boost_id]}
        boosted = session.put(f"https://discord.com/api/v9/guilds/{guild_id}/premium/subscriptions", json=payload, headers=headers)
        if boosted.status_code == 201:
            return True
        elif 'Must wait for premium server subscription cooldown to expire' in boosted.text:
            return False
    except Exception as e:
        put_boost(session, headers, guild_id, boost_id)
    
def change_guild_name(session, headers, server_id, nick):
    try:
        jsonPayload = {"nick": nick}
        r = session.patch(f"https://discord.com/api/v9/guilds/{server_id}/members/@me", headers=headers, json=jsonPayload)
        if r.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        change_guild_name(session, headers, server_id, nick)
      
#서버 부스트 시작
def boost_server(invite:str , months:int, token:str, thread:int, nick: str):
    if months == 1:
        filename = "assets/1m_tokens.txt"
    if months == 3:
        filename = "assets/3m_tokens.txt"
    try:
        session = tls_client.Session(ja3_string = fingerprints[random.randint(0, (len(fingerprints)-1))]['ja3'], client_identifier = random.choice(client_identifiers))
        if config['proxyless'] == False and len(open("assets/proxies.txt", "r").readlines()) != 0:
            proxy = getproxy()
            session.proxies.update(proxy)

        headers, useragent = get_headers(token, thread)
        boost_data = session.get(f"https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots", headers=headers)

        if "401: Unauthorized" in boost_data.text:
            error(f"Token invalid {Fore.LIGHTBLACK_EX}token={Fore.WHITE}{token[:20]}...{Fore.RESET}")
            variables.failed_tokens.append(token)
            remove(token, filename)
        if "You need to verify your account in order to perform this action." in boost_data.text:
            error(f"Token locked {Fore.LIGHTBLACK_EX}token={Fore.WHITE}{token[:20]}...{Fore.RESET}")
            variables.failed_tokens.append(token)
            remove(token, filename)
        if boost_data.status_code == 200:
            if len(boost_data.json()) != 0:
                join_outcome, guild_id = join_server(session, headers, useragent, invite, token, thread)
                if join_outcome:
                    success(f"Successfully joined {Fore.LIGHTBLACK_EX}token={Fore.WHITE}{token[:20]}...{Fore.RESET}")
                    for boost in boost_data.json():
                        boost_id = boost["id"]
                        boosted = put_boost(session, headers, guild_id, boost_id)
                        if boosted:
                            success(f"Successfully boosted server once!")
                            variables.boosts_done += 1
                            if token not in variables.success_tokens:
                                variables.success_tokens.append(token)
                        else:
                            error(f"Failed to boost {Fore.LIGHTBLACK_EX}token={Fore.WHITE}{token[:20]}...{Fore.RESET}")
                            if token not in variables.failed_tokens:
                                variables.failed_tokens.append(token)
                    remove(token, filename)
                    if config["change_server_nick"]:
                        changed = change_guild_name(session, headers, guild_id, nick)
                        if changed:
                            success(f"Successfully renamed user!")
                        else:
                            error(f"Failed to rename")
                else:
                    error(f"Failed to join")
                    variables.failed_tokens.append(token)
            else:
                remove(token, filename)
                error(f"Token doesnt have nitro")
                variables.failed_tokens.append(token)                  
    except Exception as e:
        boost_server(invite, months, token, thread, nick)

def tboost(invite, amount, months, nick):
    variables.boosts_done = 0
    variables.success_tokens = []
    variables.failed_tokens = []
    if months == 1:
        filename = "assets/1m_tokens.txt"
    if months == 3:
        filename = "assets/3m_tokens.txt"
    if validateInvite(invite) == False:
        return False
        
    while variables.boosts_done != amount:
        print()
        tokens = get_all_tokens(filename)
        
        if variables.boosts_done % 2 != 0:
            variables.boosts_done -= 1
            
        numTokens = int((amount - variables.boosts_done)/2)
        if len(tokens) == 0 or len(tokens) < numTokens:
            return False
        else:
            threads = []
            for i in range(numTokens):
                token = tokens[i]
                thread = i+1
                t = threading.Thread(target=boost_server, args=(invite, months, token, thread, nick))
                t.daemon = True
                threads.append(t)
            for i in range(numTokens):
                threads[i].start()
            for i in range(numTokens):
                threads[i].join()
    return True
        
if __name__ == "__main__":
    os.system('cls')
    menu()
