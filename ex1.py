num1 = int(input("Digite os primeiros Gols:"))
num2 = int(input("Digite os segundos Gols:"))

if num1 == num2:
    print("Foi um impate")
elif num1 < num2:
    print("A vitória foi do segundo time")
else:
    print("A vitória foi do primeiro time")
