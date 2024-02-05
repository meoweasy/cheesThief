import pandas as pd
import streamlit as st

# Отображение исходных датасетов
st.subheader("Первая часть")
first_data = pd.read_csv('datasets/first_part.csv')
st.write(first_data)

st.subheader("Вторая часть")
second_data = pd.read_csv('datasets/second_part.csv')
st.write(second_data)

st.subheader("Объединенный датасет")
main_data = pd.read_csv('datasets/main_dataset.csv')
st.write(main_data)

# Объединение 2х датасетов
def save_main_dataset():
    first_data = pd.read_csv('datasets/first_part.csv')
    second_data = pd.read_csv('datasets/second_part.csv')

    main_dataset = pd.merge(first_data, second_data[
        ['Date', 'District', 'Warehouse_Name', 'Percent_of_Crime_Solved', 'Number_of_Lights']],
                            on=['Date', 'District', 'Warehouse_Name'],
                            how='left')
    main_dataset.to_csv('datasets/main_dataset.csv', index=False)

on_save = st.toggle('Объеденить 2 датасета')
if on_save:
    save_main_dataset()

# Полнота, проверка на пустые значения
def completeness():
    data = pd.read_csv('datasets/main_dataset.csv')

    if data.isnull().values.any():
        st.write("В датасете есть пустые значения.")
    else:
        st.write("В датасете нет пустых значений.")

    missing_values = data.isnull().sum()
    st.write("Количество пустых значений в каждой колонке:")
    st.write(missing_values)

on_completeness = st.toggle('Проверить полноту данных')
if on_completeness:
    completeness()

# Уникальность, проверка на повторяемость данных
def uniqueness():
    data = pd.read_csv('datasets/main_dataset.csv')

    if data.duplicated().any():
        st.write("В датасете есть дубликаты.")
    else:
        st.write("В датасете нет дубликатов.")

    duplicate_count = data.duplicated().sum()
    st.write("Количество дубликатов в датасете:", duplicate_count)

on_uniqueness = st.toggle('Проверить уникальность данных')
if on_uniqueness:
    uniqueness()


