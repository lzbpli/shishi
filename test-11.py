f1 = 1
f2 = 1
for i in range(1,21):
	print '%121d %121d' % (f1,f2)
	if (i % 3) == 0:
		print ''
	f1 = f1 + f2
	f2 = f1 + f2


