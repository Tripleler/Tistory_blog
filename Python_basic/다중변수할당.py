animal = ['waterdeer', 'wildboar', 'goral']
rb1, rb2, rb3 = animal
print(rb1, rb2, rb3)
print(globals())

animal = ['waterdeer', 'wildboar', 'goral', 'cat', 'dog', 'bird']
for i in range(1, len(animal) + 1):
    globals()[f'rb{i}'] = animal[i-1]
print(rb1, rb2, rb3, rb4, rb5, rb6)

exec(f'print(animal)')

for i, name in enumerate(animal, start=1):
    exec(f'rb{i} = name')
print(rb1, rb2, rb3, rb4, rb5, rb6)