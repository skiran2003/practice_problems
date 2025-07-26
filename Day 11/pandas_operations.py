import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_json("cars.json")
# Finding mean of the records in a column
mean=data['range_km'].mean()
# Finding median of the records in a column
median=data['seating'].median()
# Finding mode of the records in a column
mode=data['price_inr_lakh'].mode()[0]
# Replacing the null values with mean, median and mode
data.fillna({'seating':median},inplace=True)
data.fillna({'range_km':mean},inplace=True)
data.fillna({'price_inr_lakh':mode},inplace=True)

print(data.duplicated().sum()) # Finds number of duplicate rows in the dataset
print(data.isna().sum()) # Finds number of null rows in the dataset
# Deleting column from the dataset (axis=1:Columns, axis=0:Rows)
data.drop(['price_usd','launch_date'],axis=1,inplace=True)
print(data)

# Sorting the records in ascending or descending order
data.sort_values('price_inr_lakh',ascending=False,inplace=True)
# Sorting records using multiple columns
data.sort_values(['range_km','seating'],ascending=(True,False),inplace=True)
print(data)

# Plotting a graph between two columns
x=data['model']
y=data['price_inr_lakh']
data.plot(kind='barh',x=x,y=y,labels=('model','price'))
plt.show()

