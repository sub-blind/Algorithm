test_count = int(input())
for _ in range(test_count):
    list_size = int(input())
    list1 = input().split()
    list2_input = input().split()
    list2_map = {}
    
    for index, item in enumerate(list2_input):
        list2_map[item] = index
    secret = input().split()
    result = []
    
    for item in list1:
        index_in_list2 = list2_map[item]
        secret_value = secret[index_in_list2]
        result.append(secret_value)
    print(*result)