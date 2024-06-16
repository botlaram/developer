# A Simple Python program to demonstrate working of yield
# A Python generator is a special type of iterator that generates values on-the-fly, allowing you to iterate over potentially large sequences of data without needing to store the entire sequence in memory.
# A generator function that yields 1 for the first time, 2 second time and 3 third time


def simpleGeneratorFun():
	yield 1
	yield 2
	yield 3


# Driver code to check above generator function
for value in simpleGeneratorFun():
	print(value)

