import random
import string
import pyfiglet
from colorama import init, Fore, Style
init(autoreset=True)
def main():
    ascii_banner = pyfiglet.figlet_format("PWG")
    print(Fore.CYAN + ascii_banner)
    while True:
        userPreferenceA = input(Fore.YELLOW + "How long do you want the password to be (enter only an integer)? ")
        if userPreferenceA.isdigit():
            leng = int(userPreferenceA)
            break
        else:
            print(Fore.RED + "Please enter a valid integer.")
    chars = ""
    while True:
        userPreferenceB = input(Fore.YELLOW + "Do you want to add letters to the password for basic security (press Y [yes] or N [no])? ").upper()
        if userPreferenceB in ["Y", "N"]:
            break
        else:
            print(Fore.RED + "Invalid choice. Try again.")
    if userPreferenceB == "Y":
        while True:
            userPreferenceC = input(Fore.YELLOW + "Do you want a combination of upper- and lowercase letters in the password (press Y [yes] or N [no])? ").upper()
            if userPreferenceC in ["Y", "N"]:
                break
            else:
                print(Fore.RED + "Invalid choice. Try again.")
        if userPreferenceC == "Y":
            chars += string.ascii_letters
        else:
            while True:
                userPreferenceD = input(Fore.YELLOW + "Press L for lowercase letters, U for uppercase letters, or B for a combination of both. ").upper()
                if userPreferenceD == "L":
                    chars += string.ascii_lowercase
                    break
                elif userPreferenceD == "U":
                    chars += string.ascii_uppercase
                    break
                elif userPreferenceD == "B":
                    chars += string.ascii_letters
                    break
                else:
                    print(Fore.RED + "Invalid choice. Try again.")
    while True:
        userPreferenceE = input(Fore.YELLOW + "Do you want to add numbers to the password for additional security (press Y [yes] or N [no])? ").upper()
        if userPreferenceE in ["Y", "N"]:
            break
        else:
            print(Fore.RED + "Invalid choice. Try again.")
    if userPreferenceE == "Y":
        chars += string.digits
    while True:
        userPreferenceF = input(Fore.YELLOW + "Do you want to add punctuation characters to the password for additional security (press Y [yes] or N [no])? ").upper()
        if userPreferenceF in ["Y", "N"]:
            break
        else:
            print(Fore.RED + "Invalid choice. Try again.")
    if userPreferenceF == "Y":
        chars += string.punctuation
    if chars == "":
        print (Fore.RED + "No character types selected; a password cannot be generated.")
    else:
        result = ''.join(random.choices(chars, k=leng))
        print (Fore.GREEN + result)
if __name__ == "__main__":
    main()