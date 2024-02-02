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
pop_column = df_3_head[['POP']]
# print(pop_column)

# 6. select two columns of your choosing from the entire table. isolate that data.

pop_area = df_3_head[['POP', 'AREA']]
print(pop_area)

# 7. select rows from their indices (e.g. row 5 to 10).

# 8. select rows based on a condition, such as countries whose area is greater than 1000.

# 9. select specific columns containing rows selected based on a condition.

# 10. select rows and columns based on their names.

# 11. perform a two-dimensional selection based on indexes of both rows and columns.

# 12. Use conditions to store the population of all the European countries of the dataset in a european_pops variable.

# 13. sort the df_countries DataFrame by descending GDP, and print only the 10 countries with the highest GDP.

# 14. sort the df_countries DataFrame by continents in alphabetical order and descending area size.

# 15. assign new values using indices (create copy so original df is not modified).

# 16. create a new column from another column.

# 17. delete a column.

# 18. create new column SIZE. The value is Large if the area of the country is greater than 1M ^ 2 km and Small if less.
# Assigning new values can be useful in cases where we want to discretize quantitative data.

# 19. write table to a file.

# 20. read the countries data file in two halves.

# 21. combine both tables vertically (add rows).

# 22. combine tables horizontally (add columns).
# read documentation and try to understand the behaviour of possible values of 'how' argument in the merge() function.

# Summary statistics on the table:
#
# df.describe()
# df.describe()
# df.median(numeric_only=True)
# df['POP'].skew()
# df['GDP'].kurtosis()
# Task 23: do some research on what all these statistics represent if you don't know about them.

# 24. present in a new column of the table the density of population of every country in people per square meter.

# 25. what continent has the countries with the largest density of population on average?

# 26. why is it however not scientifically valid to answer this previous research question with our dataset?

# 27. get familiar with the pivot() and melt() functions from Pandas.
