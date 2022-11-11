import numpy
num = int(input("Enter number "))
x=numpy.prod([i for i in range(1,num+1)])
print(x)