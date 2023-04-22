#!/usr/bin/python3

class Conta:
    """
    Classe para criar nova conta de cliente. Será informado o número da conta,
    o nome do titular, o saldo da conta e o seu limite
    """
    def __init__(self, numero, titular, saldo, limite = 2000.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        """
        Exibe o saldo do titular da conta. Exemplo: Saldo de 51.0 do titular Leo Sales
        """
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        """
        Adiciona um valor no saldo do titular da conta
        """
        self.__saldo += valor

    def saca(self, valor):
        """
        Retira um valor do saldo do titular da conta
        """
        self.__saldo -= valor

    def transfere(self, valor, destino):
        """
        Transfere um valor entre contas existentes.
        conta2.transfere(10.0, conta)
        """
        self.saca(valor)
        destino.deposita(valor)
