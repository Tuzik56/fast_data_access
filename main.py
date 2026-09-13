import time


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
print(f"Отсутствующий элемент: {time_search_missing:.8f} сек")


########################################################################################################################


