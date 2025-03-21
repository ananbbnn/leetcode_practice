x = 121

def isPalindrome(x):
    sx = str(x)
    if sx != sx[::-1]:
        return False
    else:
        return True
    

print(isPalindrome(x))