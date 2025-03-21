
s = "abbcccddddeeeeedcba"
count=0
output=0
last_word=''
for word in s:
    if word==last_word:
        count+=1
        output = count if count > output else output
    else:
        count=0
    last_word = word
print(output+1)



