def validParentheses(s):
    combo = ['()','[]','{}']
    for j in range(len(s)//2+1):
        for i in combo:
            s = s.replace(i,'')
    if s == '':
        return True
    else:
        return False


















s = "(("
print('ans:',validParentheses(s))