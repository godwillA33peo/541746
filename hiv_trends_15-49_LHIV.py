#!/usr/bin/env python
# coding: utf-8

import pandas as pd #for loading and wrangling the data
import bar_chart_race as bcr # for making the bar chart race (animation)


#loading the CSV data 
data = pd.read_csv("hivpr.csv", index_col="Country Name")

#taking a a look at the data
data.head()

#changing the orientation of the datafame
data = data.transpose()
data.head()

#dropping rows that won't be used for the animation
data.drop(["Country Code", "Series Name", "Series Code"], inplace = True)

#listing the regions that are in the data set so that i do not include them in the animation
regions = ["Africa Eastern and Southern", "Africa Western and Central", "East Asia & Pacific",
                           "East Asia & Pacific (IDA & IBRD countries)", "Euro area", "Europe & Central Asia (excluding high income)",
                           "European Union", "Fragile and conflict affected situations", "IDA & IBRD total","IDA only",
                           "Latin America & Caribbean", "Latin America & the Caribbean (IDA & IBRD countries)",
                           "Low & middle income", "Lower middle income", "Macao SAR, China", "Middle East & North Africa",
                           "Middle East & North Africa (IDA & IBRD countries)","North America","OECD members",
                           "Other small states","Pre-demographic dividend","Small states","South Asia",
                           "St. Vincent and the Grenadines","Sub-Saharan Africa (IDA & IBRD countries)",
                           "Turks and Caicos Islands","Upper middle income","West Bank and Gaza","World"
                          ]

#dropping the above columns
data = data.drop(columns = regions)

data.head()

#converting the year column into a python date object and making it the index
data.index = pd.to_datetime(data.index)

# checking the data type of the dataframe
data.dtypes

#converting int a floating data type so it can be use for the animation
data = data.astype(float)
data.dtypes

#bar cahrt race function
bcr.bar_chart_race(df=data, n_bars=10, filter_column_colors= True, figsize=(5, 3),
                    period_length= 700, bar_size=0.7, period_fmt="%Y",
                    cmap="dark12",
                    title="Prevalence of HIV, total (% of population ages 15-49), UNAIDS estimates.",
                    title_size='8',
                    bar_label_size=7
                )



