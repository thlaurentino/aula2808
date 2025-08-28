preco_produto = 280.00
peso_kg = 3.5
codigo_regiao = 1
tipo_cliente = "PREMIUM"

custo_kg_regiao1 = 5.00
custo_kg_regiao2 = 7.50
custo_kg_outras_regioes = 10.00

limite_desconto_padrao = 250.00
percentual_desconto_padrao = 0.10

limite_frete_gratis_premium = 200.00

print("--- Iniciando processamento logístico ---")
custo_frete = 0.0

if codigo_regiao == 1:
    custo_frete = peso_kg * custo_kg_regiao1
elif codigo_regiao == 2:
    custo_frete = peso_kg * custo_kg_regiao2
else:
    custo_frete = peso_kg * custo_kg_outras_regioes

print(f"Custo de transporte base calculado: R$ {custo_frete:.2f}")

valor_desconto = 0.0

if tipo_cliente == "PREMIUM":
    print("Cliente PREMIUM identificado. Verificando benefício de transporte...")
    if preco_produto > limite_frete_gratis_premium:
        print(">>> Benefício aplicado: Custo de transporte zerado!")
        custo_frete = 0.0
    else:
        print(">>> Compra abaixo do limite para benefício de transporte.")

elif tipo_cliente == "PADRAO":
    print("Cliente PADRAO identificado. Verificando benefício no produto...")
    if preco_produto > limite_desconto_padrao:
        print(">>> Benefício aplicado: Desconto de 10% no produto!")
        valor_desconto = preco_produto * percentual_desconto_padrao
    else:
        print(">>> Compra abaixo do limite para benefício no produto.")

total_a_pagar = (preco_produto + custo_frete) - valor_desconto

print("\n--- Relatório Final da Transação ---")
print(f"Valor do Produto: R$ {preco_produto:.2f}")
print(f"Custo de Transporte Final: R$ {custo_frete:.2f}")
print(f"Desconto Aplicado: R$ {valor_desconto:.2f}")
print("====================================")
print(f"VALOR TOTAL A PAGAR: R$ {total_a_pagar:.2f}")
print("====================================")