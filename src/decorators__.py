
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)







try:
    result = func(*args, **kwargs)
except Exception as e:
    error_message = f"Ошибка в {func.__name__}: {type(e).__name__}, args: {args}, kwargs: {kwargs}"
    if filename:
        with open(filename, 'a') as f:
            f.write(error_message + "\n")
    else:
        print(error_message)
    raise




try:
    result = func(*args, **kwargs)
    success_message = f"Функция {func.__name__} успешно завершена. Результат: {result}"
    if filename:
        with open(filename, 'a') as f:
            f.write(success_message + "\n")
    else:
        print(success_message)
except Exception as e:
    # Обработка ошибок




    def log(filename=None):
        def my_decor(func):
            def inner(*args, **kwargs):
                try:
                    result = func(*args, **kwargs)
                    success_message = f"Функция{func.__name__} успешно завершена. Результат : {result}"
                    if filename:
                        with open(filename, "a") as f:
                            f.write(success_message + "\n")
                    else:
                        print(success_message)
                except Exception as e:
                    error_message = f"Ошибка в {func.__name__} :{type(e).__name__}, args :{args}, kwargs{kwargs}"
                    if filename:
                        with open(filename, 'a') as f:
                            f.write(error_message + "\n")
                    else:
                        print(error_message)