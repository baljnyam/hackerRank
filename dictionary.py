# def group_by_owners(files):

#     return files


files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
# problem: how to add 2 value to values
# t = list(files.values())
# m = {}
# for i in files:
#     if i in m:
#         m[files[i]].append(i)
#     m[files[i]] = i
d = {}
for k, v in files.items():
    if v in d:
        d[v].append(k)
    else:
        d[v] = [k]
print(d)
