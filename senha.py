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

def generate_suggested_password(length=12):
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))

def register_user(users_db):
    user_input = input("Digite o seu nome: ").strip()
    while not user_input:
        print(TerminalColor.ERRO + "O espaço não pode ser vazio!" + TerminalColor.NORMAL)
        user_input = input("Digite o seu nome: ").strip()
    
    while True:
        user_password = stdiomask.getpass("Digite sua senha: ").strip()
        if len(user_password) < 5:
            print(TerminalColor.ERRO + "Sua senha é muito curta! Deve ter pelo menos 5 caracteres." + TerminalColor.NORMAL)
            time.sleep(2)
           
            suggested_password = generate_suggested_password()
            print("Aqui está uma senha sugerida: ", end="")
            slow_print(suggested_password, delay=0.1)
            
            use_suggested = input("Deseja usar a senha sugerida? (sim/não): ").strip().lower()
            if use_suggested in ['s', 'sim', 'ss']:
                user_password = suggested_password
                print("Senha sugerida aceita!")
                break
            else:
                print("Por favor, insira uma nova senha.")
        else:
            print("Senha aceita!")
            break

    users_db[user_input] = user_password
    print(f"Cadastro concluído! Seu nome é {user_input} e sua senha é: {'*' * len(user_password)}")

def login_user(users_db):
    max_attempts = 2
    attempts = 0

    while attempts < max_attempts:
        username = input("Digite seu nome: ").strip()
        if username in users_db:
            password = stdiomask.getpass("Digite sua senha: ").strip()
            if users_db[username] == password:
                print("Login bem-sucedido!")
                return True
            else:
                print(TerminalColor.ERRO + "Senha incorreta!" + TerminalColor.NORMAL)
        else:
            print(TerminalColor.ERRO + "Usuário não encontrado!" + TerminalColor.NORMAL)
        
        attempts += 1
        if attempts < max_attempts:
            print(f"Tente novamente. {max_attempts - attempts} tentativa(s) restante(s).")
    
    print(TerminalColor.ERRO + "Número máximo de tentativas alcançado." + TerminalColor.NORMAL)
    return False

def main():
    users_db = {}

    # Tenta fazer login
    print("\nÁrea de Login")
    logged_in = login_user(users_db)
    
    if not logged_in:
        if not users_db:
            print("\nNenhum usuário encontrado. Você deseja se cadastrar?")
            response = input("Digite 'sim' para ir para a área de cadastro ou 'não' para sair: ").strip().lower()
            if response in ['s', 'sim', 'ss']:
                print("\nIniciando cadastro...")
                register_user(users_db)
                print("\nAgora você pode fazer login com suas novas credenciais.")
                login_user(users_db)
            else:
                print("Saindo do programa.")
        else:
            print("Saindo do programa.")

if __name__ == "__main__":
    main()
