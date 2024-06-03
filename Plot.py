import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def region_analyser(region):
    data=df[df['Location']==region]
    data=data.sort_values('Date_Time')
    data=data.reset_index()
    data=data.drop('index',axis=1)
    data=data.drop('Location',axis=1)
    data=data.set_index('Date_Time')
    return data


def feature_analyzer(region,feature,rows):
    data=region_analyser(region)
    
    plt.subplot(2,1,1)
    data[feature].head(rows).plot()
    plt.axhline(data[feature].mean(),color='k',linestyle='--',linewidth=2.5)
    plt.axhline(data[feature].median(),color='g',linestyle='--',linewidth=2.5)
    plt.axhline(data[feature].mode()[0],color='m',linestyle='--',linewidth=3)
    plt.legend()
    plt.grid()
    
    plt.subplot(2,1,2)
    sns.kdeplot(data[feature].head(rows))
    plt.axvline(data[feature].mean(),color='k',linestyle='--',linewidth=2.5)
    plt.axvline(data[feature].median(),color='g',linestyle='--',linewidth=2.5)
    plt.axvline(data[feature].mode()[0],color='m',linestyle='--',linewidth=3)
    plt.legend()
    plt.grid()
    
    plt.tight_layout()
    plt.show()

print("Note: Please use exact spellings wherever needed, while passing input. Thank you.\n\n")
df=pd.read_csv('weather_data.csv')

location=df['Location']
print(list(location.unique()))
region=input("\nFrom the above list choose any city: ")


print(list(df.columns))
feature=input("\nFrom the above list choose any attribute: ")

rows=int(input("\nEnter number of rows:"))
feature_analyzer(region,feature,rows)
