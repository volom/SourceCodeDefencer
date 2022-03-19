import requests
import pandas as pd
from hw_file import sum_degree

df = pd.DataFrame(requests.get('https://jsonplaceholder.typicode.com/posts').json())
df['computation'] = df.apply(lambda x: sum_degree(x['userId'], x['id']), axis=1)
df.to_csv("some_data.csv")
print(df.head())