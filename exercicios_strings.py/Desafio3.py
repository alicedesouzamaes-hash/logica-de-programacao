email = input("Digite seu e-mail (nome.sobrenome@eaportal.org): ")

primeiro_nome = email[0:5]
domínio = email[11:]

print(f"Primeiro nome estraído: {primeiro_nome}")
print(f"Domínio extraído: {domínio}")
