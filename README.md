# Pokemon RPG 🎮

Um jogo de RPG baseado em Pokemon desenvolvido em Python, onde você pode capturar pokemons, batalhar contra inimigos e ganhar PokeCoins!

## 📋 Descrição

Este é um jogo de batalha Pokemon em modo texto onde você assume o papel de um treinador Pokemon. Você pode capturar diferentes tipos de Pokemon, batalhar contra inimigos e gerenciar seus PokeCoins.

## 🎯 Funcionalidades

- **Sistema de Captura**: Capture diferentes tipos de Pokemon
- **Sistema de Batalha**: Batalhe contra inimigos e seus Pokemon
- **Sistema de Dinheiro**: Ganhe ou perca PokeCoins nas batalhas
- **Tipos de Pokemon**: Elétrico, Fogo, Água, Planta, Inseto, Venenoso e Pedra
- **Sistema de Níveis**: Cada Pokemon tem seu próprio nível que afeta ataque e HP

## 🚀 Como Executar

### Pré-requisitos

- Python 3.x instalado no sistema

### Executando o Jogo

1. Clone ou baixe o repositório
2. Navegue até o diretório do projeto:
   ```bash
   cd pokemonRPG
   ```
3. Execute o arquivo principal:
   ```bash
   python3 main.py
   ```

## 🎮 Como Jogar

### Início do Jogo

Ao iniciar, você já possui um saldo inicial de **500 PokeCoins** e pode capturar seu primeiro Pokemon.

### Sistema de Batalha

Durante uma batalha:
1. Escolha um dos seus Pokemon disponíveis
2. Os Pokemon atacam alternadamente até que um seja derrotado
3. Cada ataque causa dano baseado no nível e tipo do Pokemon

### Ganhos e Perdas

- **Vitória**: Ganhe PokeCoins baseado no nível do Pokemon inimigo (nível × 23)
- **Derrota**: Perca PokeCoins baseado no nível do Pokemon inimigo (nível × 22)
- **Saldo Mínimo**: Seu saldo nunca ficará negativo, no mínimo chegará a 0

## 📂 Estrutura do Projeto

```
pokemonRPG/
├── main.py           # Arquivo principal do jogo
├── personagem.py     # Classes de Pessoa, Player e Inimigo
├── pokemon.py        # Classes dos Pokemon e seus tipos
└── README.md         # Este arquivo
```

## 🐛 Classes e Tipos de Pokemon

### Tipos Disponíveis:
- **Elétrico**: Ataque Raio do Trovão
- **Fogo**: Ataque Bola de Fogo
- **Água**: Ataque Encharcar
- **Planta**: Ataque Chicote de Vinha
- **Inseto**: Ataque Joaninha
- **Venenoso**: Ataque Cuspe
- **Pedra**: Ataque Pedregulho

### Exemplos de Pokemon:
- Pikachu (Elétrico)
- Charmander (Fogo)
- Squirtle (Água)
- Bulbasaur (Planta)
- Caterpie (Inseto)
- Ekans (Venenoso)
- Rhyhorn (Pedra)

## 💡 Exemplos de Uso

```python
# Criar um jogador
player = Player("Seu Nome")

# Capturar um Pokemon
player.capturar(PokemonEletrico("Pikachu"))

# Ver seus pokemons
player.mostraPokemons()

# Batalhar contra um inimigo
inimigo = Inimigo(nome="Gary", pokemons=[PokemonFogo("Charmander")])
player.batalhar(inimigo)

# Ver seu saldo
player.mostrarDinheiro()
```

## 🔧 Personalizações

Você pode modificar o arquivo `main.py` para:
- Alterar o nome do jogador
- Começar com Pokemon diferentes
- Criar inimigos com Pokemon específicos
- Ajustar valores de ganhos e perdas

## 📝 Notas

- O sistema de dano é parcialmente aleatório (até 20% de variação)
- Pokemon de nível mais alto têm mais HP e causam mais dano
- Inimigos podem ter de 1 a 6 Pokemon aleatórios se não forem especificados

## 🤝 Contribuições

Sinta-se livre para contribuir com melhorias, correções de bugs ou novas funcionalidades!

## 📄 Licença

Este é um projeto educacional livre para uso e modificação.
