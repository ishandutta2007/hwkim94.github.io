#----시간초과----
import sys

def palindrome(lst, start, end) :
    if start == end :
        return 1
    
    length = len(lst)
    center = length//2
    
    if length % 2 != 0 :
        temp1 = lst[:center]
        temp2 = lst[center+1:]

    else :
        temp1 = lst[:center]
        temp2 = lst[center:]
        
    temp2.reverse()

    if temp1 == temp2 :
        return 1
    else :
        return 0

    
num = int(input())
nlst = list(map(int, sys.stdin.readline().split()))

num2 = int(input())
questions = list(map(lambda x : x.strip(), sys.stdin.readlines()))
for question in questions :
    s, e = map(int, question.split())
    print(palindrome(nlst[s-1:e], s, e))

#----DP----
import sys
sys.setrecursionlimit(100000)

memo = {}

def palindrome(lst, start, end) :
    if start == end :
        return 1

    if start+1 == end :
        if lst[start] == lst[end] :
            memo[(start, end)] = 1
            return 1
        else :
            memo[(start,end)] = 0
            return 0
    if start + 2 == end :
        if lst[start] == lst[end] :
            memo[(start, end)] = 1
            return 1
        else :
            memo[(start,end)] = 0
            return 0
    
    if lst[start] == lst[end] :
        if (start+1, end-1) in memo.keys() :
            ans = memo[(start+1, end-1)]
            memo[(start, end)] = ans
            return ans

        else :
            ans = palindrome(lst, start+1, end-1)
            memo[(start, end)] = ans
            return ans
        

    else :
        memo[(start, end)] = 0
        return 0

    
num = int(input())
nlst = list(map(int, sys.stdin.readline().split()))

num2 = int(input())
questions = list(map(lambda x : x.strip(), sys.stdin.readlines()))

for question in questions :
    s, e = map(int, question.split())
    print(palindrome(nlst, s-1, e-1))
    
