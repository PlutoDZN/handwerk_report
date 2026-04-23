from datetime import datetime


def calculate_labor_minutes(start_time: str, end_time: str) -> int:
    start = datetime.strptime(start_time, "%H:%M")
    end = datetime.strptime(end_time, "%H:%M")

    diff = end - start
    minutes = int(diff.total_seconds() // 60)

    if minutes <= 0:
        raise ValueError("Endzeit muss nach Startzeit liegen.")

    return minutes


def calculate_labor_cost(labor_minutes: int, hourly_rate: float) -> float:
    return round((labor_minutes / 60) * hourly_rate, 2)


def calculate_material_total(quantity: float, unit_price: float) -> float:
    if quantity <= 0:
        raise ValueError("Materialmenge muss größer 0 sein.")
    if unit_price < 0:
        raise ValueError("Materialpreis darf nicht negativ sein.")
    return round(quantity * unit_price, 2)


def calculate_total_cost(labor_cost: float, material_cost: float, travel_cost: float) -> float:
    if travel_cost < 0:
        raise ValueError("Fahrtkosten dürfen nicht negativ sein.")
    return round(labor_cost + material_cost + travel_cost, 2)