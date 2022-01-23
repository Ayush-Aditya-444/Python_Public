n = int(input())
student_marks = {}
for _ in range(n):
    name = input().split()
    a=float(name[1])
    c=float(name[2])
    b=float(name[3])
    d=(a+b+c)/3
    e="{:.2f}". format(d)
    student_marks[name[0]]=e
query_name = input()
print(student_marks[query_name])