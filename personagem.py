import random 
from pokemon import *

NOMES = [
    "Tião Carreiro",
    "Pardinho",
    "Rio Negro", 
    "Solimões",
    "João Carreiro",
    "Capataz", 
    "Jads", 
    "Jadson", 
    "Bruno", 
    "Marrone",
    "Milionário",
    "José Rico",
]

POKEMONS = [
    PokemonPlanta("Bullbasaur"),
    PokemonFogo("Charmander"),
    PokemonAgua("Squirtle"), 
    PokemonInseto("Caterpie"),
    PokemonEletrico("Pikachu"),
    PokemonVenenoso("Ekans"),
    PokemonPedra("Rhyhorn")
]

class Pessoa:

    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostraPokemons(self):
        if self.pokemons:
            print("Pokemons de {}: ".format(self))
            for i, pokemon in enumerate(self.pokemons):
                print("{} - {}".format(i, pokemon))
        else:
            print("{} não tem pokemons!".format(self))

    def escolherPokemon(self):
        self.mostraPokemons()

        if self.pokemons:
            while True:
                escolher = input("Escolha seu Pokemon: ")
                try:
                    escolher = int(escolher)
                    escolha = self.pokemons[escolher]
                    print("{} eu escolho você!".format(escolha))
                    return escolha
                except:
                    print("Escolha inválida")
        else:
            print("{} não tem pokemons para escolher!".format(self))

    def batalhar(self, pessoa):
        print("{} iniciou uma batalha contra {}".format(self, pessoa))

        pessoa.mostraPokemons()
        pessoa.escolherPokemon()

        self.escolherPokemon()   


class Player(Pessoa):
    tipo = "Player"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou {}".format(self, pokemon))


class Inimigo(Pessoa):
    tipo = "Inimigo"

    def __init__(self, nome=None, pokemons=[]):

        if not pokemons:
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choice(POKEMONS))

        super().__init__(nome=None, pokemons=pokemons)

    def escolherPokemon(self):
        if self.pokemons:
            escolha = random.choice(self.pokemons)
            print("{} escolheu {}".format(self, escolha))
            return escolha
        else:
            print("{} não tem pokemons para escolher!".format(self))
