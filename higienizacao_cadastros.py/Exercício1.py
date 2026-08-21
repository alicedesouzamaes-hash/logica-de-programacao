nome_bruto = " joão pedro da silva "
email_bruto = " JOÃO.SILVA@Escola.COM "

nome_limpo = nome_bruto.strip().upper()
email_limpo = email_bruto.strip().lower()

print("--- Exercício 1: Nome e E-mail ---")
print(f"Nome higienizado: {nome_limpo}")
print(f"E-mail higienizado: {nome_limpo}\n")
