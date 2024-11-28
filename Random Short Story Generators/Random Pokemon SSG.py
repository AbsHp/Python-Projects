import random

when = ['A long time ago', 'Once upon a time', 'Yesterday', 'Before you were born', 'Sometime in the future']
who = ['Ash', 'Brock', 'Red', 'Blue', 'Misty', 'Green', 'Pikachu', 'Team Rocket', 'Koga', 'Giovanni', 'Sabrina', 'Prof. Oak', 'Ritchie', 'Gary', 'Tracy', 'Lt. Surge', 'Erika', 'Blaine']
went = ['Pallet Town', 'Viridian City', 'Cerulean City', 'Indigo Plateau', 'Elements Islands', 'Fuchsia City', 'Saffron City', 'Pewter City', 'Lavender Town', 'Vermillion City', 'Celadon City', 'Cinnabar Island', 'Cerulaean Cave', 'Mt. Moon', 'Seafoam Islands']
what = ['to eat a lot of cakes', 'to find peace', 'to fight for justice', 'to steal icecream', 'to dance', 'to practice archery', 'to fight gym battles', 'to die', 'to know the truth', 'to win the Pokemon League', 'to collect souls', 'to find MewTwo']

print(random.choice(when) + ', ' + random.choice(who) + ' went to ' + random.choice(went) + ' ' + random.choice(what) + '.')