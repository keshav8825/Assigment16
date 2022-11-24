''' Write a python program to print the value 20 from given nested tuple
tuple1 = ("Python", [10, 20, 30], (2, 4, 16))'''

tuple1 = ("python",[10,20,30],(2,4,16))
element_to_find=10
for i in range(len(tuple1)):
    if type(tuple1[i]) == list:
        for m in range(len(tuple1[i])):
            if tuple1[i][m] == element_to_find:
                print(tuple1[i][m],":",m)
print( )
