import sys

input = sys.stdin.readline

n, m = map(int, input().split())

pokemon_list = [input().rstrip() for _ in range(n)]
pokemon_dict = {name: i + 1 for i, name in enumerate(pokemon_list)}

for _ in range(m):
    quest = input().rstrip()
    
    if '0' <= quest[0] <= '9':
        print(pokemon_list[int(quest) - 1])
    else:
        print(pokemon_dict[quest])
