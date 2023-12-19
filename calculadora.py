def calculadora(num1, num2, operacao):
  if operacao == 1:
    resultado = num1 + num2
  elif operacao == 2:
    resultado = num1 - num2
  elif operacao == 3:
    resultado = num1 * num2
  elif operacao == 4:
    if num2 != 0:
      resultado = num1 / num2
    else:
      print("Erro")
      return 0
    
  else:
    print("Inválida!")
    resultado = 0

  return resultado

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = int(input("Digite a operação (1: Soma, 2: Subtração, 3: Multiplicação, 4: Divisão): "))

resultado = calculadora(numero1, numero2, operacao)
print("Resultado da operação:", resultado)
