pos = -1


def search(lst, n):
    l=0
    u = len(lst)-1

    while l <= u:
        mid = (l+u) // 2
        if lst[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if lst[mid] < n:
                l = mid+1
            else:
                u = mid-1
    return False

lst = [4, 7, 8, 12, 45, 99]
n = 1

if search(lst, n):
    print("Found at", pos+1)
else:
    print("Not Found")
