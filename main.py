import time
import random
from hash_table import HashTable


print("----- Задание 2: Доступ по индексу и линейный поиск -----")

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


print("----- Задание 3: Доступ по ключу -----")

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
print(f"Словарь быстрее списка в {list_search_time / dict_search_time:.1f} раз\n")


########################################################################################################################


print("----- Задание 4: Исследование функции hash() -----")


def bucket_index(key, table_size):
    return abs(hash(key)) % table_size


int_key = 50
str_key = "hello"

print(f"Хеш {int_key}: {hash(int_key)}")
print(f"Хеш '{str_key}': {hash(str_key)}")

print(f"Повторный хеш {int_key}: {hash(int_key)}")
print(f"Повторный хеш '{str_key}': {hash(str_key)}\n")

table_size = 10

keys = [
    10,
    25,
    37,
    42,
    55,
    99,
    100,
    2026,
    777,
    123,
    "apple",
    "banana",
    "cherry",
    "python",
    "code",
    "data",
    "hash",
    "table",
    "index",
    "bucket",
    "test",
    "user",
    "admin",
    "key",
    "value",
    "list",
    "dict",
    "set",
    "tuple",
    "none",
    "true",
    "false",
]

buckets = {i: [] for i in range(table_size)}

for k in keys:
    idx = bucket_index(k, table_size)
    buckets[idx].append(k)

for idx, b_keys in buckets.items():
    print(f"Корзина {idx}: {b_keys}")


########################################################################################################################


print("\n----- Задание 5: Простая хеш-таблица методом цепочек -----")

hash_table = HashTable(size=5)

hash_table.set("apple", 100)
hash_table.set("banana", 200)
hash_table.set("orange", 300)
hash_table.set(5, "Пять")
hash_table.set(10, "Десять")
hash_table.set(15, "Пятнадцать")

print(hash_table)


########################################################################################################################
