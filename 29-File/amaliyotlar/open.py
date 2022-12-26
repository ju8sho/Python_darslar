
with open('kino.txt') as kino:
    kino = kino.read()
print(kino)

with open('kino.txt') as file:
    file = file.readlines()

print(file)
kino = [kino.rstrip() for kino in file]
print(kino)
