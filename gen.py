# http://www.boolsat.com/

from itertools import product


def generate(N):
	numbs = xrange(1, N+1)
	st = ''

	for x, a, v, b in product(numbs, numbs, numbs, numbs):
		if a > b: 
			st += ' '.join(['-'+str(x*100+a*10+v), '-'+str(x*100+b*10+v), '0']) + ' '

	for x, a, v, b in product(numbs, numbs, numbs, numbs):
		if a > b:
			st += ' '.join(['-'+str(a*100+x*10+v), '-'+str(b*100 + x*10+v), '0']) + ' '

	for x, y, v, u in product(numbs, numbs, numbs, numbs):
		if v > u:
			st += ' '.join(['-'+str(100*x+10*y+v), '-'+str(100*x+10*y+u), '0']) + ' '

	for x in numbs:
		for y in numbs:
			for n in numbs:
				st += str(100*x+10*y+n) + ' '
			st += "0 "

	st += ' 111 0 222 0 333 0'
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

	sq = generate(N)
	save(sq)


