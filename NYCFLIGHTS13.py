Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> def main():
    flights_dataframe = pd.read_csv('C:\\Users\\Camil\\OneDrive\\Desktop\\flights.csv')
    airline_dataframe = pd.read_csv('C:\\Users\\Camil\\OneDrive\\Desktop\\airlines.csv')

    joined_dataframe = pd.merge(flights_dataframe, airline_dataframe, on='carrier')
    data_top = joined_dataframe.columns
    print(joined_dataframe)
    drop_rows = []
    for index, row in joined_dataframe.iterrows():
        for i in data_top:
            if(pd.isnull(row[i])):
                drop_rows.append(index)
                break

    dropped_data_frame = joined_dataframe.drop(drop_rows)
    print(dropped_data_frame)

    
>>> main()
        year  month  day  ...  minute            time_hour                   name
0       2013      1    1  ...      15  2013-01-01 05:00:00  United Air Lines Inc.
1       2013      1    1  ...      29  2013-01-01 05:00:00  United Air Lines Inc.
2       2013      1    1  ...      58  2013-01-01 05:00:00  United Air Lines Inc.
3       2013      1    1  ...       0  2013-01-01 06:00:00  United Air Lines Inc.
4       2013      1    1  ...       0  2013-01-01 06:00:00  United Air Lines Inc.
...      ...    ...  ...  ...     ...                  ...                    ...
336771  2013      9   19  ...       5  2013-09-19 18:00:00  SkyWest Airlines Inc.
336772  2013      9   20  ...       5  2013-09-20 18:00:00  SkyWest Airlines Inc.
336773  2013      9   22  ...       5  2013-09-22 18:00:00  SkyWest Airlines Inc.
336774  2013      9   23  ...       5  2013-09-23 18:00:00  SkyWest Airlines Inc.
336775  2013      9   24  ...       5  2013-09-24 18:00:00  SkyWest Airlines Inc.

[336776 rows x 20 columns]
