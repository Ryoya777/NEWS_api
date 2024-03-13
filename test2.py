import requests
import pandas as pd

headers = {'X-Api-Key': 'API Key 文字列'}

# Top headlines Endpoint
url = 'https://newsapi.org/v2/top-headlines'
params = {
    'category': 'business',
    'country': 'jp'
}

# Get response
response = requests.get(url, headers=headers, params=params)

# Make dataframe
if response.ok:
    data = response.json()
    df = pd.DataFrame(data['articles'])
    print('totalResults:', data['totalResults'])

print(df[[ 'publishedAt', 'title', 'url']])