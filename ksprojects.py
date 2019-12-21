
import pandas as pd
from tabulate import tabulate

def main():

    dataframe = pd.read_csv('ksprojects.csv')
    numberOfRows = dataframe.shape[0]
    print("Number of rows: ", numberOfRows)
    print()

    data_top = dataframe.columns
    tempData = []
    for coloum in data_top:
        onedata=[]
        onedata.append(coloum)
        onedata.append(dataframe[coloum].dtype)
        tempData.append(onedata)

    print(tabulate(tempData, headers=['Name', 'Data type']))
    print()
    if(checknullnals(dataframe)):
        print("there are null values")
    else:
        print("No any null values")
    print()

    tempDataFrame = dataframe.copy()
    tempDataFrame.sort_values(by=['pledged'], inplace=True, ascending=False)

    succesfulldocumentryprojectpledges = []
    average_per_backer = []
    for index, row in tempDataFrame.iterrows():
        if row['backers'] != 0:
            average = row['pledged']/row['backers']
            average_per_backer.append(average)
        else:
            average_per_backer.append(None)

        if(row['category']=="Documentary" and row['state']=="successful"):
            succesfulldocumentryprojectpledges.append(row['pledged'])

    print("top 10 highest pledges")
    print()
    for i in range(10):
        print(succesfulldocumentryprojectpledges[i])

    print()
    tempDataFrame['average_per_backer'] = average_per_backer

    print(tempDataFrame)
    print()

    droping_indexes = []
    for index, row in dataframe.iterrows():
        if row['backers'] == 0:
            droping_indexes.append(index)

    dropped_data_frame = dataframe.drop(droping_indexes)
    print()

    average_per_backer = []
    for index, row in dropped_data_frame.iterrows():
        average = row['pledged']/row['backers']
        average_per_backer.append(average)

    dropped_data_frame['average_per_backer'] = average_per_backer
    print(dropped_data_frame)
    print()

    cross_tabbed_frame = pd.crosstab(dataframe.category, dataframe.state)
    print("Count of records: ", cross_tabbed_frame.shape[0])

def checknullnals(dataframe):
    for coloum in dataframe:
        for data in dataframe[coloum]:
            if data is None:
                return True

    return False


main()
