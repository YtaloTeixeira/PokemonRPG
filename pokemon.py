import random

class Pokemon:

    def __init__(self, especie, nome=None, lvl=None):
        self.especie = especie
        if lvl:
        
            self.lvl = lvl
        else:
            self.lvl = random.randint(1, 100)
        if nome:
            self.nome = nome
        else:
            self.nome = especie
        

    def __str__(self):
        return "{} ({})".format(self.especie, self.lvl)
    
    def atacar(self, pokemon):
        print("{} atacou {}!".format(self.especie, pokemon.especie))


class PokemonEletrico(Pokemon):
    tipo = "Elétrico"

    def atacar(self, pokemon):
        print("{} lançou RAIO DO TROVÃO em {}".format(self, pokemon))

class PokemonFogo(Pokemon):
    tipo = "Fogo"

    def atacar(self, pokemon):
        print("{} lançou BOLA DE FOGO em {}".format(self, pokemon))

class PokemonAgua(Pokemon):
    tipo = "Água"

    def atacar(self, pokemon):
        print("{} lançou ENCHARCAR em {}".format(self, pokemon))

class PokemonPlanta(Pokemon):
    tipo = "Planta"

    def atacar(self, pokemon):
        print("{} lançou ENCHARCAR em {}".format(self, pokemon))


class PokemonVenenoso(Pokemon):
    tipo = "Venenoso"

    def atacar(self, pokemon):
        print("{} lançou ENCHARCAR em {}".format(self, pokemon))


class PokemonVenenoso(Pokemon):
    tipo = "Venenoso"

    def atacar(self, pokemon):
        print("{} lançou CUSPE em {}".format(self, pokemon))


class PokemonPedra(Pokemon):
    tipo = "Pedra"

    def atacar(self, pokemon):
        print("{} lançou PEDREGULHO em {}".format(self, pokemon))


class PokemonInseto(Pokemon):
    tipo = "Inseto"

    def atacar(self, pokemon):
        print("{} lançou JOANINHA em {}".format(self, pokemon))
