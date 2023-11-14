import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# a program arranging the dataset of Nobel Laureates and preparing graphs and charts
if __name__ == '__main__':
    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # firts step: loading the dataset, deleting duplicates and rows with no gender and also setting a new index
    dataset = pd.read_json('./nobel_laureates.json')
    dataset.drop_duplicates(inplace=True)
    dataset.dropna(subset='gender', inplace=True)
    dataset.reset_index(drop=True, inplace=True)

    # second step: extracting the country of birth from place_of_birth column, filling empty born_in columns with it, dropping rows with no value, reseting index and modifying names of countries: USA and UK
    dataset['born_in'] = dataset['born_in'].apply(lambda x: None if x == '' else x)
    dataset['place_of_birth'] = dataset['place_of_birth'].apply(lambda x: x.split(',')[-1].strip() if (type(x) == str and ',' in x) else None)
    dataset['born_in'].fillna(dataset['place_of_birth'], inplace=True)
    dataset.dropna(subset='born_in', inplace=True, ignore_index=True)
    dataset['born_in'] = dataset['born_in'].apply(lambda x:  'USA' if x in ['US', 'United States', 'U.S.'] else x)
    dataset['born_in'] = dataset['born_in'].apply(lambda x:  'UK' if x == 'United Kingdom' else x)

    # third step: generating new column with year of birth extracted from date of birth and creating new column representing age of winning the prize
    dataset['year_born'] = dataset['date_of_birth'].str.extract(r'(\d{4})', expand=False).astype(int)
    dataset['age_of_winning'] = dataset['year'] - dataset['year_born']

    # fourth step: rearranging the colunm with country of births information and preparing a pie chart illustrating it
    dataset['born_in'] = dataset['born_in'].apply(lambda x:  'Other countries' if (dataset['born_in'].value_counts()[x] < 25) else x)

    data = dataset['born_in'].value_counts().tolist()
    labels = dataset['born_in'].value_counts().index.tolist()
    colors = ['blue', 'orange', 'red', 'yellow', 'green', 'pink', 'brown', 'cyan', 'purple']
    explode = [0.0, 0.0, 0.0, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08]

    plt.figure(figsize=(12, 12))
    plt.pie(data, labels=labels, colors=colors, explode=explode, autopct=lambda p: '{:.2f}%  ({:,.0f})'.format(p,p * sum(data)/100))
    plt.show()

    # fifth step: deleting rows with no category value and preparing a bar chart illustrating distribution of female and male winners according to the category
    dataset['category'] = dataset['category'].apply(lambda x: None if x == '' else x)
    dataset.dropna(subset='category', inplace=True)
    category_dict = dataset.groupby(['category']).agg({'gender': 'value_counts'}).to_dict()['gender']
    categories = [category[0] for category in category_dict][::2]
    males = [category_dict[category] for category in category_dict if category[1] == 'male']
    females = [category_dict[category] for category in category_dict if category[1] == 'female']

    x_axis = np.arange(len(categories))
    plt.figure(figsize=(10, 10))
    plt.bar(x_axis-0.2, males, width=0.4, label='Males', color='blue')
    plt.bar(x_axis+0.2, females, width=0.4, label='Females', color='crimson')
    plt.xticks(x_axis, categories)
    plt.xlabel('Category', fontsize=14)
    plt.ylabel('Nobel Laureates Count', fontsize=14)
    plt.title('The total count of male and female Nobel Prize winners by categories', fontsize=20)
    plt.legend()

    plt.show()

    # sixth step: generating a box plot for ages of getting the Nobel Prize for each category
    ages_list = [dataset.loc[dataset.category==x, 'age_of_winning'] for x in categories]
    data_1 = ages_list[0].to_list()
    data_2 = ages_list[1].to_list()
    data_3 = ages_list[2].to_list()
    data_4 = ages_list[3].to_list()
    data_5 = ages_list[4].to_list()
    data_6 = ages_list[5].to_list()
    data_7 = data_1 + data_2 + data_3 + data_4 + data_5 + data_6

    data = [data_1, data_2, data_3, data_4, data_5, data_6, data_7]
    categories.append('All categories')
    plt.figure(figsize=(10, 10))

    plt.boxplot(data, labels=categories, showmeans=True)

    plt.ylabel('Age of Obtaining the Nobel Prize', fontsize=14)
    plt.xlabel('Category', fontsize=14)
    plt.title('Distribution of Ages by Category', fontsize=20)

    plt.show()
