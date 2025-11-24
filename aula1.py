# Aula 1 — Fundamentos de Python
# EBAC = Escola Britânica de Artes Criativas e Tecnologia
'''
Criei esse arquivo para registrar meus estudos sobre Python para Ciência de Dados,
do curso de Ciência de Dados da EBAC.
'''

# -----------------------------------------
# 1 - Print básico
# -----------------------------------------
# O print exibe algo na tela (no terminal)
print("Olá, Bruno! Seja bem-vindo ao Python.")


# -----------------------------------------
# 2 - Variáveis e Tipos de Dados
# -----------------------------------------
# Variáveis com diferentes tipos:
nome = "Bruno"           # string
idade = 33               # int
altura = 1.74            # float
usa_oculos = True       # bool

print(nome)
print(idade)
print(altura)
print(usa_oculos)


# -----------------------------------------
# 3) Input — Pegando Dados do Usuário
# -----------------------------------------
# input() captura algo digitado pelo usuário.
# O que vem do input é sempre uma String.
nome_usuario = input("Qual seu nome? ")
idade_usuario = input("Quantos anos você tem? ")

print("Olá,", nome_usuario + "! Você tem", idade_usuario, "anos.")


# -----------------------------------------
# 4 - Conversão de Tipos
# -----------------------------------------
# Para fazer contas, converter para int ou float.
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

resultado = numero1 + numero2

print("A soma é:", resultado)


# -----------------------------------------
# 5 - Mini Pojeto — Calculadora de Comissão
# -----------------------------------------
# Esse é um programa simples que calcula comissão de vendas

print("=== Calculadora de Comissão ===")

# Pedimos o valor da venda e convertemos para float
venda = float(input("Valor da venda: R$ "))
comissao = float(input("Percentual da comissão (%): "))

# Cálculo da comissão
valor_comissao = venda * (comissao / 100)

print("Você receberá: R$", valor_comissao)


# -----------------------------------------
# 6 - Exercício 1:  Dados do Profissional
# -----------------------------------------

print("\n=== Exercício 1 ===")

nome = input("Seu nome: ")
cargo = input("Seu cargo: ")
empresa = input("Sua empresa: ")

print("Olá,", nome + "! Você é", cargo, "na empresa", empresa + ".")


# --------------------------------------------
# 7 - Exercício 2: Cálculo do Total da Compra
# --------------------------------------------

print("\n=== Exercício 2 ===")

preco = float(input("Preço do produto: R$ "))
quantidade = int(input("Quantidade: "))

total = preco * quantidade

print("Total da compra: R$", total)


# -----------------------------------------
# 8 - Exercício 3: Metas de Vendas
# -----------------------------------------

print("\n=== Exercício 3 ===")

meta = float(input("Meta do mês (R$): "))
vendas = float(input("Vendas realizadas (R$): "))

falta = meta - vendas
percentual = (vendas / meta) * 100

print("Falta para bater a meta: R$", falta)
print("Percentual atingido:", percentual, "%")