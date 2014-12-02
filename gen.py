# http://www.boolsat.com/

from itertools import product
from math import sqrt
s = lambda x: str(x)


def generate(N, with_sectors=False, q=None):

	numbs = xrange(1, N+1)
	st = ''

	for x, a, v, b in product(numbs, numbs, numbs, numbs):
		if a > b: 
			st += ' '.join(['-'+s(x*100+a*10+v), '-'+s(x*100+b*10+v), '0']) + ' '

	for x, a, v, b in product(numbs, numbs, numbs, numbs):
		if a > b:
			st += ' '.join(['-'+s(a*100+x*10+v), '-'+s(b*100 + x*10+v), '0']) + ' '

	for x, y, v, u in product(numbs, numbs, numbs, numbs):
		if v > u:
			st += ' '.join(['-'+s(100*x+10*y+v), '-'+s(100*x+10*y+u), '0']) + ' '

	for x in numbs:
		for y in numbs:
			for n in numbs:
				st += s(100*x+10*y+n) + ' '
			st += "0 "

	k = 0
	if with_sectors:
		for x, y, u, v, n in product(numbs, numbs, numbs, numbs, numbs):
			#print x//q == True, x, q
			if (x>u or y>v) and ((x-1)//q == (u-1)//q) and (((y-1)//q) == ((v-1)//q)):
				print x, y, "|", u, v, n

				k += 1
				st += ' '.join(['-'+s(x*100+y*10+n), '-'+s(u*100 + v*10+n), '0']) + ' '

	print k

	st += ' 111 0 222 0 333 444 0'
	return st


def save(strs, filename='default.txt'):

	with open(filename, 'w') as f:
		f.write(strs)
		f.close()


if __name__ == '__main__':

	try: 
		N = int(raw_input())
	except:
		N = 3

	if N in [4, 9]:
		sq = generate(N, with_sectors=True, q=sqrt(N))
	else:
		sq = generate(N)
	
	save(sq)


