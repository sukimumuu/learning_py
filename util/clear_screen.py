import os

def clean_view():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')