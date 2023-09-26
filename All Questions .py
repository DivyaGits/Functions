#Q.2# MAX of three numbers:

# def f1(*a):
#     i=0
#     max=0
#     while i<len(a):
#         if a[i]>=max:
#             max=a[i]
#         i=i+1
#     print(max) 
# f1(7,8,9)      

         #(or)

# def f1(*a):
#     print(max(a))  
# f1(7,8,9)           



#Q.3# sum of list:

# def f1(*a):
#     i=0
#     sum=0
#     while i<len(a):
#         sum=sum+a[i]
#         i=i+1
#     print(sum)   
# f1(8,2,3,0,7)
        
         #(OR)

# def f1(*a):
#     print(sum(a))
# f1(8,2,3,0,7)    




  #Q.4  REVERSE the string:

# def f1(st):
#     print((st[::-1]))
# f1("1234abcd")    

# Q.5 print the unique questions from the list:


# def f1(a):
#     list=[]
#     for i in (a):
#         if i  not in list:
#             list.append(i)
#     print([list])    
# f1([1,2,3,3,4,2])   


# duplicat and orginal list:


# def f1(a):
#     list=[]
#     org=[]
#     for i in (a):
#         if i  not in list:
#             list.append(i)
#         elif i not in org:
#             org.append(i)    
#     print([list],[org])    
# f1([1,2,3,3,4,2])                     


#Q .6 EVEN numbers:


# def f1(a):
#     i=0
#     eve=[]
#     while i<len(a):
#         if a[i]%2==0:
#             eve.append(a[i])   
#         i=i+1
#     print(eve)
# f1([2,1,4,5,6])   


#Q.7 using conditions :

# def fun(bmi):
#     if bmi<=18.5:
#         print("Underweight")
#     elif bmi<=25.0:
#         print("Normal") 
#     elif bmi<=30.0:
#         print("Over weight")
#     else:
#         print("obese")  
# fun(bmi=int(input("enter the bmi:")))   


#Q.1 COUNT THE NUMBER OF STRINGS THAT FROM GIVEN LENGTH:

# def fun(strings):
#     count = 0
#     for i in strings:
#         if len(i) >= 2 and i[0] == i[-1]:
#             count += 1
#     return count

# my_list= ["abc", "xyz", "aba", "1221"]
# result = fun(my_list)
# print("Number of strings meeting the criteria:", result)


# Q.8 COUNT THE UPPER CASE ARE LOWER CSE LETTERS FROM GIVEN STRING:


# def count(string):
#     upper_count=0
#     lower_count=0
#     for char in string:
#         if char.isupper():
#             upper_count+=1
#         elif char.islower():
#             lower_count+=1
#     print("upper characters is %d and lower characters is %d"%(upper_count,lower_count))  
# temp=input("enter a string:")    
# count(temp)             


#Q .11  implement a function named genarate range(mi,max,step)which takes three arguments and genarates a range of integers from min to max with step.the the first integer is the minimum value,the second integer is the maximum range and third is the stepin python how to write code



def genarate(min,max,step):
    list=[]
    x=min
    while min<=max:
       if step>0:
        list=list+[x]
        x=min+step
       min=x
    print(list)    
genarate(1,10,3)
