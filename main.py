import pandas as pd


# Объединение 2х датасетов
def save_main_dataset():
    first_data = pd.read_csv('datasets/first_part.csv')
    second_data = pd.read_csv('datasets/second_part.csv')

    main_dataset = pd.merge(first_data, second_data[
        ['Date', 'District', 'Warehouse_Name', 'Percent_of_Crime_Solved', 'Number_of_Lights']],
                            on=['Date', 'District', 'Warehouse_Name'],
                            how='left')
    main_dataset.to_csv('datasets/main_dataset.csv', index=False)

# Полнота, проверка на пустые значения
def completeness():
    data = pd.read_csv('datasets/main_dataset.csv')

    if data.isnull().values.any():
        print("В датасете есть пустые значения.")
    else:
        print("В датасете нет пустых значений.")

    missing_values = data.isnull().sum()
    print("Количество пустых значений в каждой колонке:")
    print(missing_values)

# Уникальность, проверка на повторяемость данных
def uniqueness():
    data = pd.read_csv('datasets/main_dataset.csv')

    if data.duplicated().any():
        print("В датасете есть дубликаты.")
    else:
        print("В датасете нет дубликатов.")

    duplicate_count = data.duplicated().sum()
    print("Количество дубликатов в датасете:", duplicate_count)

uniqueness()