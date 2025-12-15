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

    def __init__(self, nome=None, pokemons=[], dinheiro=500):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons
        self.dinheiro = dinheiro

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
        if self.pokemons:
            escolha = random.choice(self.pokemons)
            print("{} escolheu {}".format(self, escolha))
            return escolha
        else:
            print("{} não tem pokemons para escolher!".format(self))


class Player(Pessoa):
    tipo = "Player"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou {}".format(self, pokemon))

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

    def mostrarDinheiro(self):
        print("Saldo: {}".format(self.dinheiro))

    def ganharDinheiro(self, quantia):
        self.dinheiro += quantia
        print("Você ganhou: {} PokeCoins".format(quantia))
        self.mostrarDinheiro()
    
    def perderDinheiro(self, quantia):
        if self.dinheiro >= quantia:
            self.dinheiro -= quantia
            print("Você perdeu: {} PokeCoins".format(quantia))
        else:
            print("Você perdeu: {} PokeCoins".format(quantia))
            self.dinheiro = 0
        self.mostrarDinheiro()

    def batalhar(self, pessoa):
        print("{} iniciou uma batalha contra {}".format(self, pessoa))

        pessoa.mostraPokemons()
        pokemonInimigo = pessoa.escolherPokemon()

        meuPokemon = self.escolherPokemon()

        if meuPokemon and pokemonInimigo:
            while True:
                vitoria = meuPokemon.atacar(pokemonInimigo)
                if vitoria:
                    print("{} venceu a batalha!".format(self))
                    self.ganharDinheiro(pokemonInimigo.lvl * 23)
                    break

                vitoriaInimiga = pokemonInimigo.atacar(meuPokemon)
                if vitoriaInimiga:
                    print("{} venceu a batalha!".format(pessoa))
                    self.perderDinheiro(pokemonInimigo.lvl * 22)
                    break
        else:
            print("Batalha não pode ser iniciada!")


class Inimigo(Pessoa):
    tipo = "Inimigo"

    def __init__(self, nome=None, pokemons=[]):

        if not pokemons:
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choice(POKEMONS))

        super().__init__(nome=None, pokemons=pokemons)
