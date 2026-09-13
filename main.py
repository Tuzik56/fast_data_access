import time
import random


print("--- Задание 2: Доступ по индексу и линейный поиск ---")

n = 100000
numbers = list(range(n))

idx_start = 0
idx_middle = n // 2
idx_end = n - 1

target_start = numbers[idx_start]
target_middle = numbers[idx_middle]
target_end = numbers[idx_end]
target_missing = -1

start_time = time.perf_counter()
val_start = numbers[idx_start]
time_idx_start = time.perf_counter() - start_time

start_time = time.perf_counter()
val_middle = numbers[idx_middle]
time_idx_middle = time.perf_counter() - start_time

start_time = time.perf_counter()
val_end = numbers[idx_end]
time_idx_end = time.perf_counter() - start_time

print("Доступ по индексу")
print(f"Начало: {time_idx_start:.8f} сек")
print(f"Середина: {time_idx_middle:.8f} сек")
print(f"Конец: {time_idx_end:.8f} сек\n")


def linear_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1


start_time = time.perf_counter()
res_start = linear_search(numbers, target_start)
time_search_start = time.perf_counter() - start_time

start_time = time.perf_counter()
res_middle = linear_search(numbers, target_middle)
time_search_middle = time.perf_counter() - start_time

start_time = time.perf_counter()
res_end = linear_search(numbers, target_end)
time_search_end = time.perf_counter() - start_time

start_time = time.perf_counter()
res_missing = linear_search(numbers, target_missing)
time_search_missing = time.perf_counter() - start_time

print("Поиск")
print(f"Начало: {time_search_start:.8f} сек")
print(f"Середина: {time_search_middle:.8f} сек")
print(f"Конец: {time_search_end:.8f} сек")
print(f"Отсутствующий элемент: {time_search_missing:.8f} сек\n")


########################################################################################################################


print("--- Задание 3: Доступ по ключу ---")

n = 10000
ids = random.sample(range(1, 20001), n)
data_list = [(id, f"value_{id}") for id in ids]


def search_in_list(lst, target_id):
    for id, val in lst:
        if id == target_id:
            return val
    return None


data_dict = {id: val for id, val in data_list}
test_ids = [random.randint(1, 20000) for _ in range(5000)]

start_time = time.perf_counter()
for target_id in test_ids:
    search_in_list(data_list, target_id)
list_search_time = time.perf_counter() - start_time

start_time = time.perf_counter()
for target_id in test_ids:
    data_dict.get(target_id)
dict_search_time = time.perf_counter() - start_time


print(f"Время поиска в списке: {list_search_time:.5f} сек")
print(f"Время поиска в словаре: {dict_search_time:.5f} сек")
print(f"Словарь быстрее списка в {list_search_time / dict_search_time:.1f} раз")


########################################################################################################################


