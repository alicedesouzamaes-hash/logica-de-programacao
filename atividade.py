# Solicite a quantidade total de itens
qtd_itens = int(input("Quantidade de itens: "))

# Inicializa a variável acumuladora
total_compra = 0.0

# Laço para ler o preço de cada item
for i in range(1, qtd_itens + 1):
    preco = float(input(f"Preço do item {i}: R$ "))
    total_compra += preco # Acumula o valor do item

# Cálculo da média
media_por_item = total_compra / qtd_itens if qtd_itens > 0 else 0

# Exibe o total da compra e a média por item
print(f"Total da compra: R$ {total_compra:.2f}")
print(f"Média por item: R$ {media_por_item:.2f}")