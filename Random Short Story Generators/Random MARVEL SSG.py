import random

when = ['A long time ago', 'Once upon a time', 'Yesterday', 'Before you were born', 'In future', 'Before Thanos Snap']
who = ['Ironman', 'Captain America', 'Black Widow', 'Hawkeye', 'Spiderman', 'Winter Soldier', 'Dr. Strange', 'Thanos', 'Ultron', 'Shang Chi', 'Hulk', 'Thor', 'Loki', 'Daredevil', 'Star Lord', 'Deadpool']
went = ['Titan', 'the Sanctum Sanctorum', 'Asgard', 'the Stark Tower', 'the Avengers Tower', 'SHIELD Helicarrier', 'the Avengers HQ', 'Eternity', 'Wakanda', 'the Dark Dimension', 'Earth 838', 'the Hydra Base', 'the TVA', "the Hell's Kitchen", 'Vormir', 'KnowWhere', 'Madripoor', 'the Nexus', 'the Void', 'Savage Land', 'Sokovia', 'the past']
what = ['to eat a lot of cakes', 'to find peace', 'to fight for justice', 'to steal icecream', 'to dance', 'to practice archery', 'to find infinity stones', 'to die', 'to know the truth', 'to kill Hitler']

print(random.choice(when) + ', ' + random.choice(who) + ' went to ' + random.choice(went) + ' ' + random.choice(what) + '.')
