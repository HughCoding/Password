import stdiomask
import secrets
import string
import time
import sys

class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'  

def slow_print(message, delay=0.05):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def get_credentials():
    user_input = input("Digite o seu nome: ").strip()
    while not user_input:
        print(TerminalColor.ERRO + "O espaço não pode ser vazio!" + TerminalColor.NORMAL)
        user_input = input("Digite o seu nome: ").strip()
    
    password_length = 12 

    while True:
        user_password = stdiomask.getpass("Digite sua senha: ").strip()
        if len(user_password) < 5:
            print(TerminalColor.ERRO + "Sua senha é muito curta! Deve ter pelo menos 5 caracteres." + TerminalColor.NORMAL)
            time.sleep(2)
           
            suggested_password = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(password_length))
            print("Aqui está uma senha sugerida: ", end="")
            slow_print(suggested_password, delay=0.1)
            
            use_suggested = input("Deseja usar a senha sugerida? (sim/não): ").strip().lower()
            if use_suggested in ['s', 'sim', 'ss']:
                print("Senha sugerida aceita!")
                break
            else:
                print("Por favor, insira uma nova senha.")
        else:
            print("Senha aceita!")
            break

    if len(user_password) >= 5:
     print(f"Seu nome é {user_input} e sua senha é: {'*' * len(user_password)}")


get_credentials()









