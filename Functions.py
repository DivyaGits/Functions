# list=[3, 4, 5,89,44]
# total=sum(list)
# print(total)


#Q. sum of the elements

#def my_function():
 #   print("hello i am function")

# it wont print output becuse we did not called function    

#Q.2

#def my_function():
 #   print("hello i am  from function")
#my_function() 

# now it will print out put

#Q.ARGUMENTS

#def my_function(fname):
 #   print(fname + "refsenes")
#my_function("emil")
#my_function("tobias")
#my_function("linus")   


#Q.4
# if we use 2 arguments place if we give one value : it will come TYPE ERROR.

#def my_function(name1,name2):                #INSIDE OF PARANTHASIS WE CALL ARGUMENTS
 #   print(name1 +" "+name2)
#my_function("emil")                        # it will shows error becuse we given one value only:  


#Q.5 using * symbol

#def my_function(*kids):                                 # using * symbol we can take multiple values as a tupule
 # print("The youngest child is " + kids[2])             # hear kids[2] means Linus like index we are using the values

#my_function("Emil", "Tobias", "Linus") 


# ARBITRARY Keyword Arguments **Keywords

# def my_function(**kid):
#     print("His last name is"+kid["lname"])
# my_function(fname="Tobias",lname="Resfsnes")


# Deafault parameter value:

# def my_function(country="Norway"):
#     print("I  am from"+country)
# my_function("sweden")    
# my_function("india")
# my_function()
# my_function("Brazil")


# passing a list as an Argument

# def my_function(food):
#     for i in food:
#         print(i)
# fruits=["apple","banana","cherry"] 
# my_function(fruits)
       

#Return values


# def my_function(x):
#     return 5*x
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))


# The pass statment:


#def my_function():
 #   pass



# def a(list):
#    a=sum(list)
#    print(a)
# list=[1,2,3,4,5]
# a(list)

     #or

# def sum(a,s):
#     sum=a+s
#     print(sum)
# sum(1,2)


#Q sor6t the list

# def fun(list):
#     a=sorted(list)
#     print(a)
# list=[2, 8, 4]  
# fun(list)  


#Q min value from the list


# def fun(list):
#      a=min(list)
#      print(a)
# list=[2, 8, 4]  
# fun(list)  


# Q. addition of two lists same positions:

# def fun (list1,list2):
#     i=0
#     d=[]
#     while i<len(list1):
#         a=list1[i]+list2[i]
#         d.append(a)
#         i=i+1
#         print(d)
# list1,list2=[2,3,4],[5,6,7]
# fun(list1,list2)


#Q Caliculate the Mathametical oparations

# def calculate(a,b):
#     print("The sum is:",a+b)
#     print("The difference is:",a-b)
#     print("The product is:",a*b)
# calculate(20,10)
# calculate(200,100)
# calculate(2000,1000)   
 

#Q print the given number is EVEN or ODD till N numbers:

# def fun(a):
#     i=1
#     while i<=a:
#         if i%2==0:
#             print(i,"Even")
#         else:
#             print(i,"Odd")
#         i=i+1
# fun(4)                


# Q max number of 3 numbers

# def fun(a):
#     i=0
#     max=0
#     while i<len(a):
#         if a[i]>max:
#             max=a[i]
#         i=i+1
#     print(max)        
# fun([5,6,7])    


# Q SUM OF GIVEN NUMBERS FROM TUPLE:


# def sum(*n):
#     result=0
#     for i in n:
#         result=result+i
#         print("the sum:",result)
# sum(0)
# sum(10,30)

         # AND

# def sum(name,*n):
#     result=0
#     for i in n:
#         result=result+i
#         print("the sum:",name,result)
# sum("divya",0)
# sum("rani",10,30)


# Q RECORD INFORMATION USING DICTIONARY:


# def fun(**x):
#     print("Record Information:")
#     for k,v in x.items():
#         print(k,"........",v)
# fun(name="divya",marks=90)
# fun(name="vinni",marks=80)        


# MAX of three numbers:

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



# sum of list:

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




  