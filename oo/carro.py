


"""
voçe deve criar uma classe de carro que vai possuir
doi atributos compostos por outras duas classes:

1) motor
2)direção

motor tera responsabilidade de controlar a velocidade.
Ela oferece os sequintes atributos:

1)atributo de dado veloscidade
2)Metodo acelerar, que devera incrementar a velocidade de
uma unidade
3)Metodo frear que devera incrementar a velocidade em duas
unidades

A direçao tera a responsabilidade de controlar a direção. Ela
oferece
os sequintes atributos:

1)Valor de diração com valores possiveis: norte, sul, leste,
oeste.
2)Metodo girar_a_direita
3)Metodo girar_a_esquerda


     N

O         L

     S


Exemplo:
    >>> # testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando = Direção
    >>> direçao = Direcao()
    >>> direçao.valor
    'Norte'
    >>> direçao.girar_a_direita()
    >>> direçao.valor
    'Leste'
    >>> direçao.girar_a_direita()
    >>> direçao.valor
    'Sul'
    >>> direçao.girar_a_direita()
    >>> direçao.valor
    'Oeste'
    >>> direçao.girar_a_direita()
    >>> direçao.valor
    'Norte'
    >>> direçao.girar_a_esquerda()
    >>> direçao.valor
    'Oeste'
    >>> direçao.girar_a_esquerda()
    >>> direçao.valor
    'Sul'
    >>> direçao.girar_a_esquerda()
    >>> direçao.valor
    'Leste'
    >>> direçao.girar_a_esquerda()
    >>> direçao.valor
    'Norte'
    >>> carro = Carro(direçao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direçao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direçao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direçao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direçao()
    'Oeste'

"""

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'



class Direcao:
    rotacao_a_direita_dct = {
            NORTE: LESTE,LESTE:SUL, SUL:OESTE, OESTE: NORTE}

    rotacao_a_esquerda_dct = {
            NORTE: OESTE,LESTE: NORTE, SUL: LESTE, OESTE: SUL}

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]



class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)