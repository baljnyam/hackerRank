n = int(input())
arr = map(int, input().split())
j = list(arr)
t = [b for b in j if b < max(j)]
print(max(t))
