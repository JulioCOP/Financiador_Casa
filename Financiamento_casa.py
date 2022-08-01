#Programa para aprovar o empréstimo bancário para a compra de uma casa. É perguntado o valor da casa,
# o salário do comprador e em quantos anos ele pretende financiar. A prestação mensal não pode exceder
# 30% do salário ou então o empréstimo será negado.

from time import sleep
import emoji
from emoji import emojize

valor_casa= float(input("Qual o valor da casa ? "))
salario= float(input("Qual o salario do comprador ? "))
anos= int(input("Quantos anos o usuario deseja financiar a casa ? "))
valor_prestacao= (valor_casa/ (anos*12))
sleep(1)
print(".",end="")
sleep(0.5)
print(".",end="")
sleep(0.5)
print(".",end="")
sleep(0.5)
print(".",end="")
sleep(0.5)
print("\n{} Essa casa será paga em {} anos, com valor da prestação de R$ {:.2f} {}" .format('\033[7;33;40m',anos, valor_prestacao, '\033[m'))
limite= salario*0.3
print("É permitido ao comprador pagar uma prestação no valor até {}R$ {:.2f} {}".format('\033[1;34m',limite, '\033[m'))
sleep(1)
while valor_prestacao > limite:
    print("{}O usuário deve informar um PRAZO de financiamento MAIOR.{}".format('\033[1;35m','\033[m'))
    sleep(0.75)
    anos = int(input("Digite um novo período em que o usuário deseja financiar a casa ? "))
    valor_prestacao = (valor_casa / (anos * 12))
    sleep(1)
    print(".", end="")
    sleep(0.5)
    print(".", end="")
    sleep(0.5)
    print(".", end="")
    sleep(0.5)
    print(".", end="")
    sleep(0.5)
    print("\n{} Essa casa será paga em {} anos, com valor da prestação de R$ {:.2f} {}".format('\033[7;33;40m', anos,valor_prestacao,'\033[m'))
    limite = salario * 0.3
    sleep(1.5)
    print("É permitido ao comprador pagar uma prestação no valor até {}R$ {:.2f} {}".format('\033[1;34m', limite,'\033[m'))
    sleep(1.5)
if valor_prestacao<=limite:
    sleep(0.5)
    print("Emprestimo {}PERMITIDO{}" .format('\033[1;32m', '\033[m'))
    print(emoji.emojize(":wink: :ok_hand:", use_aliases=True))
else:
    print("Emprestimo {}NEGADO{}, o salario do funcionário excede o limite permitido de 30% do salário.".format('\033[1;31m', '\033[m'))
    print(emoji.emojize(":cry: :thumbsdown:", use_aliases=True))