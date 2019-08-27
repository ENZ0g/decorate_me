import time


def time_this(num_runs=10):
    def decorator(func):

        def run_time(x):
            avr_time = 0
            for _ in range(num_runs):
                time_start = time.time()
                func(x)
                time_end = time.time()
                avr_time += (time_end - time_start)
            print(f'Функция выполнена {num_runs} раз.\n'
                  f'Среднее время выполнения: {round(avr_time / num_runs, 4)}c')

        return run_time
    return decorator


runs_ = int(input('Введите количество прогонов функции: '))
max_list_items = int(input('Введите максимальное число элементов списка (лучше 100 000 и более): '))
print('*** ВЫПОЛНЯЮ ***')


@time_this(runs_)
def reverse_list(max_items):    # Тестовая функция. Генерирует список и разворачивает его
    list_ = []
    for i in range(max_items):
        list_.append(i)
    list_.reverse()


reverse_list(max_list_items)
