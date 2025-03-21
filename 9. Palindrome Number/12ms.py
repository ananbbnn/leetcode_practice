x = -121

def isPalindrome(x):
    start = 0
    end = -1
    sx = str(x)
    l = len(sx)//2
    for i in range(l):
        if sx[start] != sx[end]:
            return False
        else:
            start += 1
            end -= 1
    return True

    
print(isPalindrome(x))