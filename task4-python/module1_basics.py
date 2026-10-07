# -*- coding: utf-8 -*-
# Автор: Миниханов Рафаэль
# Дата: 17.06.2026
# Модуль 1. Переменные, типы данных, ввод и вывод.
# Выполнены упражнения 1, 3, 5, 6, 10 (любые 5 из списка).
# Тематика — экономический анализ для платформы SellWhy.


def task1_employee_card():
    """Упр. 1. Карточка сотрудника: переменные разных типов и вывод."""
    name = "Ольга"            # str — имя сотрудника
    age = 24                   # int — возраст
    salary = 85000.50          # float — заработная плата
    is_employed = True         # bool — признак занятости

    print("=== Карточка сотрудника ===")
    print(f"Имя сотрудника: {name}")
    print(f"Возраст: {age} лет")
    print(f"Заработная плата: {salary} руб.")
    print(f"Признак занятости: {is_employed}")


def task3_total_cost():
    """Упр. 3. Расчёт итоговой стоимости товара."""
    print("\n=== Расчёт итоговой стоимости ===")
    price = float(input("Цена единицы товара, руб.: "))
    quantity = int(input("Количество единиц: "))
    total = price * quantity
    print(f"Итоговая стоимость заказа: {total} руб.")


def task5_currency_conversion():
    """Упр. 5. Конвертация рублей в доллары с округлением."""
    print("\n=== Конвертация валюты ===")
    usd_rate = float(input("Курс доллара к рублю: "))
    amount_rub = float(input("Сумма в рублях: "))
    amount_usd = round(amount_rub / usd_rate, 2)
    print(f"{amount_rub} руб. = {amount_usd} USD")


def task6_profit_and_margin():
    """Упр. 6. Прибыль и рентабельность продаж."""
    print("\n=== Прибыль и рентабельность ===")
    revenue = float(input("Выручка, руб.: "))
    costs = float(input("Общие затраты, руб.: "))
    profit = revenue - costs
    margin = profit / revenue * 100 if revenue else 0
    print(f"Прибыль: {profit} руб.")
    print(f"Рентабельность продаж: {round(margin, 2)} %")


def task10_invoice_with_vat():
    """Упр. 10. Расчёт счёта с НДС."""
    print("\n=== Счёт с НДС ===")
    quantity = int(input("Количество единиц товара: "))
    price = float(input("Цена за единицу, руб.: "))
    vat_rate = float(input("Ставка НДС, %: "))
    cost_without_vat = quantity * price
    vat_sum = cost_without_vat * vat_rate / 100
    total_with_vat = cost_without_vat + vat_sum
    print(f"Стоимость без НДС: {round(cost_without_vat, 2)} руб.")
    print(f"Сумма НДС: {round(vat_sum, 2)} руб.")
    print(f"Итого с НДС: {round(total_with_vat, 2)} руб.")


if __name__ == "__main__":
    task1_employee_card()
    task3_total_cost()
    task5_currency_conversion()
    task6_profit_and_margin()
    task10_invoice_with_vat()
