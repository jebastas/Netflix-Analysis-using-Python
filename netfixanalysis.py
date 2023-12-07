#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data = pd.read_csv('file.csv')


# In[2]:


data.head()


# In[3]:


data.tail()


# In[4]:


data.shape


# In[5]:


data.size


# In[6]:


data.columns


# In[7]:


data.dtypes


# In[8]:


data.info()


# In[4]:


#finding duplicate record in dataset

data.duplicated()


# In[5]:


data[data.duplicated()]


# In[6]:


data.drop_duplicates()


# In[7]:


data.drop_duplicates(inplace = True)


# In[8]:


data[data.duplicated()]


# In[15]:


data.shape


# In[16]:


# finding the null values

data.head()


# In[17]:


data.isnull()


# In[19]:


data.isnull().sum()


# In[21]:


# show with heatmap

import seaborn as sns
sns.heatmap(data.isnull())


# In[21]:


#q1 for 'house of cards', what is the show id & who is the director

data.head()


# In[9]:


data[data['Title'].isin(['House of Cards'])]


# In[10]:


data[data['Title'].str.contains('House of Cards')]


# In[26]:


#q2 which year highest no of tv shows & movies released, bar graph

data.dtypes


# In[11]:


# to datetime

data['Date_N'] = pd.to_datetime(data['Release_Date'])


# In[12]:


data.head()


# In[30]:


data.dtypes


# In[25]:


#counts occurance of all individual yer in date column

data['Date_N'].dt.year.value_counts()


# In[13]:


# bar graph

data['Date_N'].dt.year.value_counts().plot(kind='bar')


# In[26]:


#q3 how mny movies & tv shows in dataset, bar graph
#groupby()

data.groupby('Category').Category.count()


# In[38]:


#countplot()

sns.countplot(data['Category'])


# In[14]:


#q4 show all movies released in the year 2002

data['Year'] = data['Date_N'].dt.year #creating new column year using date_n coulumn


# In[40]:


data.head()


# In[28]:


# filtering

data[(data['Category'] == 'Movie') & (data['Year']==2002)]


# In[29]:


data[(data['Category'] == 'Movie') & (data['Year']==2020)]


# In[49]:


#q5 show only the titles of all tv shows released in india
#filtering
data.head(2)


# In[30]:


(data['Category'] == 'Tv Show') & (data['Country'] == 'India')


# In[31]:


data[ (data['Category'] == 'TV Show') & (data['Country'] == 'India') ]


# In[32]:


data[(data['Category'] == 'Tv Show') & (data['Country'] == 'India')] ['Title']


# In[54]:


#q6 show top 10 directors, who gave highest no of tv shows & movies to netflix
data.head(2)


# In[55]:


#value_counts

data['Director'].value_counts()


# In[33]:


#top 10 director

data['Director'].value_counts().head(10)


# In[59]:


#q7 show all records, where 'category is movie & type is comedies' or 'country is united kingdom'
#filtering (and, or operators)

data.head(10)


# In[34]:


(data['Category'] == 'Movie') & (data['Type'] == 'comedies')


# In[35]:


data[ (data['Category'] == 'Movie') & (data['Type'] == 'Comedies') ]


# In[36]:


data[ (data['Category'] == 'Movie') & (data['Type'] == 'Comedies') | (data['Country'] == 'United Kingdom')]


# In[71]:


#q8 n how many movies/shows tom cruise was cast
data.head()


# In[37]:


#filtering

data[ data['Cast'] == 'Tom Cruise']


# In[38]:


#str.contains()

data[ data['Cast'].str.contains('Tom Cruise')]


# In[75]:


# 1st drop null values from cast column

data_new = data.dropna() #it drops the rows that contain all or any missing values


# In[76]:


data_new.head()


# In[77]:


#str.contains

data_new[data_new['Cast'].str.contains('Tom Cruise')]


# In[78]:


#q9 different ratings by netflix

data.head(2)


# In[79]:


data['Rating'].nunique()


# In[80]:


data['Rating'].unique()


# In[81]:


#q9.1 movies got the 'TV-14' rating in canada

data.head(2)


# In[82]:


#filtering

data[(data['Category'] == 'Movie') & (data['Rating'] == 'TV-14')]


# In[83]:


data[(data['Category'] == 'Movie') & (data['Rating'] == 'TV-14')].shape


# In[84]:


data[(data['Category'] == 'Movie') & (data['Rating'] == 'TV-14') & (data['Country']== 'Canada')]


# In[85]:


#Q9.2 tv shows got 'R' rating after year 2018

data.head(2)


# In[87]:


data[(data['Category'] == 'TV Show') & (data['Rating'] == 'R')]


# In[88]:


data[(data['Category'] == 'TV Show') & (data['Rating'] == 'R') & (data['Year'] > 2018)]


# In[3]:


#q10 what is the unique duration of movie/tv show 

data.head(2)


# In[4]:


data.Duration.unique()


# In[5]:


data.Duration.dtypes


# In[6]:


#q11 which individual country has highest no of tv shows

data.head(2)


# In[7]:


data_tvshow = data[data['Category'] == 'TV Show']
data_tvshow.head(2)


# In[8]:


data_tvshow.Country.value_counts()


# In[10]:


data_tvshow.Country.value_counts().head(1)


# In[11]:


#q12 find all the instance where:
#category is 'movie' and type is 'drama' or category is 'TV Show' & type is 'kids' tv

data.head(2)


# In[13]:


data[(data['Category'] == 'Movie') & (data['Type'] == 'Dramas')].head(2)


# In[16]:


data[(data['Category'] == 'TV Show') & (data['Type'] == "Kids' TV")].head(2)


# In[17]:


data[(data['Category'] == 'Movie') & (data['Type'] == 'Dramas') | (data['Category'] == 'TV Show') & (data['Type'] == "Kids' TV")]


# In[18]:


#q13 sort the dataset by year

data.head(2)


# In[15]:


data.sort_values(by = 'Year')


# In[20]:


import matplotlib.pyplot as plt


# In[22]:


plt.figure(figsize=(8,6))
sns.countplot(x='Rating', data=data)
plt.title("Released with Highest Rating")
plt.show()


# In[23]:


plt.figure(figsize=(10,10))
y = sns.countplot(y='Country', data=data, order=data['Country'].value_counts().index[:15])
plt.tick_params(labelsize=10)
plt.title("Country with most released")
plt.show()


# In[ ]:




