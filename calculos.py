def calculadora():
  while True:
    num1 = float(input("Digite o primeiro número: "));
    num2 = float(input("Digite o segundo número: "));
    operacao = input("Escolha a operação: +, -, *, / : ");
    break
  
  if operacao not in ["+", "-", "*", "/"]:
    print("DIGITE UMA OPERAÇÃO VÁLIDA!");
    calculadora()
  else:
    if(operacao == "+"):
        soma = num1 + num2;
        print(soma);
    elif(operacao == "-"):
        sub = num1 - num2;
        print(sub);
    if(operacao == "*"):
      mul = (num1 * num2);
      print(mul);
    elif(operacao == "/"):
      if (num2 != 0):
        divisao = (num1/num2);
        print(divisao)
      else:
        print("Divisão por 0 não pode");
        calculadora()
        

calculadora();