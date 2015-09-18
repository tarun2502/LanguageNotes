beatles = [['John', 1943], ['Paul', 1942], ['George', 1943],['Rigo', 1940]]
print beatles
print beatles[0]
print beatles[0][1]

# Mutation in the list
p = ['H','E', 'L', 'L', 'O' ]
p[0] = 'Y'
print p
# Aliasing 
q = p # Now q also refers to p
q[-1] = "!" # Now p is also changed.
print q

# function values are passed as reference.
spy = [0,0,7]
def replace_spy(p): # Here p is refering to the same spy
    p[2] = p[2] + 1
replace_spy(spy)
print spy #[0, 0, 8]

a = 4
def replace_n(n):
    n = n + 1 # now n refers to new value i.e. 5

replace_n(a)
print a # A is not changed to 5

#list append
list1 = ["Tarun", "Sandhya"]
list1.append("Atharva")
print list1 # ["Tarun", "Sandhya", "Atharva"]

#Concatenation operation for list
list1 = [0, 1]
list2 = [3,4]
list3 = list1 + list2
print list3 # Lit 1 and 2 are not affected., [0, 1, 3, 4]

#Length of list
print len(list3) # 4
print len(['a', ['b',['c']]]) #2
print len("Udacity") #7

#Good one
p = [1, 2]
q = [3, 4]

p.append(q) # Remebmebr we are appending a new element to p .
print p, len(p) # [1, 2,[3, 4]], 3
q[1] = [5]
print p # [1, 2, [3, 5]] as q was added as a refernce to p

#Loops on lists
p = [1, 2, 3]
def pint_all_elements(p):
    i = 0
    while i < len(p):
        print p[i]
        i+=1

pint_all_elements(p)

#For Loop
# for <name> in <list>:
#   <Block>

def sum_list(l):
    sum = 0
    for elem in l:
        sum += elem
    return sum

print sum_list(p)

def is_Udacity(list1):
    count = 0
    for x in list1:
        assert isinstance(x, str)
        if x.startswith("U"):
            count = count + 1
    return count

#To give the postion of element found
def find_element(list1, elem_to_find):
    index = 0
    for elem in elem_to_find:
        if elem == elem_to_find:
            return index
        index += 1
    if index == len(list1):
        retrun -1

# index => gives location of first match otherwise gives error.
# <list>.index(<value>) => returns positon of first mathc or error
print p.index(2) # 2

# in => <value> in <list> => true or false
print 3 in p #true

# not in => <value> not in <list> => true or false
print 4 not in p #=> true

#Another way to write above functions.
def find_element2(list1, elem_to_find):
    if elem_to_find not in list1:
        return -1
    return list1.index(elem_to_find)

# Union of two lists.
def union(p, q):
    assert isinstance(a, list)
    for elem in q:
        if elem not in p:
            p.append(elem)
#No need to return as it modifies the original list.


