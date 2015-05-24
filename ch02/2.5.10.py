from timeit import Timer

MOD = 100000	# to calculate last 5 digits, compute everything mod this.

def fib_rec(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return ( fib_rec(n-1) + fib_rec(n-2) ) % MOD

def fib_iter(n):
	a,b = 0,1
	c = 0
	if n == 0:	return 0
	if n == 1:	return 1

	i = 2
	while i <= n:
		c = (a+b) % MOD
		a = b
		b = c
		i = i+1
	return c

print """This program will compute the maximum values of n, such that 
the nth Fibonacci number is computed under 1 minute, using 
both - recursive and iterative algorithms."""

n = 0
t = 0
while t < 60:
	t = Timer("fib_rec(n)", "from __main__ import fib_rec, n").timeit(1)
	print "Time for n=%d is %fs\n" % (n, t)
	n = n+1

print "*******************************************************\n"
print "Max n using recursive algorithm: %d\n" % (n-1,)
print "*******************************************************\n"

n = 1
t = 0
while t < 60:
	t = Timer("fib_iter(n)", "from __main__ import fib_iter, n").timeit(1)
	print "Time for n=%d is %fs\n" % (n, t)
	n = 2*n 	# used doubling, because here the final answer will be huge.
				# no point in incrementing n by 1. It'll be terribly slow!

print "*******************************************************\n"
print "Max n using iterative algorithm: %d\n" % (n-1,)
print "*******************************************************\n"