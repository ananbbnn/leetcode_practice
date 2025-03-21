words =["n","a","o"]
left = 0
right = 2

def vowelStrings(words, left, right):
    vowel = ['a','e','i','o','u']
    vowel_check = []
    for i in range(left,right+1):
        if words[i][0] in vowel and words[i][-1] in vowel:
            vowel_check.append(1)
        else:
            vowel_check.append(0)
    print(vowel_check)
    
    output = sum(vowel_check)
    return output
    
    
print(vowelStrings(words, left, right))