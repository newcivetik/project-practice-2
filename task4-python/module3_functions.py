# -*- coding: utf-8 -*-
# Автор: Миниханов Рафаэль
# Дата: 17.06.2026
# Модуль 3. Функции.
# Выполнены упражнения 1, 2, 3, 4, 10 (любые 5 из списка).
# У каждой функции есть docstring.


def calculate_profit(revenue, costs):
    """Упр. 1. Возвращает прибыль как разницу выручки и затрат."""
    return revenue - costs


def calculate_vat(price, vat_rate=20):
    """Упр. 2. Возвращает сумму НДС. Ставка по умолчанию — 20%."""
    return price * vat_rate / 100


def get_business_category(annual_revenue):
    """Упр. 3. Возвращает категорию бизнеса по годовой выручке."""
    if annual_revenue <= 1_000_000:
        return "Микробизнес"
    elif annual_revenue <= 10_000_000:
        return "Малый бизнес"
    elif annual_revenue <= 100_000_000:
        return "Средний бизнес"
    return "Крупный бизнес"


def compound_interest(principal, rate, years):
    """Упр. 4. Возвращает итоговую сумму по формуле сложного процента."""
    return principal * (1 + rate / 100) ** years


def generate_report(company, revenue, costs):
    """Упр. 10. Формирует и выводит многострочный отчёт по компании."""
    profit = calculate_profit(revenue, costs)
    margin = profit / revenue * 100 if revenue else 0
    conclusion = "деятельность прибыльна" if profit > 0 else "деятельность убыточна"
    print("----- Финансовый отчёт -----")
    print(f"Компания: {company}")
    print(f"Выручка: {revenue} руб.")
    print(f"Затраты: {costs} руб.")
    print(f"Прибыль: {profit} руб.")
    print(f"Рентабельность продаж: {round(margin, 2)} %")
    print(f"Вывод: {conclusion}")


if __name__ == "__main__":
    # Упр. 1 — три набора входных данных
    print("calculate_profit:")
    for rev, cost in [(100000, 60000), (50000, 70000), (200000, 200000)]:
        print(f"  выручка={rev}, затраты={cost} -> прибыль={calculate_profit(rev, cost)}")

    # Упр. 2 — с явной ставкой и по умолчанию
    print("\ncalculate_vat:")
    print(f"  ставка 10%: {calculate_vat(1000, 10)} руб.")
    print(f"  ставка по умолчанию 20%: {calculate_vat(1000)} руб.")

    # Упр. 3 — четыре категории
    print("\nget_business_category:")
    for value in [500_000, 5_000_000, 50_000_000, 500_000_000]:
        print(f"  {value} руб. -> {get_business_category(value)}")

    # Упр. 4 — сроки 3, 5, 10 лет
    print("\ncompound_interest (100000 руб., 8%):")
    for term in [3, 5, 10]:
        print(f"  {term} лет: {round(compound_interest(100000, 8, term), 2)} руб.")

    # Упр. 10 — отчёт
    print()
    generate_report("SellWhy", 1_200_000, 800_000)
