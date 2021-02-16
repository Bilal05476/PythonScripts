pos = -1
def search(lst, n):
    i = 0
    while i < len(lst):
        if lst[i] == n:
            globals()['pos'] = i
            return True
        i += 1
        
    return False

lst = [5,4,9,7,8,2]
n = 9

if search(lst, n):
    print("Found at", pos)
else:
    print("Not Found")