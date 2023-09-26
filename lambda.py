# Q
# lambda is a keyword we can use without using def it wont give any error
 
# s=lambda n:n*n
# print(s(4))
# print(s(10))

# Q. USING some functions 
# filter()
# map()
# reduce()

# 1.filter() if condition is true then it will count the valuse from the sequence


# l=[10,20,30,40,15]
# l1=list(filter(lambda x:x%2==0,l))
# print(l1)
# l2=list(filter(lambda x:x%2!=0,l))
# print(l2)

# 2. map() for applying some oparations ,and both sequences contain same values or length

l=[10,20,30]
l1=[10,20]
l2=list(map(lambda x,y:x+y,l,l1))
print(l2)