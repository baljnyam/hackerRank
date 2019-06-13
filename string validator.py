s = input()
a = False
b = False
d = False
e = False
for i in s:
     if i.isalpha():
          a = a or True
          if i.islower():
               d = d or True
          else:
               e = e or True
     elif i.isdigit():
          b = b or True
     else:
          continue
print(a and b)
print(a)
print(b)
print(d)
print(e)


