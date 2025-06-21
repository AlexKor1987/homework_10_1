import pytest
from io import StringIO
from contextlib import redirect_stdout
from src.decorators import log


@log()
def add(a, b):
    return a + b


# Тест на проверку логирования в консоль
def test_success_logging_to_console():
    f = StringIO()
    with redirect_stdout(f):
        result = add(2, 3)
    output = f.getvalue().strip()

    assert result == 5
    assert "Функция add успешно завершена. Результат: 5" in output


@log()
def divide(a, b):
    return a / b


# Тест на проверку логирования ошибок в консоль
def test_error_logging_to_console():
    f = StringIO()
    with redirect_stdout(f):
        with pytest.raises(ZeroDivisionError):
            divide(1, 0)
    output = f.getvalue().strip()

    assert "Ошибка в divide:" in output
    assert "ZeroDivisionError" in output