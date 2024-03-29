def verifica_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    if b == numero:
        return True
    else:
        return False

numero_procurado = int(input("Digite o número que deseja verificar na sequência de Fibonacci: "))

if verifica_fibonacci(numero_procurado):
    print("O número ",numero_procurado," pertence à sequência de Fibonacci.")
else:
    print("O número ",numero_procurado," não pertence à sequência de Fibonacci.")
