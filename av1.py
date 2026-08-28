# ==============================================================================
# PROVA PRÁTICA AV1 - 3º BIMESTRE
# ARQUIVO: av1_saneamento_dados.py
# Nome do Aluno: Alice de Souza Maes. 
# Data: 28/08/26
# ==============================================================================

# Lista de cadastros brutos recebidos do sistema
cadastros_brutos = [
   "  joao da silva;11988887777  ",
   "  maria sousa;21977776666  ",
   "  carlos edgardo oliveira;31966665555  ",
   "  ana paula lima;41955554444  "
]

print("==================================================")
print("     SISTEMA DE SANEAMENTO DE DADOS - AV1         ")
print("==================================================\n")

# TODO: Escreva o laco de repeticao usando for e range() para percorrer a lista
for i in range(len(cadastros_brutos)):
   
   # 1. Remova os espacos extras do inicio e fim do cadastro atual
   dados_limpos = cadastros_brutos[i].strip()
   
   # 2. Separe o nome e o telefone (Dica: use o metodo .split(";"))
   partes = dados_limpos.split(";")
   nome_bruto = partes[0]
   telefone = partes [1]
   # 3. Converta o nome para letras MAIUSCULAS
   nome_maiusculo = nome_bruto.upper()
   # 4. Extraia o DDD (2 primeiros digitos do telefone) usando fatiamento [0:2]
   telefone = telefone[1:3]
   
   # 5. Exiba o resultado padronizado no terminal
   # Exemplo de print formatado desejado:
   # Funcionario: NOME MAIUSCULO | DDD: 11 | Telefone: 11988887777
   print(f"Funcionario: {nome_maiusculo} | DDD: {telefone} | Telefone: {partes[1]}")
   pass

print("\n==================================================")
print("             PROCESSAMENTO CONCLUÍDO              ")
print("==================================================")
