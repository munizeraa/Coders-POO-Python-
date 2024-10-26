# Classe Pai
class DefaultCharacter:
    def __init__(self, name, life, strength, atk, defense):
        self.name = name
        self.life = life
        self.strength = strength
        self.atk = atk
        self.defense = defense

# Classe Filha de DefaultCharacter, portanto ela herda de DefaultCharacter
class Sorcerer(DefaultCharacter):
    def __init__(self, elemental_power, name, life, strength, atk, defense):
        super().__init__(name, life, strength, atk, defense)
        self.elemental_power = elemental_power

# Classe Filha de DefaultCharacter, portanto ela herda de DefaultCharacter
class Deprived(DefaultCharacter):
    def __init__(self, name, life, strength, atk, defense, bolao_da_mega_sena):
        super().__init__(name, life, strength, atk, defense)
        self.bolao_da_mega_sena = bolao_da_mega_sena

if __name__ == '__main__':
    amaral = DefaultCharacter("Amaral", 10, 10, 10, 10)

    mago_doido = Sorcerer("Magic", "Harry", 12, 12, 12, 12)
    mago_doido.name = "Jonas"

    deprived = Deprived("Xonas", 11, 11, 11, 11, True)

    print(deprived.name)
    print(amaral.name)
    print(mago_doido.name)