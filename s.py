N = 3

numbs = xrange(1, N+1)

st = ''

for x in numbs:
	for a in numbs:
		for v in numbs:
			for b in numbs:
				if a >= b:
					continue 
	
				st += ' '.join(['-'+str(x*100+a*10+v), '-'+str(x*100+b*10+v), '0']) + ''

for x in numbs:
	for a in numbs:
		for v in numbs:
			for b in numbs:
				if a >= b:
					continue
				st += ' '.join(['-'+str(a*100+x*10+v), '-'+str(b*100 + x*10+v), '0']) + ''

for x in numbs:
	for y in numbs:
		for v in numbs:
			for u in numbs:
				if v >= u:
					continue

				st += ' '.join(['-'+str(100*x+10*y+v), '-'+str(100*x+10*y+u), ' ']) + ''




st += '111 0222 0333 0'






f = open('123.txt', 'w')
f.write(st)
f.close()



