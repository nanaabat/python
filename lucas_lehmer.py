	def lucas_leher(p):
2	    lucas_sequence = [4]
3
4	    #for loop
5	    for i in range(0, p - 2):
6	        n = (lucas_sequence[i] ** 2) % ((2 ** p) - 1)
7	        lucas_sequence.append(n)
8
9	    return lucas_sequence
10
11	print(lucas_leher(4))
