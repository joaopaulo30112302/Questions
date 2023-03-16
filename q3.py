import json
with open("dados.json", encoding="utf-8") as file:
    dataJson = json.load(file)
days = []
values = []
highest = []
lowest = []
for x in range(len(dataJson)):
    days.append(dataJson[x]["dia"])
    values.append(dataJson[x]["valor"])
average = sum(values) / (len(days) - values.count(0))
highest.append(max(values, key=float))
highest.append(days[values.index(highest[0])])
lowest.append(min([x for x in values if x !=0]))
lowest.append(days[values.index(lowest[0])])

print("A média dos faturamentos diários é R$"+str(f'{(average):.2f}'))
print("O dia "+str(highest[1])+" teve o maior faturamento, com valor de R$"+str(f'{(highest[0]):.2f}'))
print("O dia "+str(lowest[1])+" teve o menor faturamento, com valor de R$"+str(f'{(lowest[0]):.2f}'))