import pandas as pd


def main():
    census_population_dataframe = pd.read_csv('state-populations.csv')
    census_regions_dataframe = pd.read_csv('census-divisions.csv')

    census = pd.merge(census_population_dataframe, census_regions_dataframe, on='state')

    print(census)
    print()

    reshaped_frame = pd.melt(census, id_vars=['state'], var_name='year', value_name='population')
    print(reshaped_frame)
    print()

    print("group the data by 2010: ")
    print()
    grouped_frame = census.groupby('2010')
    print(grouped_frame.first())
    print()

    print("Summary after grouped by 2010 ")
    print()
    print(grouped_frame.describe())
    print()

    print("group the data by 2011: ")
    print()
    grouped_frame = census.groupby('2011')
    print(grouped_frame.first())
    print()

    print("Summary after grouped by 2011 ")
    print()
    print(grouped_frame.describe())
    print()

    print("group the data by 2012: ")
    print()
    grouped_frame = census.groupby('2012')
    print(grouped_frame.first())
    print()

    print("Summary after grouped by 2012 ")
    print()
    print(grouped_frame.describe())
    print()

    print("group the data by 2013: ")
    print()
    grouped_frame = census.groupby('2013')
    print(grouped_frame.first())
    print()

    print("Summary after grouped by 2013 ")
    print()
    print(grouped_frame.describe())
    print()

    print("group the data by 2014: ")
    print()
    grouped_frame = census.groupby('2014')
    print(grouped_frame.first())
    print()

    print("Summary after grouped by 2014 ")
    print()
    print(grouped_frame.describe())
    print()

    print("group the data by 2015: ")
    print()
    grouped_frame = census.groupby('2015')
    print(grouped_frame.first())
    print()

    print("Summary after grouped by 2015 ")
    print()
    print(grouped_frame.describe())
    print()

    print("group the data by 2016: ")
    print()
    grouped_frame = census.groupby('2016')
    print(grouped_frame.first())
    print()

    print("Summary after grouped by 2016 ")
    print()
    print(grouped_frame.describe())
    print()

    print("group the data by region ")
    print()
    grouped_frame = census.groupby('region')
    print(grouped_frame.first())
    print()

    print("Summary after grouped by region ")
    print()
    print(grouped_frame.describe())
    print()

    print("group the data by division ")
    print()
    grouped_frame = census.groupby('division')
    print(grouped_frame.first())
    print()

    print("Summary after grouped by division ")
    print()
    print(grouped_frame.describe())
    print()


main()
