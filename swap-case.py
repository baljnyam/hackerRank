'''def swap_case(s):
    for i in range(len(s)):
        if s[i].islower:
            s = s.replace(s[i], s[i].upper())
        elif s[i] == s[i].upper():
            s = s.replace(s[i], s[i].lower())
        else:
            continue
    return s
'''
def swap_case(s):
       b = ''
       for i in s:
              if i.isalpha():
                     if i.isupper():
                            b = b + i.lower()
                     else:
                            b = b + i.upper()
              else:
                     b = b + i
       
       return b
                     
s = input()
result = swap_case(s)

print(result)



