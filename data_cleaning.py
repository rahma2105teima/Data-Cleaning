from numpy import inf
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("tmdb-movies.csv")
print(len(df))
print(df.shape)
print(df.info())
#sum nan values to decide if few so we will drop
print(df.isna().sum())

#removing nan values
df.dropna(inplace=True)
print(df.info())

df.drop(['homepage','imdb_id','id', 'tagline', 'overview', 'keywords', 'production_companies'], axis=1, inplace=True)
print(df.info())

#see if there is duplication in data
print("There are {} duplicated rows".format(df.duplicated().sum()))

#removing duplication
df.drop_duplicates(inplace=True)
print(df.info())

#converting 'release_date' to datetime dtype
df['release_date'] = pd.to_datetime(df['release_date'])
print(df.info())

#draw hist for all columns
df.hist(figsize=(10,10))
plt.show()

#check if there are rows with zero or -ve budget 
neg = (df['budget']<=0).sum()
print(neg)

print(df[df['budget']==0].describe())

df[df['budget']==0].hist(figsize=(10,10))
plt.show()

#removing zero and -ve budget
df= df[df['budget']>0]
print(df.info())

#check if there are rows with zero or -ve revenue
neg = (df['revenue']<=0).sum()
print(neg)

#removing zero and -ve revenue
df= df[df['revenue']>0]
print(df.info())

#make mask for sucess movies which have +ve differance between
#revenue and budget and for fail which hase -ve ones
sucess = ((df.revenue - df.budget)>0)
fail = ((df.revenue - df.budget)<=0)

#mean budget for success movies
print(df.budget[sucess].mean())

#mean budget for fail movies
print(df.budget[fail].mean())

#ploting the distribution of budget for the success vs fail movies
df.budget[sucess].hist(alpha =0.7,bins=20, label= 'sucess')
df.budget[fail].hist(alpha =0.6,bins=20, label= 'fail')
plt.title('budget for sucess and fail movies distribution')
plt.xlabel('budget')
plt.ylabel('number on movies')
plt.legend()
plt.show()