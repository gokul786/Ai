import numpy as np
import pandas as pd
import difflib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies_data=pd.read_csv('/content/movies.csv')
movies_data.head()
