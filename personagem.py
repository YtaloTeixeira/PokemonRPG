from pokemon import *

class Pessoa:
    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = "Anônimo"

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostraPokemons(self):
        if self.pokemons:
            print("Pokemons de {}: ".format(self))
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print("{} não tem pokemons!".format(self))


class Player(Pessoa):
    tipo = "Player"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou {}".format(self, pokemon))

class Inimigo(Pessoa):
    tipo = "Inimigo"

eu = Player(nome="Ytalo")

pokemonSelvagem = PokemonFogo("Charmander")
eu.mostraPokemons()
eu.capturar(pokemonSelvagem)
eu.mostraPokemons()
