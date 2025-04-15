def validParentheses(s):
    if len(s)%2 != 0:
        return False
    close = [')',']','}']
    count = 0
    open_count = 0
    close_count = 0
    skip = 0

    for i,string in enumerate(s):
        count += 1
        if string in close:
            close_count += 1
            if skip <=0:
                skip = count-1
                start = i - (count-1)
                stop = i
                print('1:'+ s[start:stop])
                print('2:'+ s[stop +(count-2):start + (count-2):-1])
                print('skip:',skip)
                open_s=s[start:stop]
                close_s=s[stop +(count-2):start + (count-2):-1]
                close_s = close_s.replace(')','(').replace('}','{').replace(']','[')
                if open_s != close_s or open_s == '':
                    return False
                count = 0
        else:
            open_count += 1
        skip -= 1
    if close_count == open_count:
        return True
    else:
        return False



















s = "(([]){})"
print(validParentheses(s))