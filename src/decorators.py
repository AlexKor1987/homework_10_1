import time


def log(filename=None):
    """Декоратор, который автоматически логирует начало и конец выполнения
    функции, а также ее результаты или возникшие ошибки"""
    def my_decor(func):
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                success_message = f"Function {func.__name__} is ok. Arguments: {args} Result: {result}"
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
                raise
        return inner
    return my_decor


def printing_start_finish_time(func):
    """Декоратор, который выводит время начала и время окончания работы
    программы, а также её длительность"""
    def wrapper(*args, **kwargs):
        current_time_1 = time.time()
        time_1 = time.ctime(current_time_1)
        time_message_1 = f"Function {func.__name__} started in {time_1}"
        with open("mylog.txt", "a", encoding="utf-8") as f:
            f.write("\n" + time_message_1 + "\n")
        result = func(*args, **kwargs)  # Вызов исходной функции
        current_time_2 = time.time()
        time_2 = time.ctime(current_time_2)
        d_time = round((current_time_2 - current_time_1), 3)
        time_message_2 = f"Function {func.__name__} finished in {time_2}, working time is {d_time}"
        with open("mylog.txt", "a", encoding="utf-8") as f:
            f.write(time_message_2 + "\n")
        return result
    return wrapper


@printing_start_finish_time
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)
