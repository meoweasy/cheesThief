import pandas as pd
import streamlit as st
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm
import numpy as np

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

on_describe = st.toggle('Посмотреть данные по параметрам')
if on_describe:
    st.write(main_data.describe())

def correl():
    main_data['Date'] = pd.to_datetime(main_data['Date'])
    le_district = LabelEncoder()
    main_data['District'] = le_district.fit_transform(main_data['District'])

    le_warehouse = LabelEncoder()
    main_data['Warehouse_Name'] = le_warehouse.fit_transform(main_data['Warehouse_Name'])
    correlation_matrix = main_data.corr()

    fig, ax = plt.subplots(figsize=(10, 8))
    scatter_plot = sns.pairplot(main_data, height=2, aspect=1.5)
    st.pyplot(scatter_plot)

on_corr = st.toggle("Посмотреть корреляцию")
if on_corr:
    correl()


def correl2():
    df = pd.read_csv('datasets/main_dataset.csv')
    filtered_df = df[(df['Warehouse_Name'] == 'Сметанинковы') & (df['District'] == 'Петрокотский') ]

    filtered_df = filtered_df.drop(['Date'], axis=1)
    st.write(filtered_df)

    le_district = LabelEncoder()
    filtered_df['District'] = le_district.fit_transform(filtered_df['District'])

    le_warehouse = LabelEncoder()
    filtered_df['Warehouse_Name'] = le_warehouse.fit_transform(filtered_df['Warehouse_Name'])
    correlation_matrix = filtered_df.corr()

    fig, ax = plt.subplots(figsize=(10, 8))
    scatter_plot = sns.pairplot(filtered_df, height=2, aspect=1.5)
    st.pyplot(scatter_plot)

on_corr2 = st.toggle("Посмотреть корреляцию для определенного склада и района")
if on_corr2:
    correl2()
