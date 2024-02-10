# Variables and Data Types 

a = complex(8,2) # for complex number
b = True         # for Boolean data types
c = "Harry"      # Strings
d = None         # None 

print(a,b,c,d)

print(type(a))
print(type(b))
print(type(c))
print(type(d))

l1 = [8,2,3,[-4,5],["apple", "samsung","intel"]]  # Sequenced data type, ordered and mutable 
print(l1)
# Note: Concatination is only done in case of Same data types.

t1 = (8,5,5,6,2,("parrot","sparrow"),("Lion","tiger"))   # Sequenced data type, ordered and immutable
print(t1)

dict1 = {
    "name":"Shayar", "age":23, "canVote": True  # mapped data type : dictionary, contains key:value pair
}
print(dict1)