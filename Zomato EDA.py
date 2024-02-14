#!/usr/bin/env python
# coding: utf-8

# # Zomato EDA

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


df = pd.read_csv(r"C:\\Users\\harsh\\Documents\\Python stuff\\Zomatodataset\\zomato.csv", encoding='latin1')
df


# In[ ]:


df.isnull().sum()


# In[ ]:


df.describe()


# In[ ]:


df.info()


# In[ ]:


[features for features in df.columns if df[features].isnull().sum() > 0]


# In[ ]:





# In[ ]:


df.columns


# # joining two dataset

# In[ ]:


final_df = pd.merge(df, df_country, on='Country Code', how = 'left')


# In[ ]:


final_df.dtypes


# In[ ]:


country_names = final_df.Country.value_counts().index


# In[ ]:


country_values = final_df.Country.value_counts().values


# In[ ]:


#Top 3 countries that uses zomato
plt.pie(country_values[:3], labels = country_names[:3], autopct="%1.2f%%")


# # Observation: Highest records of zomato are from India followed by US and UK

# In[ ]:


## Numerical variables
final_df.describe()


# In[ ]:


final_df.info()


# In[ ]:


ratings = final_df.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index().rename(columns={0:'Rating Count'})


# # Conclusion
# 1. when rating is between 4.5 to 4.9 ---> excellent
# 2. when rating is between 4.0 to 3.4 ---> very good
# 3. when rating is between 3.5 to 3.9 ---> good 
# 4. when rating is between 3. to 3.4 ---> average
# 5. when rating is between 2.5 to 2.9 ---> aaverage
# 6. when rating is between 2.0 to 2.4 ---> poor
# 
#     

# In[ ]:


ratings.info()


# In[ ]:


import matplotlib


# In[ ]:


matplotlib.rcParams['figure.figsize'] = (12,6)
sns.barplot(x = 'Aggregate rating', y='Rating Count', data = ratings)


# In[ ]:


matplotlib.rcParams['figure.figsize'] = (12,6)
sns.barplot(x = 'Aggregate rating', y='Rating Count',hue = 'Rating color', data = ratings, palette = ['blue', 'red', 'orange', 'yellow', 'green', 'green'] )


# # Observation:
# 1. Not rated count is very high
# 2. Maximum no of ratings are between 2.5 to 3.4

# In[ ]:


# Count Plot
sns.countplot(x = 'Rating color', data = ratings, palette = ['pink', 'red', 'orange', 'yellow', 'green', 'green'])


# In[ ]:


### Find the countires that has given 0 rating


# In[ ]:


zero_rating_df = final_df[final_df['Aggregate rating'] == 0]
zero_rating_df


# In[ ]:


country_0_rating = zero_rating_df['Country'].value_counts()
print(country_0_rating)


# # Observation
#     Maximum number of 0 ratings is from Indian Customer

# In[ ]:


# Which currency is used by which country
final_df.info()


# In[ ]:


final_df[['Country', 'Currency']].groupby(['Country', 'Currency']).size().reset_index()


# In[ ]:


# Which countries do have online deliveyr option
final_df[['Country', 'Has Online delivery']].groupby(['Country', 'Has Online delivery']).size().reset_index()


# # Observations:
#        Only two countries has online deliveries- India and UAE

# In[ ]:


# Create a pie chart for distribution
final_df.City.value_counts().index


# In[ ]:


city_value = final_df.City.value_counts().values
city_labels = final_df.City.value_counts().index


# In[ ]:


plt.pie(city_value[:5], labels = city_labels[:5])


# In[ ]:





# In[ ]:





# In[ ]:




