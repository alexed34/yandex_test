import pytest
from main import calculation_cargo_delivery, check_datas, calculation_distance, calculate_dimension, calculate_fragile, \
    calculate_workload, check_finish_cost


@pytest.fixture()
def test_datas():
    distance = 1
    dimensions = 'little'
    fragile = None
    workload = None
    return distance, dimensions, fragile, workload



@pytest.mark.parametrize('test_distance, expected',
                         [(1, False), (0.1, False),
                          (0, 'Неверно указано расстояние до пункта назначения'),
                          ('0', 'Неверно указано расстояние до пункта назначения')])
def test_check_datas_distance(test_datas, test_distance, expected):
    distance, dimensions, fragile, workload = test_datas
    actual_result = check_datas(test_distance, dimensions, fragile, workload)
    assert actual_result == expected


@pytest.mark.parametrize('test_dimensions, expected',
                         [('big', False), ('little', False),
                          (1, 'Неверно указаны габариты'),
                          ('a', 'Неверно указаны габариты')])
def test_check_datas_dimensions(test_datas, test_dimensions, expected):
    distance, dimensions, fragile, workload = test_datas
    actual_result = check_datas(distance, test_dimensions, fragile, workload)
    assert actual_result == expected


@pytest.mark.parametrize('test_fragile, expected',
                         [('yes', False), (None, False),
                          (1, 'Неверно указана хрупкость'),
                          ('a', 'Неверно указана хрупкость')])
def test_check_datas_fragile(test_datas, test_fragile, expected):
    distance, dimensions, fragile, workload = test_datas
    actual_result = check_datas(distance, dimensions, test_fragile, workload)
    assert actual_result == expected


@pytest.mark.parametrize('test_workload, expected',
                         [('very high', False), ('high', False), ('medium', False), (None, False),
                          (1, 'Неверно указана загруженность'),
                          ('a', 'Неверно указана загруженность')])
def test_check_datas_workload(test_datas, test_workload, expected):
    distance, dimensions, fragile, workload = test_datas
    actual_result = check_datas(distance, dimensions, fragile, test_workload)
    assert actual_result == expected

@pytest.mark.parametrize('test_distance, test_fragile, expected',
                         [(30,'yes', False), (30, None, False), (31,None, False),
                          (30.1,'yes', 'Груз запрещен к перевозке, хрупкий и дистанция более 30 км'),])
def test_check_datas_distance_and_fragile(test_datas, test_distance, test_fragile, expected):
    distance, dimensions, fragile, workload = test_datas
    actual_result = check_datas(test_distance, dimensions, test_fragile, workload)
    assert actual_result == expected




@pytest.mark.parametrize('distance, expected', [(0.1, 50), (2, 50), (10, 100), (30, 200), (31, 300),
                                                  (2.1, 100), (10.1, 200), (30.1, 300),
                                                 ])
def test_calculation_distance(distance, expected):
    cost = 0
    actual_result = calculation_distance(distance, cost)
    assert actual_result == expected



@pytest.mark.parametrize('dimensions, expected', [('big', 250), ('little', 150)])
def test_calculate_dimension(dimensions, expected):
    cost = 50
    actual_result = calculate_dimension(dimensions, cost)
    assert actual_result == expected


@pytest.mark.parametrize('fragile, expected', [('yes', 350), (None, 50)])
def test_calculate_fragile(fragile, expected):
    cost = 50
    actual_result = calculate_fragile(fragile, cost)
    assert actual_result == expected


@pytest.mark.parametrize('workload, expected', [('very high', 1.6), ('high', 1.4), ('medium', 1.2), (None, 1)])
def test_calculate_workload(workload, expected):
    cost = 50
    actual_result = calculate_workload(workload, cost)
    assert actual_result == cost * expected



@pytest.mark.parametrize('cost, expected', [(399, 400),(401, 401)])
def test_check_finish_cost(cost, expected):
    actual_result = check_finish_cost(cost)
    assert actual_result == expected


def test_calculation_cargo_delivery(test_datas):
    distance, dimensions, fragile, workload = test_datas
    actual_result = calculation_cargo_delivery(distance, dimensions, fragile, workload)
    assert actual_result == 400
    distance = -1
    actual_result = calculation_cargo_delivery(distance, dimensions, fragile, workload)
    assert actual_result == 'Неверно указано расстояние до пункта назначения'


