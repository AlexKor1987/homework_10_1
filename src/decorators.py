#from time import time
#from time import time.time
#from time import time.ctime

import time


def log(filename=None):
    def my_decor(func):
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                success_message = f"Function {func.__name__} is ok. Result: {result}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(success_message + "\n")
                else:
                    print(success_message)
                return result
            except Exception as e:
                error_message = f"Error in {func.__name__}: {type(e).__name__}, args: {args}, kwargs: {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as text:
                        text.write(error_message + "\n")
                else:
                    print(error_message)
        return inner
    return my_decor

def printing_start_finish_time(func):
    def wrapper(*args, **kwargs):
        current_time_1 = time.time()
        time_1 = time.ctime(current_time_1)
        time_message_1 = f"Function {func.__name__} started in {time_1}"
        with open("mylog.txt", "a", encoding="utf-8") as f:
            f.write("\n" + time_message_1 + "\n")
        result = func(*args, **kwargs)  # Вызов исходной функции
        current_time_2 = time.time()
        time_2 = time.ctime(current_time_2)
        time_message_2 = f"Function {func.__name__} finished in {time_2}"
        with open("mylog.txt", "a", encoding="utf-8") as f:
            f.write(time_message_2 + "\n")
        return result
    return wrapper

@printing_start_finish_time
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)