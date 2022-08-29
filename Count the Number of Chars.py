a = set()
b = set()
# Adding elements to a
for i in range(1, 6): 
   a.add(i) 
# Adding elements to b
for i in range(3, 8): 
   b.add(i) 
print("a = ", a) 
print("b = ", b) 
print("\n") 
 
# LIST OPERATION OF INSERTION AND DELETION

list1, list2 = [143, 'xyz'], [136, 'abc']
list1.append(list2)   # list2 is child of list1,making sub list
 
print(list1)

list1.insert(3,2010)
list1.insert(4,'smith')
print(list1)
 
#TUPLE OPERATION OF INSERTION AND DELETION
tup1=('abc','xyz',100,'1pqr',"sandya","arati","nec")
 
tup2=(1,2,3,4)
 
tup3="a","b","c","d"
tup2=tup2+(5,)		# inserting one more element to tuple
print(tup1)
print(tup2)
print(tup3)
del tup1		# entire tuple has to be deleted
 

 
# DICTIONARY OPERATION
 
k={"name":'arati','age':20} # k is dictionary, contains keys and values
k.clear()		# entire dictionary is cleared
 
a={'name':'Xb','age':25};
 
c=a.copy()	# copy is built in function of dictionary
 
print ('\n')
 
print(c)
 
z=('name','age') # tuple values taken and made as keys in dict
 
dict=dict.fromkeys(z)	
print(dict)
 
dict={'name':'arati','age':20}
 
dict1={'salary':25000}
 
dict.update(dict1) #dict1 values appended with dict values
print(dict)
