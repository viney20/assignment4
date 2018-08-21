import copy as c
#Q.1- Reverse the whole list using list methods.
lst=[1,2,3,4,5]
lst.reverse()
print(lst)
#Q.2- Print all the uppercase letters from a string.
lst=['a','b','A','B']
for i in range(0,len(lst)):
               if lst[i].isupper()==True:
                       print(lst[i])

#Q.3- Split the user input on comma's and store the values in a list as integers.
lst=[]
b=0
strr=input("enter only numbers")
strr1=strr.split(',')
for i in range(0,len(strr1)):
    b=int(strr1[i])
    lst.append(b)
print("list:",lst)

#Q.4- Check whether a string is palindromic or not.
strr=input("enter ur string")
strr1=strr[::-1]
if strr==strr1:
    print("string is palindromic")
else:
    print("string is not palindromic")

#Q.5- Make a deepcopy of a list 
lst=[1,2,[3,4],5]
lst1=c.deepcopy(lst)
lst1[2][0] = 7
print(lst)
print(lst1)

