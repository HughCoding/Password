import stdiomask
import secrets
import string
import time
import sys

class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'  

def slow_print(mensagem, delay=0.05):
    for char in mensagem:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def gerar_senha_sugerida(length=12):
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))

def registro_usuario(usuarios_db):
    usuario_input = input("Digite o seu nome: ").strip()
    while not usuario_input:
        print(TerminalColor.ERRO + "O espaço não pode ser vazio!" + TerminalColor.NORMAL)
        usuario_input = input("Digite o seu nome: ").strip()
    
    while True:
        usuario_senha = stdiomask.getpass("Digite sua senha: ").strip()
        if len(usuario_senha) < 5:
            print(TerminalColor.ERRO + "Sua senha é muito curta! Deve ter pelo menos 5 caracteres." + TerminalColor.NORMAL)
            time.sleep(2)
           
            senha_sugerida = gerar_senha_sugerida()
            print("Aqui está uma senha sugerida: ", end="")
            slow_print(senha_sugerida, delay=0.1)
            
            use_suggested = input("Deseja usar a senha sugerida? (sim/não): ").strip().lower()
            if use_suggested in ['s', 'sim', 'ss']:
                usuario_senha = senha_sugerida
                print("Senha sugerida aceita!")
                break
            else:
                print("Por favor, insira uma nova senha.")
        else:
            print("Senha aceita!")
            break

    usuarios_db[usuario_input] = usuario_senha
    print(f"Cadastro concluído! usuário: {usuario_input} | senha: {'*' * len(usuario_senha)}")

def login_user(usuarios_db):
    tentativa_maxima = 2
    tentativas = 0

    while tentativas < tentativa_maxima:
        usuario = input("Digite seu nome: ").strip()
        if usuario in usuarios_db:
            senha = stdiomask.getpass("Digite sua senha: ").strip()
            if usuarios_db[usuario] == senha:
                print("Login bem-sucedido!")
                return True
            else:
                print(TerminalColor.ERRO + "Senha incorreta!" + TerminalColor.NORMAL)
        else:
            print(TerminalColor.ERRO + "Usuário não encontrado!" + TerminalColor.NORMAL)
        
        tentativas += 1
        if tentativas < tentativa_maxima:
            print(f"Tente novamente. {tentativa_maxima - tentativas} tentativa(s) restante(s).")
    
    print(TerminalColor.ERRO + "Número máximo de tentativas alcançado." + TerminalColor.NORMAL)
    return False

def main():
    usuarios_db = {}


    print("\nÁrea de Login")
    logado = login_user(usuarios_db)
    
    if not logado:
        if not usuarios_db:
            print("\nNenhum usuário encontrado. Você deseja se cadastrar?")
            response = input("Digite 'sim' para ir para a área de cadastro ou 'não' para sair: ").strip().lower()
            if response in ['s', 'sim', 'ss']:
                print("\nIniciando cadastro...")
                registro_usuario(usuarios_db)
                print("\nAgora você pode realizar o login com suas novas credenciais.")
                login_user(usuarios_db)
            else:
                print("Saindo do programa.")
        else:
            print("Saindo do programa.")

if __name__ == "__main__":
    main()
