neme = []
scere = []
for _ in range(int(input())):
       name = input()
       score = float(input())
       neme.append(name)
       scere.append(score)
b = []
k = []
n = [i for i in range(len(scere)) if scere[i] > min(scere)]
for i in n:
       b.append(scere[i])
for i in n:
       if min(b) == scere[i]:
              k.append(neme[i])
k.sort()
for i in k:
       print(i)
