# -*- coding: utf-8 -*-
# Автор: Миниханов Рафаэль
# Дата: 17.06.2026
# Модуль 2. Условные конструкции и циклы.
# Выполнены упражнения 1, 2, 3, 6, 9 (любые 5 из списка).


def task1_financial_result():
    """Упр. 1. Финансовый результат периода через if/elif/else."""
    print("=== Финансовый результат периода ===")
    profit = float(input("Итоговая прибыль за месяц, руб.: "))
    if profit > 0:
        print("Прибыль")
    elif profit < 0:
        print("Убыток")
    else:
        print("Безубыточность")


def task2_business_category():
    """Упр. 2. Классификация субъекта по годовой выручке."""
    print("\n=== Классификация по выручке ===")
    revenue = float(input("Годовая выручка, руб.: "))
    if revenue <= 1_000_000:
        category = "Микробизнес"
    elif revenue <= 10_000_000:
        category = "Малый бизнес"
    elif revenue <= 100_000_000:
        category = "Средний бизнес"
    else:
        category = "Крупный бизнес"
    print(f"Категория: {category}")


def task3_personal_income_tax():
    """Упр. 3. Расчёт НДФЛ по прогрессивной ставке."""
    print("\n=== Расчёт НДФЛ ===")
    salary = float(input("Ежемесячная зарплата, руб.: "))
    rate = 13 if salary <= 50000 else 15
    tax = salary * rate / 100
    net = salary - tax
    print(f"Ставка НДФЛ: {rate} %")
    print(f"Сумма налога: {round(tax, 2)} руб.")
    print(f"Зарплата на руки: {round(net, 2)} руб.")


def task6_compound_interest_table():
    """Упр. 6. Накопление капитала по модели сложного процента (5 лет)."""
    print("\n=== Сложный процент за 5 лет ===")
    principal = float(input("Начальный капитал, руб.: "))
    rate = float(input("Процентная ставка, %: "))
    for year in range(1, 6):
        amount = principal * (1 + rate / 100) ** year
        print(f"Год {year}: {round(amount, 2)} руб.")


def task9_half_year_revenue():
    """Упр. 9. Анализ выручки за полугодие: min, max, среднее."""
    print("\n=== Анализ выручки за полугодие ===")
    revenues = []
    for month in range(1, 7):
        value = float(input(f"Выручка за месяц {month}, руб.: "))
        revenues.append(value)
    print(f"Минимальная выручка: {min(revenues)} руб.")
    print(f"Максимальная выручка: {max(revenues)} руб.")
    print(f"Среднемесячная выручка: {round(sum(revenues) / len(revenues), 2)} руб.")


if __name__ == "__main__":
    task1_financial_result()
    task2_business_category()
    task3_personal_income_tax()
    task6_compound_interest_table()
    task9_half_year_revenue()
