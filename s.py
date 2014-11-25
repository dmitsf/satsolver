
try:
	N = int(raw_input())
except:	
	N = 3	


numbs = xrange(1, N+1)

st = ''

i = 0
for x in numbs:
	for a in numbs:
		for v in numbs:
			for b in numbs:
				if a > b: 
					st += ' '.join(['-'+str(x*100+a*10+v), '-'+str(x*100+b*10+v), '0']) + ' '
					i += 1

for x in numbs:
	for a in numbs:
		for v in numbs:
			for b in numbs:
				if a > b:
					st += ' '.join(['-'+str(a*100+x*10+v), '-'+str(b*100 + x*10+v), '0']) + ' '
					i += 1

for x in numbs:
	for y in numbs:
		for v in numbs:
			for u in numbs:
				if v > u:
				#	continue
					st += ' '.join(['-'+str(100*x+10*y+v), '-'+str(100*x+10*y+u), '0']) + ' '
					i += 1

for x in numbs:
	for y in numbs:
		for n in numbs:
			st += str(100*x+10*y+n) + ' '		

		st += "0 "


#for x in numbs:
#	for y in numbs:
#		st += str(10*x + y) + ' 0 '


st += ' 111 0 222 0 333 0'






f = open('123.txt', 'w')
f.write(st)
f.close()



