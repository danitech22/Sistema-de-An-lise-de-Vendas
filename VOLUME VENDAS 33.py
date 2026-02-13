vendas = [
    {"data": "2024-01-01", "vendedor": "Ana", "cliente": "Carlos", "valor": 200},
    {"data": "2024-01-01", "vendedor": "João", "cliente": "Maria", "valor": 150},
    {"data": "2024-01-02", "vendedor": "Ana", "cliente": "Carlos", "valor": 300},
    {"data": "2024-01-02", "vendedor": "Maria", "cliente": "Pedro", "valor": 100},
    {"data": "2024-01-03", "vendedor": "João", "cliente": "Carlos", "valor": 400},
    {"data": "2024-01-03", "vendedor": "Ana", "cliente": "Maria", "valor": 250},
    {"data": "2024-01-03", "vendedor": "Ana", "cliente": "Carlos", "valor": 50},
]

total_por_vendedor = {}
total_por_cliente = {}
qtd_por_cliente = {}
faturamento_por_dia = {}
volume_por_dia = {}

for venda in vendas:
    vendedor = venda["vendedor"]
    cliente = venda["cliente"]
    data = venda["data"]
    valor = venda["valor"]

    if vendedor not in total_por_vendedor:
        total_por_vendedor[vendedor] = 0
    total_por_vendedor[vendedor] += valor

    if cliente not in total_por_cliente:
        total_por_cliente[cliente] = 0
    total_por_cliente[cliente] += valor

    if cliente not in qtd_por_cliente:
        qtd_por_cliente[cliente] = 0
    qtd_por_cliente[cliente] += 1

    if data not in faturamento_por_dia:
        faturamento_por_dia[data] = 0
    faturamento_por_dia[data] += valor

    if data not in volume_por_dia:
        volume_por_dia[data] = 0
    volume_por_dia[data] += 1

vendedor_campeao = None
maior_venda = 0
for vendedor, total in total_por_vendedor.items():
    if total > maior_venda:
        maior_venda = total
        vendedor_campeao = vendedor

cliente_campeao = None
maior_gasto = 0
for cliente, total in total_por_cliente.items():
    if total > maior_gasto:
        maior_gasto = total
        cliente_campeao = cliente

cliente_recorrente = None
maior_qtd = 0
for cliente, qtd in qtd_por_cliente.items():
    if qtd > maior_qtd:
        maior_qtd = qtd
        cliente_recorrente = cliente

dia_faturamento_campeao = None
maior_faturamento = 0
for data, total in faturamento_por_dia.items():
    if total > maior_faturamento:
        maior_faturamento = total
        dia_faturamento_campeao = data

dia_volume_campeao = None
maior_volume = 0
for data, qtd in volume_por_dia.items():
    if qtd > maior_volume:
        maior_volume = qtd
        dia_volume_campeao = data

print("- 📊 Total por vendedor:\n", total_por_vendedor)
print("\n -🧍 Total por cliente:\n", total_por_cliente)
print("\n -🔁 Compras por cliente:\n", qtd_por_cliente)
print("\n -🏆 Vendedor campeão:\n", vendedor_campeao)
print("\n -🏆 Cliente campeão:\n", cliente_campeao)
print("\n -🔁 Cliente recorrente:\n", cliente_recorrente)
print("\n -💰 Dia maior faturamento:\n", dia_faturamento_campeao)
print("\n -📦 Dia maior volume:\n", dia_volume_campeao)














 








    


