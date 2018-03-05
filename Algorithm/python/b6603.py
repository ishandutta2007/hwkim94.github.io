#모듈을 이용한 구현
import sys
import itertools

lines = tuple(map(lambda x : x.strip(), sys.stdin.readlines()))
lines = tuple(map(lambda x : list(map(int, x.split()[1:])), lines))

for idx, line in enumerate(lines[:-1]) :
    if idx :
        print("")
    
    results = list(itertools.combinations(sorted(line), 6))

    for result in results :
        print(" ".join(map(str, result)), end=" ")
        print("")

    
