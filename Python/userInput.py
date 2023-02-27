a=10
b=20
sum=a+b
print("sum of",a,"and",b, "is",sum)
print(f"sum of {a} and {b} is {sum}")
print("sum of {} and {} is {}".format(a,b,sum))
print("sum of {1} and {0} is {2}".format(a,b,sum))


# print("Enter a no: ")
# a=input()

# print("Enter a no: ")
# b=input()

# print("First no:" ,a , type(a))
# print("Second no:",b,type(b))

# print("Sum: ",a+b)

# return type of input() is string


'''
TypeCasting: 

int()
str()
bool()
float()

'''

print("Enter a no: ")
a=int(input())

b=int(input("Enter a no: "))

print("First no:" ,a , type(a))
print("Second no:",b,type(b))

print("Sum: ",a+b)