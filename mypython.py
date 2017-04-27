import random
import string

for i in range(3):
	word = "".join(random.choice(string.ascii_lowercase) for x in range(10))
	word = word + '\n'
	f = open("file{0}.dat".format(i), 'w')
	f.write(word)
	print(word)

x = round((random.random()*42) +1)
y = round((random.random()*42) +1)
total = x*y
print(x)    
print(y)    
print(total)
