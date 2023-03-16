revenues = {
    "sp": 67836.43,
    "rj": 36678.66,
    "mg": 29229.88,
    "es": 27165.48,
    "outros": 19849.53
}
total = sum(revenues[x] for x in revenues)
print("R$"+str(total)+" é o faturamento total da empresa")

for key, value in revenues.items():
    print(str(key)+" representa "+ (f'{(value/total):.2%}') +" do faturamento nacional da empresa")