# -*- coding: utf-8 -*-
# Автор: Миниханов Рафаэль
# Дата: 17.06.2026
# Итоговая мини-программа. Вариант 1 — Калькулятор рентабельности.
# Объединяет конструкции всех трёх модулей:
#   - переменные разных типов (str, float, bool);
#   - условная конструкция if/elif/else (качественная оценка);
#   - цикл for (вывод построчного отчёта);
#   - две функции с docstring.


def calculate_metrics(revenue, costs):
    """Вычисляет прибыль и рентабельность продаж.

    Возвращает кортеж (прибыль, рентабельность в %).
    """
    profit = revenue - costs
    margin = profit / revenue * 100 if revenue else 0.0
    return profit, margin


def assess_margin(margin):
    """Возвращает качественную оценку уровня рентабельности."""
    if margin > 20:
        return "высокая рентабельность"
    elif margin >= 10:
        return "средняя рентабельность"
    return "низкая рентабельность"


def main():
    """Точка входа: ввод данных, расчёт и вывод структурированного отчёта."""
    print("=== Калькулятор рентабельности (SellWhy) ===")
    company = input("Наименование компании: ")
    revenue = float(input("Выручка, руб.: "))
    costs = float(input("Затраты, руб.: "))

    profit, margin = calculate_metrics(revenue, costs)
    assessment = assess_margin(margin)
    is_profitable = profit > 0

    report_lines = [
        f"Компания:               {company}",
        f"Выручка:                {revenue:.2f} руб.",
        f"Затраты:                {costs:.2f} руб.",
        f"Прибыль:                {profit:.2f} руб.",
        f"Рентабельность продаж:  {margin:.2f} %",
        f"Качественная оценка:    {assessment}",
        f"Прибыльность:           {'да' if is_profitable else 'нет'}",
    ]

    print("\n----- ИТОГОВЫЙ ОТЧЁТ -----")
    for line in report_lines:
        print(line)


if __name__ == "__main__":
    main()
