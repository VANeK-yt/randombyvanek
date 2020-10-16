import random
import time
import colorama

from colorama import Fore, Back, Style
colorama.init(convert=True)

ipolse = float(input("Введите число до ста"))
if ipolse <= 100:
  while True:
    rand0m = random.randint(1, 100)
    print(Style.RESET_ALL)
    print(Back.YELLOW + Fore.BLUE + "Программа выбрала число " + str(rand0m) )
    if rand0m == ipolse:
      time.sleep(0.2)
      print(Back.MAGENTA + Fore.GREEN + "Это правда!")
      print(Style.RESET_ALL)
      input("enter")
      break
    else:
      time.sleep(0.2)
      print(Back.CYAN + Fore.RED + "Это ложь!")
      time.sleep(0.5)
      
    
