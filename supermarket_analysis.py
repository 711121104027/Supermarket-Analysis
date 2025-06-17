#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[2]:


df  = pd.read_csv('/home/jupyter-711121104027/Sample - Superstore.csv', encoding='latin-1')
df.head()


# In[3]:


df.sample()


# In[4]:


df.describe()


# In[5]:


df.info()


# In[6]:


df.isnull().sum()


# In[7]:


df.duplicated().sum()


# In[8]:


df['Order Date']  =pd.to_datetime(df['Order Date'])
df['Ship Date']  =pd.to_datetime(df['Ship Date'])


# In[9]:


df['Order Month'] = df['Order Date'].dt.month
df['Order Year'] = df['Order Date'].dt.year
df['Order day of week'] = df['Order Date'].dt.dayofweek
df.head()


# In[10]:


monthly_sales = df.groupby('Order Month')['Sales'].sum().reset_index()
monthly_sales


# In[11]:


plt.figure(figsize=(8, 4))
plt.plot(monthly_sales['Order Month'], monthly_sales['Sales'], marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(False)
plt.tight_layout()
plt.show()


# In[12]:


category_perf = df.groupby('Category').agg(
    total_orders=('Order ID', 'nunique'),
    total_quantity=('Quantity', 'sum'),
    total_sales=('Sales', 'sum'),
    total_profit=('Profit', 'sum')  # only if you have this column
).reset_index()

category_perf = category_perf.sort_values(by='total_sales', ascending=False)

print(category_perf)


# In[13]:


plt.figure(figsize=(12, 7))
sns.barplot(data=category_perf, x='Category', y='total_sales')
plt.title("Sales by Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()


# In[14]:


regional_perf = df.groupby('Region').agg(
    total_sales=('Sales', 'sum'),
    total_profit=('Profit', 'sum'),
    total_orders=('Order ID', 'nunique'),
    total_customers=('Customer ID', 'nunique'),
    avg_order_value=('Sales', 'mean')
).reset_index()

regional_perf = regional_perf.sort_values(by='total_sales', ascending=False)

print(regional_perf)


# In[15]:


plt.figure(figsize=(10, 6))
sns.barplot(data=regional_perf, x='Region', y='total_sales')
plt.title("Sales by Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[16]:


segment_perf = df.groupby('Segment').agg(
    total_sales=('Sales', 'sum'),
    total_profit=('Profit', 'sum'),
    total_orders=('Order ID', 'nunique'),
    total_quantity=('Quantity', 'sum')
).reset_index()

segment_perf = segment_perf.sort_values(by='total_sales', ascending=False)

print(segment_perf)


# In[17]:


plt.figure(figsize=(8, 5))
sns.barplot(data=segment_perf, x='Segment', y='total_sales', palette='Set2')
plt.title('Sales by Segment')
plt.ylabel('Total Sales')
plt.xlabel('Segment')
plt.tight_layout()
plt.show()


# In[18]:


top_products = df.groupby("Product Name")["Sales"].sum().nlargest(10).sort_values()
plt.figure(figsize=(10, 6))


# In[19]:


top_products.plot(kind='barh', color='skyblue')
plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.tight_layout()
plt.show()


# In[26]:


state_profit = df.groupby("State")["Profit"].sum().sort_values()
state_profit


# In[21]:


plt.figure(figsize=(12, 8))
state_profit.plot(kind="barh", color="salmon")
plt.title("Profit by State")
plt.xlabel("Total Profit")
plt.tight_layout()
plt.show()


# In[22]:


plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="Sales", y="Profit", hue="Category")
plt.title("Sales vs Profit by Category")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.xscale('log')
plt.tight_layout()
plt.show()


# In[23]:


plt.figure(figsize=(10, 6))
sns.boxplot(x="Discount", y="Profit", data=df)
plt.title("Impact of Discount on Profit")
plt.tight_layout()
plt.show()


# In[25]:


df["Order Date"] = pd.to_datetime(df["Order Date"])
df['Month'] = df['Order Date'].dt.to_period('M').astype(str)
monthly_profit = df.groupby("Month")["Profit"].sum()
monthly_profit


# In[27]:


plt.figure(figsize=(12, 6))
monthly_profit.plot(marker='o')
plt.title("Monthly Profit Trend")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


# In[28]:


ship_mode = df["Ship Mode"].value_counts()
ship_mode


# In[29]:


plt.figure(figsize=(6, 6))
ship_mode.plot(kind="pie", autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
plt.title("Distribution of Ship Modes")
plt.ylabel("")
plt.tight_layout()
plt.show()


# In[ ]:




