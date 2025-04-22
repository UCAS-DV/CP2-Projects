
class pokemon:
    def __init__(self, name, species, hp, damage):
        self.name = name
        self.species = species
        self.hp = hp
        self.damage = damage

    def __str__(self):
        return f'Name: {self.name} \nSpecies: {self.species} \nHP: {self.hp} \nDMG: {self.damage}'

    def battle(self, opponent):
        while self.hp > 0 and opponent.hp > 0:
            opponent.hp -= self.damage
            print(f'{self.name} attacked {opponent.name} for {self.damage} HP {opponent.name} now has {opponent.hp} HP')
            if opponent.hp > 0:
                self.hp -= opponent.damage
                print(f'{opponent.name} attacked {self.name} for {opponent.damage} HP {self.name} now has {self.hp} HP')
                if self.hp <= 0:     
                    print(f'{self.name} has been knocked out. {opponent.name} won the battle')
            else:
                print(f'{opponent.name} has been knocked out. {self.name} won the battle')
                
bob = pokemon('Mr. Bob', ' Charizard', 300, 95)
fluffy = pokemon('Fluffy', 'Pikachu', 280, 110)

print(bob)
print(fluffy)

bob.battle(fluffy)