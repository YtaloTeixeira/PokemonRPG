class Pokemon:

    def __init__(self, especie, nome=None, lvl=1):
        self.especie = especie
        self.lvl = lvl
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
    

