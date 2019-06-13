n = int(input())
student_marks = {}
b = 0
for _ in range(n):
       name, *line = input().split()
       scores = list(map(float, line))
       student_marks[name] = scores
query_name = input()
t = (sum([ i for key in student_marks for i in student_marks[key] if key == query_name])/3)
print(b)
