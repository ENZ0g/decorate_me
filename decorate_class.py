import time


class Timer:
    def __init__(self, runs=10):
        self.runs = runs

    def __call__(self, runs=None, *args, **kwargs):
        if runs is None:
            runs = self.runs

        if callable(runs):          # при вызове "пустого" декоратора @timer, в runs передается
                                    # декорируемя функция
            def run_time(x):
                avr_time = 0
                for _ in range(self.runs):
                    time_start = time.time()
                    runs(x)
                    time_end = time.time()
                    avr_time += (time_end - time_start)
                print(f'Функция выполнена {self.runs} раз.\n'
                      f'Среднее время выполнения: {round(avr_time / self.runs, 4)}с')

            return run_time

        else:
            def decorator(func):

                def run_time(x):
                    avr_time = 0
                    for _ in range(runs):
                        time_start = time.time()
                        func(x)
                        time_end = time.time()
                        avr_time += (time_end - time_start)
                    print(f'Функция выполнена {runs} раз.\n'
                          f'Среднее время выполнения: {round(avr_time / runs, 4)}с')

                return run_time
            return decorator


timer = Timer(9)    # при отсутствии параметра (количество прогонов функции), он принимается равным 10

# @timer            # можно вообще не указывать ни (), ни параметр, тогда он берется равным указанному при создании
                    # экземпляра класса, функция __call__ выполняет условеие callable

# @timer()          # при указании пустых скобок берется значение, указанное при создании экземпляра класса,
                    # выполняется ветка else функции __call__

@timer(13)          # можно переопределить количество прогонов
def reverse_list(max_items):
    list_ = []
    for i in range(max_items):
        list_.append(i)
    list_.reverse()


reverse_list(100000)
