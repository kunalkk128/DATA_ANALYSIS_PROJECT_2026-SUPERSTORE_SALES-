import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\kacha\OneDrive\दस्तऐवज\project csv files or code\RAW & UNCLEANED.CSV",encoding='utf-8-sig')
print("\033[1;33mShows the original dataset:\033[0m\n")
print(df)

print("\033[1;33m\nShows first 10 rows of the dataset:\033[0m\n")
print(df.head(10))#shows first 10 rows of the dataset

print("\033[1;33m\nShows the information of the dataset:\033[0m\n")
print(df.info()) #shows the information of the dataset

print("\033[1;33m\nShows the data types of the dataset:\033[0m\n")
print(df.dtypes) #shows the data types 

print("\033[1;33mShows the missing values in the dataset:\033[0m\n")
print(df.isnull().sum()) #shows the missing values in the dataset

print("\033[1;33mRemoves the duplicated values in the dataset:\033[0m\n")
df.drop_duplicates(inplace=True)
print (df.to_csv(r"C:\Users\kacha\OneDrive\दस्तऐवज\project csv files or code\RAW & UNCLEANED.CSV",index=False))

print("\033[1;33m\nDuplicates removed and file saved successfully!\033[0m\n")

sales_array = df['Sales'].to_numpy()
profit_array = df['Profit'].to_numpy()
quantity_array = df['Quantity'].to_numpy()
discount_array = df['Discount'].to_numpy()

print("\033[1;33m\nShows the sales, profit, quantity and discount arrays:\033[0m\n")

print("\nSales Array:", sales_array[:10]) 
print("\nProfit Array:", profit_array[:10])
print("\nQuantity Array:", quantity_array[:10])
print("\nDiscount Array:", discount_array[:10])

print("\033[1;36m\nshows the mean of sales:\033[0m\n")

print("mean of sales:", np.mean(sales_array))
print("mean of sales:", np.mean(profit_array))
print("mean of sales:", np.mean(quantity_array))
print("mean of sales:", np.mean(discount_array))

print("\033[1;36m\nshows the median of sales:\033[0m\n")

print("median of sales:", np.median(sales_array))
print("median of profit:", np.median(profit_array))
print("median of quantity:", np.median(quantity_array))
print("median of discount:", np.median(discount_array))

print("\033[1;36m\nshows the standard deviation of sales:\033[0m\n")

print("standard deviation of sales:", np.std(sales_array))
print("standard deviation of sales:", np.std(profit_array))
print("standard deviation of sales:", np.std(quantity_array))
print("standard deviation of sales:", np.std(discount_array))

print("\033[1;36m\nshows the minimum of sales:\033[0m\n")

print("minimum of sales:", np.min(sales_array))
print("minimum of sales:", np.min(profit_array))
print("minimum of sales:", np.min(quantity_array))
print("minimum of sales:", np.min(discount_array))

print("033[1;36m\nshows the maximum of sales:\033[0m\n")

print("maximum of sales:", np.max(sales_array))
print("maximum of profit:", np.max(profit_array))
print("maximum of quantity:", np.max(quantity_array))
print("maximum of discount:", np.max(discount_array))

df=df.dropna() #removes the missing values in the dataset
print("\033[1;33m\nData frame after removing missing values:\033[0m\n")
print (df.to_csv(r"C:\Users\kacha\OneDrive\दस्तऐवज\project csv files or code\RAW & UNCLEANED.CSV",index=False))

print("\033[1;33mShows the missing values in the dataset:\033[0m\n")
print(df.isnull().sum()) #shows the missing values in the dataset

# shows data only 500 + in And condition.
print("\033[1;33m\nfiltered_data And condition :\033[0m\n")
filtered_data = df[(df['Sales'] > 500) & (df['Profit'] > 50)]
print(print(filtered_data[['Order ID', 'Sales', 'Profit']]))

print("\033[1;33m\n--- SORTING DATA ---\033[0m")
# sorting sales data high to low 
sorted_df = df.sort_values(by='Sales', ascending=False)
print(sorted_df[['Order ID', 'Sales', 'Profit']].head(10))


print("\033[1;33m\n--- GROUPBY OPERATIONS ---\033[0m")
# Country wise Total Sales aur Total Profit
Country_summary = df.groupby('Country')[['Sales', 'Profit']].sum()
print("\033[1;36mTotal Sales & Profit by Country:\033[0m")
print(Country_summary)

print("\033[1;34mCurrent Rows Count:\033[0m", len(df))
print("\033[1;35m\n---Aggregation Operations ---:\033[0m")
agg_summary = df.groupby('Country').agg({'Sales': ['sum', 'mean', 'max'],
                                         'Profit': ['sum', 'mean', 'max'],
                                         'Quantity':['count',],
                                         'Discount': ['max', 'min']})
print(agg_summary.head(10))



print("\033[1;35m\n--- PIVOT TABLE OPERATIONS ---\033[0m\n")
# Pivot table creation:
pivot_df = pd.pivot_table(
    df, 
    values=['Sales', 'Profit'], 
    index='Country', 
    aggfunc='sum'
)
print(pivot_df.head(15))


print("\033[1;35m\n--- MERGE OPERATIONS (WITHOUT EXTRA CSV) ---\033[0m")
# created Same df form 2 different small DataFrames.
df_sales = df[['Order ID', 'Sales', 'Profit']]
df_customer = df[['Order ID', 'Customer Name', 'Country']]

# merging the two DataFrames on 'Order ID' column using inner join
merged_df = pd.merge(df_sales, df_customer, on='Order ID', how='inner')
print("\033[1;36mMerged Result (Combined from same file):\033[0m")
print(merged_df.head())


print("\033[1;35m\n--- FEATURE ENGINEERING ---\033[0m")

df['total']=df['Sales']+ df['Profit']
df['profit_margin'] = df['Profit'] / df['Sales']
print("\033[1;36m\nFeature Engineering Result:\033[0m")
print(df[['Order ID', 'total', 'profit_margin']].head())
print (df.to_csv(r"C:\Users\kacha\OneDrive\दस्तऐवज\project csv files or code\RAW & UNCLEANED.CSV",index=False))
print("\033[1;33m\nfile successfully Updated!\033[0m\n")

print("\033[1;35m\n--- NOW CREATING CHARTS: ---\033[0m")
# 1. Bar Chart
df=df.head(20)
sns.barplot(x="Country", y="Sales", data=df)
plt.title("Sales by Country")
plt.show()


# 2. create Line Chart
df=df.head(20)
sns.lineplot(x="Country", y="Sales", data=df)
plt.title("Sales by Country")
plt.show()


# 3. create Pie Chart
df=df.head(20)
data = df.groupby("Country")["Sales"].sum()
plt.pie(data, labels=data.index, autopct="%1.1f%%")
plt.title("Sales Percentage by Country")
plt.show()


# 4. create Histogram chart 
df=df.head(20)
sns.histplot(data=df, x="Sales", bins=10)
plt.title("Sales Distribution")
plt.show()


# 5. create Scatter Plot chart 
df=df.head(20)
sns.scatterplot(x="Sales", y="Profit", data=df)
plt.title("Sales and Profit")
plt.show()


# 6.create Box Plot chart 
df=df.head(20)
sns.boxplot(x="Country", y="Sales", data=df)
plt.title("Sales by Country")
plt.show()


print("\033[1;35m\n--- Bussiness Questions Answers ---\033[0m")

# Q1. Which region/country has highest sales?
q1 = df.groupby('Country')['Sales'].sum().sort_values(ascending=False)
print("\033[1;36m\n1. Sales by Country (Highest First):\033[0m")
print(q1.head(1))

# Q2. Which category earns maximum profit?
q2 = df.groupby('Product ID')['Profit'].sum().sort_values(ascending=False)
print("\033[1;36m\n2. Product ID with Maximum Profit:\033[0m")
print(q2.head(1))

# Q3. Which product sells most (by Quantity)?
q3 = df.groupby('Product ID')['Quantity'].sum().sort_values(ascending=False)
print("\033[1;36m\n3. Most Sold Product by Quantity:\033[0m")
print(q3.head(1))

# Q4. Monthly sales trend (Simple Order Date wise Sales)
q4 = df.groupby('Order Date')['Sales'].sum()
print("\033[1;36m\n4. Order Date Wise Sales Trend:\033[0m")
print(q4.head(5))

# Q5. Which customer segment buys most?
q5 = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False)
print("\033[1;36m\n5. Top Customer by Sales:\033[0m")
print(q5.head(1))

# Q6. Top 10 products by Sales
q6 = df.groupby('Product ID')['Sales'].sum().sort_values(ascending=False)
print("\033[1;36m\n6. Top 10 Products by Sales:\033[0m")
print(q6.head(10))

# Q7. Loss-making products (Jinke Profit 0 se chota hai)
q7 = df[df['Profit'] < 0][['Product ID', 'Profit']]
print("\033[1;36m\n7. Loss Making Products:033[0m")
print(q7.head(5))

# Q8. Average Order Value (AOV)
q8 = df['Sales'].mean()
print("\033[1;36m\n8. Average Order Value (Sales Mean):\033[0m")
print(q8)

# Q9. Best shipping mode (Yahan Order ID use kar rahe hain agar Ship Mode nahi hai)
q9 = df.groupby('Order ID')['Sales'].sum().sort_values(ascending=False)
print("\033[1;36m\n9. Top Order by Sales:\033[0m")
print(q9.head(1))

# Q10. Sales Forecast Trend (First row Sales vs Last row Sales)
first_sales = df['Sales'].head(5).mean()
last_sales = df['Sales'].tail(5).mean()
print("\033[1;36m\n10. Sales Comparison (First 5 vs Last 5 Rows Avg Sales):\033[0m")
print("\033[1;36mFirst 5 Avg:\033[0m", first_sales)
print("\033[1;36mLast 5 Avg:\033[0m", last_sales)
