from pokemon import *
from personagem import *

def escolhaInicial(player):
    print("Olá {}! Escolha o Pokemon que irá te acompanhar nesta jornada!".format(player))

    pikachu = PokemonEletrico("Pikachu", lvl=1)
    charmander = PokemonFogo("Charmander", lvl=1)
    squirtle = PokemonAgua("Squitle", lvl=1)

    
    print("1 - ", pikachu)
    print("2 - ", charmander)
    print("3 - ", squirtle)

    while True:
        escolha = input("Escolha seu Pokemon: ")

        if escolha == '1':
            player.capturar(pikachu)
            break
        elif escolha == '2':
            player.capturar(charmander)
            break
        elif escolha == '3':
            player.capturar(squirtle)
            break
        else:
            print("Escolhar uma opção válida!")

