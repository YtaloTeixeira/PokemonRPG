class Pokemon:

    def __init__(self, especie, tipo, nome=None, lvl=1):
        self.especie = especie
        self.tipo = tipo
        self.lvl = lvl
        if nome:
            self.nome = nome
        else:
            self.nome = especie
        

    def __str__(self):
        return "{} LVL: {}".format(self.especie, self.lvl)
    
    def atacar(self, pokemon):
        print("{} atacou {}!".format(self.especie, pokemon.especie))
    

class PokemonEletrico(Pokemon):
    def atacar(self, pokemon):
        print("{} lançou RAIO DO TROVÃO em {}".format(self, pokemon))

    def choque(self):
        print("CHOQUE")




meuPokemon = PokemonEletrico("Pikachu", "Elétrico")
pokemonAmigo = Pokemon("Charmander", "Fogo")

meuPokemon.choque()
pokemonAmigo.atacar(meuPokemon)


    