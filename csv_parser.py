#!/usr/bin/env python3

"""
 Скрипт для обработки входящего файла csv и создания нового файла.
 Входной файл содержит три параметра
  - Equipment
  -Value
  -Utilization
 Выходной файл содержит дополнительное вычисляемое значение MaxUtil
 MaxUtil = Value / Utilization

 Пример запуска файла
 python csv_parser.py -f /tmp/input-csv.csv -o /tmp/output.csv

"""

import argparse
from csv import DictReader
from csv import DictWriter

DIGITS = 2
VALUE = 'Value'
UTILIZATION = 'Utilization'
MAX_UTIL = 'MaxUtil'


def parse_args():
    """Указание агрументов при запуске скрипта."""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-f', '--file',
        help='CSV input file',
        type=str,
    )
    parser.add_argument(
        '-o', '--output_file',
        help='CSV output file',

    )
    return parser.parse_args()


def count_max_util(value: float, utilization: float) -> float:
    """Рассчет макисмальной возможности использования MaxUtil"""
    try:
        max_util = round(value / utilization * 100, DIGITS)
    except ZeroDivisionError:
        max_util = 0
    return max_util


def get_utilization(utilization: str) -> float:
    """Возвращает данные по Utilization в виде десятичного числа.

    Также перед перобразованием из строки исключается знак процента.
    """
    utilization = utilization.rstrip('%')
    return float(utilization)


def parse_csv_file(input_file_name: str, output_file_name: str):
    """Парсинг входящего csv файла и запись результатов во второй csv файл."""
    with open(input_file_name, 'r') as read_csv:
        csv_dict_reader = DictReader(read_csv)
        csv_fieldnames = csv_dict_reader.fieldnames

        if UTILIZATION in csv_fieldnames and VALUE in csv_fieldnames:
            csv_fieldnames.append(MAX_UTIL)

            with open(output_file_name, 'w') as output_csv:

                writer = DictWriter(output_csv, fieldnames=csv_fieldnames)
                writer.writeheader()

                for row in csv_dict_reader:
                    value = row.get(VALUE)
                    util = row.get(UTILIZATION)
                    if value and util:
                        try:
                            value = float(value)
                            util = get_utilization(util)
                            row[MAX_UTIL] = count_max_util(value, util)
                            writer.writerow(row)
                        except (TypeError, ValueError):
                            continue
        else:
            print('Check your input_file! Incorrect data!')


if __name__ == "__main__":
    options = parse_args()
    parse_csv_file(options.file, options.output_file)
