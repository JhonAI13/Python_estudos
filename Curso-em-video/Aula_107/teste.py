import moeda

p = float(input('Digite o preço: R$'))
print(f"""A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}.
O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}.
Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}""")