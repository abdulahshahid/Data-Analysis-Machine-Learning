import matplotlib.pyplot as plt
import pandas as pd
from texttable import Texttable
df = pd.read_csv('Gapminder.csv')
''' at that step i am going to to make duplicate of dataframe which i will use in dictionary '''
ddf = pd.read_csv('Gapminder.csv')
ddf.fillna(value=0, method=None, axis=None, inplace=True, limit=None, downcast=None)
ddf = ddf.drop(['Country', 'Region-Geo', 'Continent', 'Region', 'Year', 'Year_cat', ], axis=1)
allvalues = ddf.values
print(allvalues)
Judging_Values = list(df.head(0))
judging_2 = Judging_Values.copy()
for i in range(0, 6):
    Judging_Values.remove(judging_2[i])
Judging_Factors = Judging_Values
df.fillna(0)
alldata = df.values
countries_name = list(alldata[:, 0])
Continent = alldata[:, 2]
Sorted_Continents = list(set(Continent))
years = list(alldata[:, 4])
Sort_Year_1 = sorted(set(years))
required_indicators_buray = ['Inflation', 'ChildrenPerWoman', 'Imports', 'Populationgrowth', 'Poverty']
required_indicators_achy = ['IncomePerPerson', 'Literacyrateadulttotal', 'Exports', 'Taxrevenue']
my_all_countries_dict = {}
my_country_dict = {}
my_one_country_dict = []
average_finding_list = []
continent_rank = []
all_Pakistan_indicators_average_burii = []
all_Pakistan_indicators_average_achi = []
my_countries_list = []
Sort_Year = []
my_countries_list_1 = []
mine = []
Global_rank = []
tablerank = []
tablelist = []
rank = 1
my_continent_average_per_indicator = []
my_continent_average_per_indicator_final = []
for i in range(len(countries_name)):
    my_all_countries_dict[countries_name[i], years[i]] = allvalues[i, :]
for l in range(len(Sort_Year_1)):
    my_one_country_dict.append(my_all_countries_dict['Pakistan', Sort_Year_1[l]])
for n in required_indicators_buray:
    for m in my_one_country_dict:
        average_finding_list.append(m[Judging_Values.index(n)])
        average = sum(average_finding_list) / len(average_finding_list)
    for o in range(len(average_finding_list)):
        if average_finding_list[o] == 0:
            average_finding_list[o] = average
        else:
            average_finding_list[o] = average_finding_list[o]
    required_average = sum(average_finding_list) / len(average_finding_list)
    all_Pakistan_indicators_average_burii.append(required_average)
    average_finding_list = []
    required_average = 0000
for n in required_indicators_achy:
    for m in my_one_country_dict:
        average_finding_list.append(m[Judging_Values.index(n)])
        average = sum(average_finding_list) / len(average_finding_list)
    for o in range(len(average_finding_list)):
        if average_finding_list[o] == 0:
            average_finding_list[o] = average
        else:
            average_finding_list[o] = average_finding_list[o]
    required_average = sum(average_finding_list) / len(average_finding_list)
    all_Pakistan_indicators_average_achi.append(required_average)
    average_finding_list = []
    required_average = 0000
for A in range(len(Sorted_Continents)):
    tablelist = []
    for B in range(len(Continent)):
        if Continent[B] == Sorted_Continents[A]:
            my_countries_list.append(countries_name[B])
        my_countries_list_1 = list(set(my_countries_list))
        my_one_country_dict = []
        average = 0
        average_finding_list = []
    for K in range(len(required_indicators_buray)):
        tablerank = []
        for D in range(len(my_countries_list_1)):
            for U in range(len(countries_name)):
                if countries_name[U] == my_countries_list_1[D]:
                    Sort_Year.append(years[U])
            for L in Sort_Year:
                my_one_country_dict.append(my_all_countries_dict[my_countries_list_1[D], L])
            Sort_Year = []
            for M in my_one_country_dict:
                average_finding_list.append(M[Judging_Values.index(required_indicators_buray[K])])
                average = sum(average_finding_list) / len(average_finding_list)
            for Z in range(len(average_finding_list)):
                if average_finding_list[Z] == 0:
                    average_finding_list[Z] = average
                else:
                    average_finding_list[Z] = average_finding_list[Z]
            required_average = sum(average_finding_list) / len(average_finding_list)
            my_continent_average_per_indicator.append(required_average)
            average_finding_list = []
            average = 0
            my_one_country_dict = []
        my_continent_average_per_indicator.append(all_Pakistan_indicators_average_burii[K])
        my_continent_average_per_indicator.sort()
        for H in my_continent_average_per_indicator:
            if H == all_Pakistan_indicators_average_burii[K]:
                tablerank.append(rank)
                tablerank.append(required_indicators_buray[K])
                tablerank.append(Sorted_Continents[A])
                tablelist.append(tablerank)
                continent_rank.append(rank)
                break
            else:
                rank += 1
        rank = 000
        my_continent_average_per_indicator_final = []
        required_average = 0
        my_continent_average_per_indicator = []
    Global_rank.append(int(sum(continent_rank) / len(required_indicators_buray)))
    table = Texttable()
    table.add_rows(tablelist)
    table.header(['Rank', 'Indicators', 'Continent'])
    print(table.draw())
    print(int(sum(continent_rank) / len(required_indicators_buray)), 'is rank of Pakistan in', Sorted_Continents[A], 'for number of countries:', len(my_countries_list_1))
    print('************************************************************************************************************************************************************')
    continent_rank = []
    my_countries_list_1 = []
    my_countries_list = []
print('TIME OF WAITING HAS COME TO END. NOW TIME FOR GLOBAL RANKING OF PAKISTAN!!!. ARE YOU READY TO KNOW THE CONDITION OF YOUR COUNTRY!!!')
print(sum(Global_rank), 'is the global rank of Pakistan out of  :', len(set(countries_name)), 'Countries')
print('Remember rank number 1 will given to that country which has minimum average of burii values')
print('************************************************************************************************************************************************************')
for i in range(len(Global_rank)):
    plt.bar(Sorted_Continents[i], Global_rank[i], label=Sorted_Continents[i], width=0.5)
plt.title('Continent wise global ranking of Pakistan for buray indicators!!', fontweight='bold', fontsize=20)
plt.xlabel('close it to see more!!', fontweight='bold')
plt.show()
Global_rank = []
for A in range(len(Sorted_Continents)):
    tablelist = []
    for B in range(len(Continent)):
        if Continent[B] == Sorted_Continents[A]:
            my_countries_list.append(countries_name[B])
        my_countries_list_1 = list(set(my_countries_list))
        my_one_country_dict = []
        average = 0
        average_finding_list = []
    for K in range(len(required_indicators_achy)):
        tablerank = []
        for D in range(len(my_countries_list_1)):
            for U in range(len(countries_name)):
                if countries_name[U] == my_countries_list_1[D]:
                    Sort_Year.append(years[U])
            for L in Sort_Year:
                my_one_country_dict.append(my_all_countries_dict[my_countries_list_1[D], L])
            Sort_Year = []
            for M in my_one_country_dict:
                average_finding_list.append(M[Judging_Values.index(required_indicators_achy[K])])
                average = sum(average_finding_list) / len(average_finding_list)
            for Z in range(len(average_finding_list)):
                if average_finding_list[Z] == 0:
                    average_finding_list[Z] = average
                else:
                    average_finding_list[Z] = average_finding_list[Z]
            required_average = sum(average_finding_list) / len(average_finding_list)
            my_continent_average_per_indicator.append(required_average)
            average_finding_list = []
            average = 0
            my_one_country_dict = []
        my_continent_average_per_indicator.append(all_Pakistan_indicators_average_achi[K])
        my_continent_average_per_indicator.sort()
        my_continent_average_per_indicator.reverse()
        for H in my_continent_average_per_indicator:
            if H == all_Pakistan_indicators_average_achi[K]:
                tablerank.append(rank)
                tablerank.append(required_indicators_achy[K])
                tablerank.append(Sorted_Continents[A])
                tablelist.append(tablerank)
                continent_rank.append(rank)
                break
            else:
                rank += 1
        rank = 000
        my_continent_average_per_indicator_final = []
        required_average = 0
        my_continent_average_per_indicator = []
    Global_rank.append(int(sum(continent_rank) / len(required_indicators_achy)))
    table = Texttable()
    table.add_rows(tablelist)
    table.header(['Rank', 'Indicators', 'Continent'])
    print(table.draw())
    print(int(sum(continent_rank) / len(required_indicators_achy)), 'is rank of Pakistan in', Sorted_Continents[A], 'for number of countries:', len(my_countries_list_1))
    print('************************************************************************************************************************************************************')
    continent_rank = []
    my_countries_list_1 = []
    my_countries_list = []
print('TIME OF WAITING HAS COME TO END. NOW TIME FOR GLOBAL RANKING OF PAKISTAN!!!. ARE YOU READY TO KNOW THE CONDITION OF YOUR COUNTRY!!!')
print(sum(Global_rank), 'is the global rank of Pakistan out of  :', len(set(countries_name)), 'Countries in those values by increasing of such values country will go up')
print('First rank will given to that country which has max average of achi values e,g Taxrevenue')
print('************************************************************************************************************************************************************')
for i in range(len(Global_rank)):
    plt.bar(Sorted_Continents[i], Global_rank[i], label=Sorted_Continents[i], width=0.5)
plt.title('Continent wise global ranking of Pakistan for achyy indicators', fontweight='bold', fontsize=20)
plt.show()
