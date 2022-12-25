import pytest
from application.function import obj_sort


@pytest.mark.parametrize('letters', [
    'СкКЗзКСс',
    'сскзскз',
])
@pytest.mark.parametrize('color', [
    'КЗС',
    'ЗСК',
])
def test_valid_parametrize(letters, color):
    """Дымовое тестирование - позитивное."""
    assert obj_sort(letters, color)


@pytest.mark.parametrize('letters', [
    'qwertivm',
    'ошвлуьсвпе'
])
@pytest.mark.parametrize('color', [
    ' ',
    '164572547',
])
def test_invalid_parametrize(letters, color):
    """Дымовое тестирование - негативное."""
    assert not obj_sort(letters, color)


def test_valid_params():
    """Простой пример с валидными заглавными буквами."""
    res = obj_sort('СКЗКСКЗЗ', 'СКЗ')
    assert res == ['С', 'С', 'К', 'К', 'К', 'З', 'З', 'З']


def test_valid_different_params():
    """Проверяем комбинации заглавных и строчных букв."""
    res = obj_sort('СкКЗзКСс', 'СКЗ')
    assert res == ['С', 'С', 'с', 'к', 'К', 'К', 'З', 'з']


def test_len_big_different_data():
    """Проверяем успешность обработки большого объема данных, с комбинацией заглавных и строчных букв - по длине."""
    res = obj_sort('СКЗКСЗКСскскзЗКССКЗСКЗКЗскскзСКЗСКСКЗСКЗСКСКЗСКЗЗКскскзЗСКЗСКЗЗКЗКЗСЗКЗскскзсзкСКЗСКСКЗ', 'СКЗ')
    assert len(res) == len('СКЗКСЗКСскскзЗКССКЗСКЗКЗскскзСКЗСКСКЗСКЗСКСКЗСКЗЗКскскзЗСКЗСКЗЗКЗКЗСЗКЗскскзсзкСКЗСКСКЗ')


def test_big_data():
    """Проверяем успешность обработки большого объема данных."""
    res = obj_sort('СКЗКСЗКСЗКСЗСКЗСКЗСКЗСКЗСКЗСКЗСКЗСКЗСКЗСКЗЗКЗСКЗСКЗСКЗЗСКЗСКЗСЗКЗСКЗСКЗСКЗСКЗ', 'КСЗ')
    assert len(res) == len('СКЗКСЗКСЗКСЗСКЗСКЗСКЗСКЗСКЗСКЗСКЗСКЗСКЗСКЗЗКЗСКЗСКЗСКЗЗСКЗСКЗСЗКЗСКЗСКЗСКЗСКЗ')
    assert res == ['К', 'К', 'К', 'К', 'К', 'К', 'К', 'К', 'К', 'К', 'К', 'К', 'К', 'К', 'К', 'К', 'К', 'К', 'К', 'К',
                   'К', 'К', 'К', 'К', 'К', 'С', 'С', 'С', 'С', 'С', 'С', 'С', 'С', 'С', 'С', 'С', 'С', 'С', 'С', 'С',
                   'С', 'С', 'С', 'С', 'С', 'С', 'С', 'С', 'С', 'З', 'З', 'З', 'З', 'З', 'З', 'З', 'З', 'З', 'З', 'З',
                   'З', 'З', 'З', 'З', 'З', 'З', 'З', 'З', 'З', 'З', 'З', 'З', 'З', 'З', 'З', 'З', 'З']


def test_invalid_params():
    """Простой пример с невалидными данными."""
    res = obj_sort('164572547', 'СК.')
    assert not res


@pytest.mark.parametrize('letters', [
    ' скзскз',
    'сскз скз',
])
@pytest.mark.parametrize('color', [
    'КЗС',
    'ЗСК',
])
def test_valid_data_with_space(letters, color):
    """Проверяем успешность валидных данных с пробелами."""
    assert obj_sort(letters, color)
