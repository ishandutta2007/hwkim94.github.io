import sys

num, cri = map(int, sys.stdin.readline().split())
student_from = [0] *(num+1)
student_to = [False] *(num+1)
criterion = list(map(lambda x : x.strip(), sys.stdin.readlines()))

for front, back in map(lambda x : map(int, x.split()), criterion) :     
    student_from[back] += 1

    if student_to[front] :
        student_to[front].append(back)
    else :
        student_to[front] = [back]

lst = [x for x in range(1, num+1) if not student_from[x]]
result = []
while lst :
    start = lst.pop(0)
    result.append(start)

    if not student_to[start] :
        continue
    
    for student in student_to[start] :
        student_from[student] -= 1

        if not student_from[student] :
            lst.append(student)

sys.stdout.write(" ".join(map(str, result)) + "\n")
