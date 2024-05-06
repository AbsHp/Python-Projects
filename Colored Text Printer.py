import colorama
from colorama import Back, Fore

colorama.init(autoreset = True)

text = input("Enter a phrase or sentence: ")

print(Fore.RED + text)
print(Back.RED + text)

print(Fore.YELLOW + Back.MAGENTA  + text)
print(Fore.GREEN + Back.WHITE  + text)
print(Fore.CYAN + Back.BLUE  + text)
print(Fore.GREEN + Back.MAGENTA  + text)
print(Fore.RED + Back.YELLOW  + text)
print(Fore.BLACK + Back.RED  + text)
print(Fore.WHITE + Back.CYAN  + text)
print(Fore.BLUE + Back.YELLOW  + text)
print(Fore.MAGENTA + Back.RED  + text)
