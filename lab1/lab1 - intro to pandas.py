# 'pandas' is used for data manipulation and analysis.
# see pandas dataframe documentation here: https://pandas.pydata.org/docs/reference/frame.html

import pandas as pd

# 1. create a dataframe with two columns 'col1' and 'col2'.
d = {'Name': ['Tom', 'Dick', 'Harry'], 'Age': [6, 7, 8]}
df = pd.DataFrame(data=d, index=[i for i in range(len(d['Name']))])
# print(df)

d_1 = {'col1': [0, 1], 'col2': [2, 3]}
df_1 = pd.DataFrame(data=d_1)
# print(df_1)

# 2. read the csv file containing country data and manually create new dataframe with it.

with open("countries.csv", 'r') as countries_file:
    headers = countries_file.readline().strip().split(',')
    d_2 = {header: [] for header in headers}
    for line in countries_file:
        row_values = line.strip().split(',')
        for i, header in enumerate(headers):
            d_2[header].append(row_values[i])

df_2 = pd.DataFrame(data=d_2)
# print(df_2)

# 3. repeat task 2 but using the pandas function to create dataframes from csv.
df_3 = pd.read_csv("countries.csv")
# print(df_3)

# 4. there is a pandas function, head(). use it to select top rows from table (default is 5).
df_3_head = df_3.head(10)
# print(df_3_head)

# 5. select one column. This is also called a series object.
pop_series = df_3_head[['POP']]
# print(pop_series)

# 6. select two columns of your choosing from the entire table. isolate that data.
df_pop_area = df_3_head[['POP', 'AREA']]
# print(df_pop_area)

# 7. select rows from their indices (e.g. row 5 to 10).
# print(df_3.iloc[5:10])

# 8. select rows based on a condition, such as countries whose area is greater than 1000.
df_biggest_countries = df_3[df_3['AREA'] > 1000]
# print(df_biggest_countries)

# 9. select specific columns containing rows selected based on a condition.
df_pop_area_biggest_countries = df_3.loc[df_3['AREA'] > 1000, ['POP', 'AREA']]
# print(df_pop_area_biggest_countries)

# 10. select rows and columns based on their country names.
df_countries_indices = df_3.rename(index=df_3['COUNTRY'])  # rename index by countries.
# print(df_countries_indices.loc[['UK', 'France'], ['POP', 'AREA']])

# 11. perform a two-dimensional selection based on indexes of both rows and columns.
# print(df_3.iloc[5:10, 2:4])

# 12. Use conditions to store the population of all the European countries of the dataset in a european_pops variable.
european_pops = df_3.loc[df_3['CONT'] == "Europe", ['COUNTRY', 'POP']]
# print(european_pops)

# 13. sort the df_countries DataFrame by descending GDP, and print only the 10 countries with the highest GDP.
df_gpd_sort = df_3.sort_values(by=['GDP'], ascending=False)
# print(df_gpd_sort.head(10))
# 14. sort the df_countries DataFrame by continents in alphabetical order and descending area size.
df_area_cont_sort = df_3.sort_values(by=['CONT', 'AREA'], ascending=(True, False))
# print(df_area_cont_sort)

# 15. assign new values using indices (create copy so original df is not modified).
df_countries_post_2022 = df_3.copy()
df_countries_post_2022.loc[df_countries_post_2022['COUNTRY'] == 'UK', 'CONT'] = 'Brexit'
# print(df_countries_post_2022)

# 16. create a new column from another column.
df_countries_post_2022['AREA_SQUARE_KM'] = df_countries_post_2022['AREA'] * 1000
# print(df_countries_post_2022)

# 17. delete a column.
df_countries_post_2022 = df_countries_post_2022.drop(columns=['AREA'])
# print(df_countries_post_2022)

# 18. create new column SIZE. The value is Large if the area of the country is greater than 1M ^ 2 km and Small if less.
# Assigning new values can be useful in cases where we want to discretize quantitative data.
df_countries_post_2022['SIZE'] = ""
df_countries_post_2022.loc[df_countries_post_2022['AREA_SQUARE_KM'] > 1000000, 'SIZE'] = 'Large'
df_countries_post_2022.loc[df_countries_post_2022['AREA_SQUARE_KM'] < 1000000, 'SIZE'] = 'Small'
# print(df_countries_post_2022)

# 19. write table to a file.
# df_countries_post_2022.to_csv("countries_new.csv", index=False)

# 20. read the countries data file in two halves.
df_countries_1 = pd.read_csv("countries_new.csv", nrows=10)
df_countries_2 = pd.read_csv("countries_new.csv", skiprows=range(1, 11))

# print(df_countries_1.shape)
# print(df_countries_2.shape)

# 21. combine both tables vertically (add rows).

df_countries_new = pd.concat([df_countries_1, df_countries_2]).reset_index(drop=True)
# print(df_countries_new)

# 22. combine tables horizontally (add columns).
# read documentation and try to understand the behaviour of possible values of 'how' argument in the merge() function.
df_4 = df_3[['COUNTRY', 'POP']].sort_values(by='POP').iloc[5:]
df_5 = df_3[['COUNTRY', 'GDP', 'AREA']]
df_6 = pd.merge(df_4, df_5, on='COUNTRY', how='inner')
# print(df_6)

# Summary statistics on the table:
# print(df_countries_post_2022.describe())
# print(df_countries_post_2022.median(numeric_only=True))
# print(df_countries_post_2022['POP'].skew())
# print(df_countries_post_2022['GDP'].kurtosis())

# Task 23: do some research on what all these statistics represent if you don't know about them.

# 24. present in a new column of the table the density of population of every country in people per square meter.
df_3['POPULATION DENSITY'] = df_3['AREA']/df_3['POP']
print(df_3)

# 25. what continent has the countries with the largest density of population on average?

# 26. why is it however not scientifically valid to answer this previous research question with our dataset?

# 27. get familiar with the pivot() and melt() functions from Pandas.
