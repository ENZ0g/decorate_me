import time


class Timer:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, *args):
        self.end = time.time()
        self.time = self.end - self.start
        print(f'Функция выполнена 1 раз.\n'
              f'Время выполнения: {round(self.time, 4)}с')


def reverse_list(max_items):
    list_ = []
    for i in range(max_items):
        list_.append(i)
    list_.reverse()


with Timer():
    reverse_list(1000000)
