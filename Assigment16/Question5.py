#Write a python program to check if all items in the tuple are the same
A = ['python', 'python', 'python', 'python']
if([A[0]]*len(A) == A):
    print("same")
else:
    print("Not same")