#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

# ----- Movies -----
movies = pd.read_csv('../data/movies.csv')
movies['title'] = movies['title'].str.strip()
movies['genres'] = movies['genres'].str.lower().str.replace('|', ', ')
movies.to_csv('../data/movies_clean.csv', index=False)

# ----- Ratings -----
ratings = pd.read_csv('../data/ratings.csv')
ratings.to_csv('../data/ratings_clean.csv', index=False)

# ----- Tags  -----
tags = pd.read_csv('../data/tags.csv')
tags.to_csv('../data/tags_clean.csv', index=False)

print("✅ CSVs limpios exportados: movies_clean.csv, ratings_clean.csv, tags_clean.csv")

