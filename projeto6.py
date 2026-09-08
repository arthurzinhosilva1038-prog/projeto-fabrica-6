def somarImposto(valor, taxaimposto):
    return valor + (valor * taxaimposto / 100)

print("=== cálculo de Preço com Imposto === ")
valor = float(input("Digite a taxa de imposto (%)"))
taxaImposto = float(input("Digite o custo do item (antes do imposto): "))]

valorImposto = somarImposto(valor, taxaImposto)
print(f"Preço final com imposto: R$ {valorImposto}")