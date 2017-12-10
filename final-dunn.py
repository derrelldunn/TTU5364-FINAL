#Derrell Dunn
#Math 5364
#Fall 2017

import math

def testevaluate(x_value):
    #function_value = float(x_value*x_value*x_value)-3*(float(x_value*x_value)) + 6
    function_value = (math.pow(x_value,3))-(3*math.pow(x_value,2))+(6)
    #print("f(n)={}".format(function_value))
    return function_value


def expevaluate(ex_value):
    efunction_value = math.exp(-(math.pow(ex_value,2)))
    return efunction_value


summation = 0

limit_a = input("What is the lower limit a?: ")
limit_b = input("What is the upper limit b?: ")
partition_num = input("How many partitions for the calculation to use?: ")
print ("The limit a is {} The limit b is {} the number of partitions are {}".format(limit_a, limit_b, partition_num))
#check for valid data
assert isinstance(partition_num, int)
assert limit_b > limit_a

summation = 0
delta = float(limit_b - limit_a)/float(partition_num)
step = int(delta)
for index in range(0, partition_num, 1):
    summation += float(delta * expevaluate(limit_a + (delta * index) ) )
print("Left Summation x = {}, f(n) = {}, summation={:2.10f}".format(limit_a + (delta * index),expevaluate(limit_a + (delta * index) ),summation))

summation = 0
for index in range(1, partition_num+1, 1):
    summation += float(delta * expevaluate(limit_a + (delta * index) ) )
print("Right Summation x = {}, f(n)= {}, summation={:2.10f}".format(limit_a + (delta * index),expevaluate(limit_a + (delta * index) ) ,summation))

summation = 0
for index in range(0, partition_num, 1):
    summation += float(delta * expevaluate(limit_a + delta * (index+0.5)))
print("Midpoint Summation x = {}, f(n) = {}, summation={:2.10f}".format(limit_a + delta * (index+ 0.5),expevaluate(limit_a + delta * (index+0.5)), summation))

