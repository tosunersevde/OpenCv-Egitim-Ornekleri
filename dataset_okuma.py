# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 11:19:08 2022

@author: tosun
"""

import pandas as pd

df = pd.read_excel("Date_Fruit_Datasets.xlsx")
# print(df.head(5))

numbers = pd.Series(df["Output"], dtype="category")
df["Numbers"] = numbers.astype("category")

df["Numbers"] = df["Numbers"].cat.rename_categories(
    ['0000','0001','0010','0011','0100','0101','0110'])

count = pd.value_counts(df["Output"])
df["Count"] = count

print(df)

number = df.groupby("Output").groups
name = df.groupby("Class").groups

number_table = {"Number":number,
                "Count":count}
table1 = pd.DataFrame(number_table)
print(table1)

name_table = {"Veriler":name}
table2 = pd.DataFrame(name_table)
print(table2)

# name_list = names.values
# print(name_list)

# number = pd.unique(df["Output"])
# print(number)

# numbers = pd.Categorical(df["Output"])
# print(numbers)

#binary donusum 
"""decimal = input("Sayı (Decimal) :")
binary = bin(int(decimal)).replace("0b", "")"""

"""decimal = []
binary = []
for i in range(897):
    decimal.append(df["Output"][i])
    binary.append(bin(int(decimal[i])))
    df["Output"][i] = binary[i]"""

"""df['Numbers'].rename_categories({0:'0000',
                                 1:'0001',
                                 2:'0010',
                                 3:'0011',
                                 4:'0100',
                                 5:'0101',
                                 6:'0110'})"""