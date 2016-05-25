import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("g", help="name of input file")
parser.add_argument("t", help="number of trysses")

args = parser.parse_args()


t = int(args.t)

f = open(args.g)

x = 0
for line in f:
	x = x+1

g = {}

for j in range(0, x):
	g[j] = []

f = open(args.g)

for line in f:
	line2 = line.strip()
	spl = line.split()
	q = int(spl[0])
	w = int(spl[1])
	g[q].append(w)
	g[w].append(q)
	




u = {} 
z = g.copy() 

for k in range(0,x):
	for v in z[k]:
	
		for j in range(0, x):
			u[j] = 0


		for a in z[k]:
			if a != v:
				u[a] = u[a] + 1
		
		for a in z[v]:
			if a != k:
				u[a] = u[a] + 1
	
		counter = 0

		
		for p,o in u.items():
			if o==2 :
				counter = counter + 1
		
		
		if counter < t-2:
			g[k].remove(v)
			g[v].remove(k)
			

print(g)

os.system('pause')



