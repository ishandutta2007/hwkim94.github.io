import sys

num1, num2 = map(int, input().split())
i = list(map(lambda x : x.strip(), sys.stdin.readlines()))

pokemons, quizs = i[:num1], i[num1:]

pokemon_dic = {}
num_dic = {}

for num, pokemon in enumerate(pokemons) :
    pokemon_dic[pokemon] = num
    num_dic[num+1] = pokemon

answer = []

for quiz in quizs :
    if not quiz.isaplha() :
        quiz = int(quiz)
        answer.append(num_dic[quiz])
    else :
        answer.append(str(pokemon_dic[quiz]+1))
        
print ("\n".join(answer))
