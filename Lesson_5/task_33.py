"""Хакер Василий получил доступ к классному журналу 
и хочет заменить все свои минимальные оценки на максимальные."""


# Вариант 1 - max and min
# list_of_ratings = [2, 2, 4, 3, 2, 3, 3, 5, 5, 5, 5, 5, 10]
# max_number = max(list_of_ratings)
# min_number = min(list_of_ratings)
# print(f'Минимум - {min_number}, Максимум - {max_number}')

# for i in range(len(list_of_ratings)):
#     if list_of_ratings[i] == min_number:
#         list_of_ratings[i] = max_number
        
# print(list_of_ratings)


def update_ratings(list_of_ratings):
    max_number = max(list_of_ratings)
    min_number = min(list_of_ratings)
    print(f'Минимум - {min_number}, Максимум - {max_number}')

    for i in range(len(list_of_ratings)):
        if list_of_ratings[i] == min_number:
            list_of_ratings[i] = max_number
            
    return list_of_ratings


ratings_peapls = {"Антон": [2, 2, 4, 3, 2, 3, 3, 5, 5, 5, 5, 5, 9], 
                  "Дмитрий": [1, 2, 4, 5, 8, 2, 1], 
                  "Алексей": [1, 2, 4, 1, 9, 2, 1]}

for peapl_rating in ratings_peapls.values():
    result = update_ratings(peapl_rating)
    print(result)

update_ratings_list = [update_ratings(peapl_rating) for peapl_rating in ratings_peapls.values()]
print(update_ratings_list)

# test_data = []
# for i in range(10):
#     if i % 2 == 0:
#         test_data.append(i)

# print(test_data)

# test_data2 = [i for i in range(10) if i % 2 == 0]
# print(test_data2)