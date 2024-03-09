# Import das bibliotecas
import pyautogui
import time
import pyfiglet
from termcolor import colored

# Banner
banner = colored(pyfiglet.figlet_format("Joy Boy"), color='white')
print(banner)
print('By FeyHan_042')

# Coleta o alvo por input
alvo = input("Digite o URL do alvo aqui: ")
time.sleep(1)

# Coordenadas do meu monitor...
# Ajuste-as para se adaptar ao seu monitor
tela1 = 349, 112
tela2 = 986, 276
tela3 = 357, 450
tela4 = 966, 495

# Opera nas 4 abas do terminator
# Ajuste com as ferramentas de seu gosto.

pyautogui.leftClick(tela1)
time.sleep(3)
pyautogui.typewrite(f'nmap {alvo}')
pyautogui.hotkey('Enter')
time.sleep(5)
pyautogui.leftClick(tela2)
time.sleep(3)
pyautogui.typewrite(f'findomain -t {alvo}')
pyautogui.hotkey('Enter')
time.sleep(10)
pyautogui.leftClick(tela3)
time.sleep(10)
pyautogui.typewrite(f'httpx -u {alvo} -sc 200')
pyautogui.hotkey('Enter')
time.sleep(10)
pyautogui.leftClick(tela4)
time.sleep(2)
pyautogui.typewrite(f'nuclei -u {alvo} -t /home/sandro/nuclei-templates/http')
pyautogui.hotkey('Enter')
time.sleep(8)
pyautogui.leftClick(tela3)
time.sleep(2)
pyautogui.typewrite(f'cd sqlmap ; python sqlmap.py -u {alvo} --dbs')
pyautogui.hotkey('Enter')
time.sleep(10)
pyautogui.leftClick(tela2)
time.sleep(2)
pyautogui.typewrite(f'gobuster dir -u https://{alvo}/ -w /home/sandro/wordlists/wordlists/discovery/directory_list_lowercase_2.3_small.txt')
pyautogui.hotkey('Enter')
time.sleep(2)
pyautogui.leftClick(tela1)
pyautogui.typewrite(f'cd .. ; dalfox url https://www.{alvo}/')
pyautogui.hotkey('Enter')
