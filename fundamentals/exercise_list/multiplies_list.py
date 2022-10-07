factor = int(input())
count = int(input())
factored = []
suma = factor
for number in range(count):
    factored.append(suma)
    suma += factor
print(factored)