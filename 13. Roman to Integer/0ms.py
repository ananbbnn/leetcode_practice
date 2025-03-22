s = "MCMXCIV"
output = 0

if 'CM' in s:
    output += 900
    s = s.replace('CM','')
if 'CD' in s:
    output += 400
    s = s.replace('CD','')
if 'XC' in s:
    output += 90
    s = s.replace('XC','')
if 'XL' in s:
    output += 40
    s = s.replace('XL','')
if 'IX' in s:
    output += 9
    s = s.replace('IX','')
if 'IV' in s:
    output += 4
    s = s.replace('IV','')
romans = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
for i in romans.keys():
    output += s.count(i)*romans[i]




print(output)
