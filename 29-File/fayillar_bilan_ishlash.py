with open('pi.txt') as file:
	pi = file.read()

print(pi)
print(type(pi))

pi = pi.rstrip()
pi = pi.replace('\n','')
pi = float(pi)

print(pi)


filenomi = 'data/pi.txt'
with open(filenomi) as file:
    pi = file.read()
    
print(pi)  




