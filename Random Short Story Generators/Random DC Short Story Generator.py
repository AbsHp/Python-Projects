import random

when = ['A long time ago', 'Once upon a time', 'Yesterday', 'Before you were born', 'In future']
who = ['Shazam', 'Batman', 'Superman', 'Joker', 'Wonder Woman', 'The Flash']
went = ['Arkham Asylum', 'Bat Cave', 'Gotham City', 'Manhattan', 'Atlantis', 'Paradise Island', 'Krypton']
what = ['to eat a lot of cakes', 'to find peace', 'to fight for justice', 'to steal icecream', 'to dance', 'to practice archery']

print(random.choice(when) + ', ' + random.choice(who) + ' went to ' + random.choice(went) + ' ' + random.choice(what) + '.')
