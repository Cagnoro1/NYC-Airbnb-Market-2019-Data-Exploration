#!/usr/bin/env python
# coding: utf-8

# # NYC Airbnb Market 2019 Data Exploration
Steps

1. Import libraries
2. Load datasets
3. Initial exploration
4. Data cleaning
5. Data Analysis
# In[131]:


# Import libraries

import pandas as pd
import numpy as np
import os

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import seaborn as sns

plt.style.use('ggplot') 


# In[92]:


#Load dataset
df = pd.read_csv('/Users/christelleagnoro/Desktop/airbnb_nyc_2019.csv')


# ## 3. Intial exploration of data

# In[25]:


df.head()


# In[35]:


df.tail()


# In[40]:


#Number of rows and coulums 
df.shape


# In[41]:


df.info()


# In[42]:


# Statistical Summary
df.describe()


# # 4. Data cleaning

# In[43]:


# List of null data
df.isnull().sum()


# In[46]:


# Drop all missing values rows
df.dropna(inplace=True)
# data.fillna()
df.isnull().sum()


# In[48]:


# Checking for duplicates rows
df.duplicated().sum()


# # 5. Data Analysis 

# ### Outliers prices

# In[132]:


# Calculate average price
df.price.info()


# In[74]:


# Calculate average price by naigbohood and room type
print("Neighbourhood Group  | Room Type   |  Price       ")
print("------------------------------------------------")
avg_price_combo = df.groupby(['neighbourhood_group', 'room_type'])['price'].mean().round().astype(int)
print(avg_price_combo)


# In[98]:


#Number of AirBnb in different neighbourhood_group
neighbourhood_group_count = df.groupby("neighbourhood_group").count().head()

# Display the results
print(neighbourhood_group_count[['id']].rename(columns={'id': 'count'}))


# In[103]:


#Pie chart of different neighbourhood group by count


# In[108]:


# price dependency on neighbourhood
sns.barplot(data=df, x='neighbourhood_group', y='price', hue='room_type')


# In[110]:


# number of reviews and price rel
plt.figure(figsize=(8, 5))
plt.title("Locality and Review Dependency")
sns.scatterplot(data=df, x='number_of_reviews', y='price', hue='neighbourhood_group')
plt.show()


# In[111]:


sns.pairplot(data=df, vars=['price', 'minimum_nights', 'number_of_reviews', 'availability_365'], hue='room_type')


# In[112]:


#Geographical Distribution of AirBnb Listing
plt.figure(figsize=(10, 7))
sns.scatterplot(data=df, x='longitude', y='latitude', hue='room_type')
plt.title("Geographical Distribution of AirBnb Listing")
plt.show()


# In[123]:


#histogram Average reviews of AirBnb in different neighbourhood
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_style("whitegrid")

# 1. Calculate average reviews per month by neighborhood group
avg_reviews = df.groupby('neighbourhood_group')['reviews_per_month'].mean().sort_values(ascending=False)

# 2. Create the plot
plt.figure(figsize=(10, 6))
ax = sns.barplot(
    x=avg_reviews.index,
    y=avg_reviews.values,
    palette="plasma",
    saturation=0.8,
    edgecolor="black",
    linewidth=0.5
)

# 3. Customize the plot
plt.title('Average Reviews per Month by Neighborhood Group', fontsize=14, pad=20)
plt.xlabel('Neighborhood Group', fontsize=12)
plt.ylabel('Average Reviews/Month', fontsize=12)
plt.ylim(0, avg_reviews.max()*1.1)  # Add 10% headroom

# 4. Add value labels
for p in ax.patches:
    ax.annotate(
        f"{p.get_height():.2f}",  # Format to 2 decimal places
        (p.get_x() + p.get_width() / 2., p.get_height()),
        ha='center',
        va='center',
        xytext=(0, 5),
        textcoords='offset points',
        fontsize=10
    )

plt.tight_layout()
plt.show()


# In[124]:


# Calculate avg price by neighborhood & room type
avg_price_by_room = df.groupby(['neighbourhood_group', 'room_type'])['price'].mean().round().astype(int).unstack()

# Display as formatted table
print("Average Price by Neighborhood and Room Type ($)")
print("="*50)
print(avg_price_by_room.to_markdown())  # Requires 'tabulate' package


# In[129]:


plt.figure(figsize=(12, 6))
sns.barplot(
    data=df,
    x='neighbourhood_group',
    y='price',
    hue='room_type',
    estimator='mean',
    palette='viridis',
    errorbar=None,
    edgecolor='black'
)

plt.title('Average Airbnb Price by Room Type & Neighborhood', fontsize=14, pad=20)
plt.xlabel('Neighborhood Group', fontsize=12)
plt.ylabel('Average Price ($)', fontsize=12)
plt.legend(title='Room Type', bbox_to_anchor=(1.05, 1), loc='upper left')

# Add value labels
for container in plt.gca().containers:
    plt.bar_label(
        container,
        fmt='$%d',
        label_type='edge',
        padding=3,
        fontsize=10
    )

plt.tight_layout()
plt.show()


# In[130]:


# Save to CSV
avg_price_by_room.to_csv('avg_price_by_room_neighborhood.csv')

# Save plot
plt.savefig('price_by_room_neighborhood.png', dpi=300, bbox_inches='tight')


# In[ ]:




