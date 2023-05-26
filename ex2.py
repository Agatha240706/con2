valor = float(input("valor da compra:"))
num = float(input("Quantidade de prestações:"))

prest = valor/num

if valor > 500:
    print('você não consegue pagar')
else:
    print("você pode pagar")