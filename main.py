"""Задача. Вам нужно написать функцию расчёта стоимости доставки.
Стоимость рассчитывается в зависимости от:
- расстояния до пункта назначения:
    - более 30 км: +300 рублей к доставке;
    - до 30 км: +200 рублей к доставке;
    - до 10 км: +100 рублей к доставке;
    - до 2 км: +50 рублей к доставке;
- габаритов груза:
    - большие габариты: +200 рублей к доставке;
    - маленькие габариты: +100 рублей к доставке;
- хрупкости груза. Если груз хрупкий — +300 рублей к доставке. Хрупкие грузы нельзя возить на расстояние более 30 км;
- загруженности службы доставки. Стоимость умножается на коэффициент доставки:
    - очень высокая загруженность — 1.6;
    - высокая загруженность — 1.4;
    - повышенная загруженность — 1.2;
    - во всех остальных случаях коэффициент равен 1.

Минимальная сумма доставки — 400 рублей. Если сумма доставки меньше минимальной, выводится минимальная сумма."""


def check_datas(distance, dimensions, fragile, workload):
    """
    check the received data for correctness.
    :param distance: int, float
    :param dimensions: 'big' or 'little'
    :param fragile: 'yes', None
    :param workload: 'very high', 'high', 'medium', None
    :return: Fals or str with a description of the error
    """
    if not isinstance(distance, (int, float)) or distance <= 0:
        return 'Неверно указано расстояние до пункта назначения'
    if dimensions not in ['big', 'little']:
        return "Неверно указаны габариты"
    if fragile not in ['yes', None]:
        return "Неверно указана хрупкость"
    if workload not in ['very high', 'high', 'medium', None]:
        return "Неверно указана загруженность"
    if distance > 30 and fragile == 'yes':
        return 'Груз запрещен к перевозке, хрупкий и дистанция более 30 км'
    return False


def calculation_distance(distance, cost):
    """
    check distance calculation
    """
    if distance <= 2:
        cost += 50
    elif distance <= 10:
        cost += 100
    elif distance <= 30:
        cost += 200
    elif distance > 30:
        cost += 300
    return cost


def calculate_dimension(dimensions, cost):
    """
    calculate cargo dimensions
    """
    if dimensions == 'big':
        cost += 200
    elif dimensions == 'little':
        cost += 100
    return cost


def calculate_fragile(fragile, cost):
    """calculate fragile"""
    if fragile == 'yes':
        cost += 300
    return cost


def calculate_workload(workload, cost):
    """load cost calculation"""
    if workload == 'very high':
        cost *= 1.6
    elif workload == 'high':
        cost *= 1.4
    elif workload == 'medium':
        cost *= 1.2
    return cost

def check_finish_cost(cost):
    """check the final price"""
    if cost < 400:
        cost = 400
    return cost


def calculation_cargo_delivery(distance, dimensions, fragile, workload):
    result_check = check_datas(distance, dimensions, fragile, workload)
    if result_check:
        return result_check
    cost = 0
    cost = calculation_distance(distance, cost)
    cost = calculate_dimension(dimensions, cost)
    cost = calculate_fragile(fragile, cost)
    cost = calculate_workload(workload, cost)
    cost = check_finish_cost(cost)

    return cost


if __name__ == "__main__":
    distance = 1
    dimensions = 'big'
    fragile = 'yes'
    workload = 'high'
    cost = calculation_cargo_delivery(distance, dimensions, fragile, workload)
    # print(cost)
