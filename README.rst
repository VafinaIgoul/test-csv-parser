Пример обработчика csv-файла.

Скрипт для обработки входящего файла csv и создания нового файла.
Входной файл содержит три параметра
  - Equipment
  -Value
  -Utilization
Выходной файл содержит дополнительное вычисляемое значение MaxUtil
 MaxUtil = Value / Utilization

Пример запуска файла
python csv_parser.py -f /tmp/input-csv.csv -o /tmp/output.csv