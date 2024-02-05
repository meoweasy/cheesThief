# Бандитский Сыроград

## Разведочный анализ данных
Перед тем, как начать анализировать, необходимо данные привести к нормальной форме, а именно:
* Посмотреть полноту данных, тоесть проверить есть ли нулевые значения. При работе с моделями очень важно, чтобы не было пустых значений, они могут исказить предсказание или выдвать не совсем точное значение, ухудшать точность модели.
* Проверить данные на уникальность, тоесть проверить нет ли повторяющихся строчек данных. Это так же влияет на точность анализа.

Технологии, которые я использую для разведки:
* python 3.9
* библиотека pandas для работы с файлами формата .csv
* библиотека streamlit для удобного отображения данных

Первым делом было замечено, что 3 первых столбца в датасетах идентичны, поэтому логично было бы их объеденить в один датасет. Для этого был реализован метод `save_main_dataset()`. Здесь считываются 2 исходных датасета и с помощью функции `merge` библиотеки pandas объединяются 2 датасета в один со сдвигом влево и данные сохраняются в новый датасет.

```python
def save_main_dataset():
    first_data = pd.read_csv('datasets/first_part.csv')
    second_data = pd.read_csv('datasets/second_part.csv')

    main_dataset = pd.merge(first_data, second_data[
        ['Date', 'District', 'Warehouse_Name', 'Percent_of_Crime_Solved', 'Number_of_Lights']],
                            on=['Date', 'District', 'Warehouse_Name'],
                            how='left')
    main_dataset.to_csv('datasets/main_dataset.csv', index=False)
```

Для оценки полноты данных создан метод `completeness()`. Здесь, с помощью функции `data.isnull().values.any():` просматриваем есть ли пустые значения. И выводим сумму всех пустых значений в каждом столбце с помощью функции `data.isnull().sum()`.

```python
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
```

Для проверки уникальности значений был создан метод `uniqueness()`. Здесь проверяем есть ли дубликаты с помощью метода `data.duplicated().any()`. Так же выводим кол-во повторяющихся строчек с помощью метода `data.duplicated().sum()`.

```python
def uniqueness():
    data = pd.read_csv('datasets/main_dataset.csv')

    if data.duplicated().any():
        st.write("В датасете есть дубликаты.")
    else:
        st.write("В датасете нет дубликатов.")

    duplicate_count = data.duplicated().sum()
    st.write("Количество дубликатов в датасете:", duplicate_count)
```
**Что же получается?**
Получился вот такой датасет после объединения

![Изображение](image/1.png "Объединенный датасет")

**А что с полнотой и уникальностью?**
Методы вывели следующую информацию

![Изображение](image/2.png "Результаты")

### Вывод по разведке и ответ на первый вопрос
* Данные представлены в полном объеме
* Данные не имеют повторяющихся значений

Можно сказать, что данные готовы к последующему анализу. Пока сложно оценить насколько эффективны собранные данные, необходимо создать модели анализа данных и оценить как каждый параметр влияет на другой параметр (решение в слеующем разделе и относится уже к 2 вопросу). 

## Реализация анализа данных. Достижение бизнес-цели
