#!/usr/bin/python3
def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo":saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))

conta = cria_conta(123, "Leo", 55.0, 1000.0)

print(conta)

deposita(conta, 15.0)
print(conta)

saca(conta, 20.0)
print (conta)
