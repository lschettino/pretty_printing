import sys
import numpy 

file = open("tecnologia.txt", "r")

M = int(input("Maximum line length: "))
print("\n")

# 1-index the list of words
A = [""]
for line in file: 
	A.extend(line.split(" "))
A = [s.replace('\n', '') for s in A]
#print(A)

size = len(A)
n = len(A) - 1 

# initialize list for final minimum penalty, line breaks  
D = [0]
line_breaks = [0]

# create array with partial sums 
partial = numpy.zeros(size)
for i in range(1,size):
	partial[i] = partial[i - 1] + len(A[i])

# initialize matrix with penalties between words i and j 
cost = [[]]

# populate cost array, 1-indexed   
for i in range(1,size): 
	row = [""]
	for j in range(i, size): 
		penalty = (M - j + i - (partial[j] - partial[i - 1])) ** 3
		if penalty < 0: 
			row.append(sys.maxsize)
		elif j == n - 1:
			row.append(0)
		else: 
			row.append(penalty)

	cost.append(row)

# base case -> D[1]  = A[1]
D.append(cost[1][1])

# apply the recursion 
for j in range(2, size):
	my_min = sys.maxsize, 0
	for i in range(1, j): 
		penalty = cost[j - i][i]
		if penalty == sys.maxsize:
			break 
		# else: 
		if D[j - i - 1] + penalty < my_min[0]:
				my_min = D[j - i - 1] + penalty, j - i

		if j == n: 
			if (cost[1][j] != sys.maxsize) and (D[j - i - 1] < my_min[0]):
				my_min = D[j - i - 1], 0

	D.append(my_min[0])
	line_breaks.append(my_min[1])

# function that neatly prints paragraph given list of line breaks
def neatly_print(breaks):
	b = breaks[-1]
	lst =[] 
	words = []
	if b != breaks[b]:
		lst.append(b)
	while b > 0: 
		lst.append(breaks[b])
		b = breaks[b] - 1 
	lst.reverse()
	for i in range(len(lst) - 1): 
		words.append(A[lst[i]:lst[i + 1]])
	words.append(A[lst[-1] : ])
	#print(words)
	if words[0][0] == '': 
		words[0].remove('')
	for i in range(len(words)):
		words[i] = ' '.join(words[i])
	print("\n".join(words))

neatly_print(line_breaks)
