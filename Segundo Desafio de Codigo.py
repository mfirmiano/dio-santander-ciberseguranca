def verificar_comando(comando):
    # Caracteres suspeitos para injeção de comando
    caracteres_suspeitos = [';', '&', '|', '$']
    
    # TODO: Verifique se algum dos caracteres suspeitos está no comando:
    if any(c in comando for c in caracteres_suspeitos):
        return "Comando Suspeito"
    else:
        return "Comando Seguro"

# Entrada do usuário
comando_usuario = input()

# TODO: Retorne o resultado da verificação:
print (verificar_comando("cat file.txt; rm -rf /"))
