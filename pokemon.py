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
        self.ataque = self.lvl * 5
        self.hp = self.lvl * 15.5

    def __str__(self):
        return "{} ({})".format(self.especie, self.lvl)

    def atacar(self, pokemon):
        danoMáximo = int((self.ataque * random.random() * 1.2)) # Ataque máximo 6
        pokemon.hp -= danoMáximo
        print("{} perdeu {} pontos de vida!".format(pokemon, danoMáximo))

        if pokemon.hp <= 0:
            print("{} foi derrotado!".format(pokemon))
            return True
        else:
            return False


class PokemonEletrico(Pokemon):
    tipo = "Elétrico"

    def atacar(self, pokemon):
        print("{} lançou RAIO DO TROVÃO em {}".format(self, pokemon))
        return super().atacar(pokemon)


class PokemonFogo(Pokemon):
    tipo = "Fogo"

    def atacar(self, pokemon):
        print("{} lançou BOLA DE FOGO em {}".format(self, pokemon))
        return super().atacar(pokemon)


class PokemonAgua(Pokemon):
    tipo = "Água"

    def atacar(self, pokemon):
        print("{} lançou ENCHARCAR em {}".format(self, pokemon))
        return super().atacar(pokemon)


class PokemonPlanta(Pokemon):
    tipo = "Planta"

    def atacar(self, pokemon):
        print("{} lançou ENCHARCAR em {}".format(self, pokemon))
        return super().atacar(pokemon)


class PokemonVenenoso(Pokemon):
    tipo = "Venenoso"

    def atacar(self, pokemon):
        print("{} lançou ENCHARCAR em {}".format(self, pokemon))
        return super().atacar(pokemon)


class PokemonVenenoso(Pokemon):
    tipo = "Venenoso"

    def atacar(self, pokemon):
        print("{} lançou CUSPE em {}".format(self, pokemon))
        return super().atacar(pokemon)


class PokemonPedra(Pokemon):
    tipo = "Pedra"

    def atacar(self, pokemon):
        print("{} lançou PEDREGULHO em {}".format(self, pokemon))
        return super().atacar(pokemon)


class PokemonInseto(Pokemon):
    tipo = "Inseto"

    def atacar(self, pokemon):
        print("{} lançou JOANINHA em {}".format(self, pokemon))
        return super().atacar(pokemon)
