import pandas as pd
import numpy as np
movies=pd.read_csv("tmdb_5000_movies[1].csv")
movies=pd.read_csv("tmdb_5000_movies[1].csv")
credits=pd.read_csv("tmdb_5000_movies[1].csv")
movies.head(0)
credits.head(0)
movies=movies.merge(credits,on=["title"])
movies.head(0)
movies=movies.merge(credits,on=["titles"])
movies=movies.merge(credits,on=["title"])
movies[["movie_id","title","overview","genres","keywords","cast","crew"]]
import pandas as pd
import numpy as np
movies=pd.read_csv("tmdb_5000_movies[1].csv")
credits=pd.read_csv("tmdb_5000_credits[1].csv")
credits.head(0)
movies=movies.merge(credits,on=["title"])
movies.head(1)
movies[["movie_id","title","overview","genres","keywords","cast","crew"]]
movies=movies[["movie_id","title","overview","genres","keywords","cast","crew"]]
movies.isnull().sum()
movies.dropna(inplace=True)
 import ast
def convert(obj):
    l=[]
    for i in ast.literal_eval(obj):
        l.append(i["name"])
    return l
movies["genres"].apply(convert)
movies["genres"]=movies["genres"].apply(convert)
movies["keywords"].apply(convert)
movies["keywords"]=movies["keywords"].apply(convert)
movies.head()
def convert2(obj):
    l=[]
    counter=0
    for i in ast.literal_eval(obj):
        if counter !=3:
            l.append(i["name"])
            couter+=1
        else:
            break
    return l
movie["cast"].apply(counter2)
movies["cast"].apply(counter2)
movies["cast"].apply(convert2)
import pandas as pd
import numpy as np
movies=pd.read_csv("tmdb_5000_movies[1].csv")
credits=pd.read_csv("tmdb_5000_credits[1].csv")
credits.head(0)
movies=movies.merge(credits,on=["title"])
movies.head(1)
movies=movies[["movie_id","title","overview","genres","keywords","cast","crew"]]
movies.head()
movies.dropna(inplace=True)
 import ast
def convert(obj):
    l=[]
    for i in ast.literal_eval(obj):
        l.append(i["name"])
    return l
movies["genres"]=movies["genres"].apply(convert)
movies["keywords"]=movies["keywords"].apply(convert)
def convert2(obj):
    l=[]
    counter=0
    for i in ast.literal_eval(obj):
        if counter !=3:
            l.append(i["name"])
            couter+=1
        else:
            break
    return l
movies["cast"].apply(convert2)
def convert2(obj):
    l=[]
    counter = 0
    for i in ast.literal_eval(obj):
        if counter != 3
            l.append(i["name"])
            couter+=1
        else:
            break
    return l
def convert2(obj):
    l=[]
    counter = 0
    for i in ast.literal_eval(obj):
        if counter != 3:
            l.append(i["name"])
            couter+=1
        else:
            break
    return l
movies["cast"].apply(convert2)
def convert2(obj):
    l=[]
    counter = 0
    for i in ast.literal_eval(obj):
        if counter != 3:
            l.append(i["name"])
            counter+=1
        else:
            break
    return l
movies["cast"].apply(convert2)
def convert3(obj):
    l=[]
    for i in ast.literal_eval(obj):
        if i["job"]=="Director"
        l.append(i["name"])
        break
    return l
def convert3(obj):
    l=[]
    for i in ast.literal_eval(obj):
        if i["job"]=="Director":
            l.append(i["name"])
        break
    return l
movies["crew"].apply(convert3)
def convert3(obj):
    l=[]
    for i in ast.literal_eval(obj):
        if i["job"]=="Director":
            l.append(i["name"])
            break
    return l
movies["crew"].apply(convert3)
movies["overview"].apply(lambda x:x.split())
movies["overview"]=movies["overview"].apply(lambda x:x.split())
movies["genres"].apply(lambda x:[i.replace(" ","")for i inx])
movies["genres"].apply(lambda x:[i.replace(" ","")for i in x])
movies["genres"]=movies["genres"].apply(lambda x:[i.replace(" ","")for i in x])
movies["keywords"]=movies["keywords"].apply(lambda x:[i.replace(" ","")for i in x])
movies["cast"]=movies["cast"].apply(lambda x:[i.replace(" ","")for i in x])
movies["crew"]=movies["crew"].apply(lambda x:[i.replace(" ","")for i in x])
movies.head()
movies["caste"]
movies["cast"]
movies["cast"]=movies["cast"].apply(convert2)
import pandas as pd
import numpy as np
movies=pd.read_csv("tmdb_5000_movies[1].csv")
credits=pd.read_csv("tmdb_5000_credits[1].csv")
credits.head(0)
movies=movies.merge(credits,on=["title"])
movies.head(1)
movies=movies[["movie_id","title","overview","genres","keywords","cast","crew"]]
movies.head()
movies.dropna(inplace=True)
 import ast
def convert(obj):
    l=[]
    for i in ast.literal_eval(obj):
        l.append(i["name"])
    return l
movies["genres"]=movies["genres"].apply(convert)
movies["keywords"]=movies["keywords"].apply(convert)
def convert2(obj):
    l=[]
    counter = 0
    for i in ast.literal_eval(obj):
        if counter != 3:
            l.append(i["name"])
            counter+=1
        else:
            break
    return l
movies["cast"]=movies["cast"].apply(convert2)
def convert3(obj):
    l=[]
    for i in ast.literal_eval(obj):
        if i["job"]=="Director":
            l.append(i["name"])
            break
    return l
movies["crew"].apply(convert3)
movies["overview"]=movies["overview"].apply(lambda x:x.split())
movies["genres"]=movies["genres"].apply(lambda x:[i.replace(" ","")for i in x])
movies["keywords"]=movies["keywords"].apply(lambda x:[i.replace(" ","")for i in x])
movies["cast"]=movies["cast"].apply(lambda x:[i.replace(" ","")for i in x])
movies["crew"]=movies["crew"].apply(lambda x:[i.replace(" ","")for i in x])
movies.head()
movies["cast"]
movies["crew"]=movies["crew"].apply(convert3)
import pandas as pd
import numpy as np
movies=pd.read_csv("tmdb_5000_movies[1].csv")
credits=pd.read_csv("tmdb_5000_credits[1].csv")
credits.head(0)
movies=movies.merge(credits,on=["title"])
movies.head(1)
movies=movies[["movie_id","title","overview","genres","keywords","cast","crew"]]
movies.head()
movies.dropna(inplace=True)
 import ast
def convert(obj):
    l=[]
    for i in ast.literal_eval(obj):
        l.append(i["name"])
    return l
movies["genres"]=movies["genres"].apply(convert)
movies["keywords"]=movies["keywords"].apply(convert)
def convert2(obj):
    l=[]
    counter = 0
    for i in ast.literal_eval(obj):
        if counter != 3:
            l.append(i["name"])
            counter+=1
        else:
            break
    return l
movies["cast"]=movies["cast"].apply(convert2)
def convert3(obj):
    l=[]
    for i in ast.literal_eval(obj):
        if i["job"]=="Director":
            l.append(i["name"])
            break
    return l
movies["crew"]=movies["crew"].apply(convert3)
movies["overview"]=movies["overview"].apply(lambda x:x.split())
movies["genres"]=movies["genres"].apply(lambda x:[i.replace(" ","")for i in x])
movies["keywords"]=movies["keywords"].apply(lambda x:[i.replace(" ","")for i in x])
movies["cast"]=movies["cast"].apply(lambda x:[i.replace(" ","")for i in x])
movies["crew"]=movies["crew"].apply(lambda x:[i.replace(" ","")for i in x])
movies.head()
movies["cast"]
movies["tags"]=movies["overview"]+movies["genres"]+movies["keywords"]+movies["cast"]+movies["crew"]
new_df=movies[["movie_id","title","tags"]]
new_df["tags"].apply(lambda x:" ".join(x))
new_df["tags"]=new_df["tags"].apply(lambda x:" ".join(x))
new_df.head()
new_df['tags'].apply(lambda x:x.lower())
new_df["tags"]=new_df['tags'].apply(lambda x:x.lower())
new_df.head()
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()
cv=CountVectorizer(max_features=5000,stop_words="english")
cv.fit_transform(new_df["tags"]).toarray()
cv.get_feature_names()
cv.get_feature_names_out()
pip install nltk
import nltk
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()
def stem(text):
    y=[]
    for i in text.split():
        y.append(ps.stem(i))
    return "".join(y)
def stem(text):
    y=[]
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)
new_df["tags"].apply(stem)
new_df["tags"]=new_df["tags"].apply(stem)
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=5000,stop_words="english")
cv.fit_transform(new_df["tags"]).toarray()
vectors=cv.fit_transform(new_df["tags"]).toarray()
vectors
cv.get_feature_names_out()
from sklearn.metrics.pairwise import cosine_similarity
similarity=cosine_similarity(vectors)
%history -f main1.py


