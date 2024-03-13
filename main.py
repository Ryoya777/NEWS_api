import requests
import pandas as pd
import random
import os
from datetime import datetime

# APIキーの設定（実際のAPIキーに置き換えてください）
API_KEY = os.getenv('NEWSAPI_API_KEY')

# ニュースカテゴリのリスト
categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']

def fetch_news(category):
    """指定されたカテゴリのニュースを取得し、CSVファイルに保存する"""
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'category': category,
        'country': 'jp',
        'apiKey': API_KEY
    }
    
    response = requests.get(url, params=params)
    if response.ok:
        data = response.json()
        df = pd.DataFrame(data['articles'])
        # 必要な情報のみを選択
        df = df[['publishedAt', 'title', 'url']]
        # CSVファイルに保存
        time_now = datetime.now().strftime('%Y%m%d')
        csv_file_name = f'{category}_{time_now}.csv'
        df.to_csv("News_folder/"+csv_file_name, index=False)
        print(f"ニュースを保存しました: {csv_file_name}")
    else:
        print("ニュースの取得に失敗しました。")

# ユーザーにカテゴリを選択させる
choice = input("ニュースのカテゴリを選択してください。'ランダム'または'選択': ").strip()

if choice == 'ランダム':
    selected_category = random.choice(categories)
elif choice == '選択':
    print("カテゴリを選択してください: business, entertainment, general, health, science, sports, technology")
    selected_category = input().strip()
    if selected_category not in categories:
        print("無効なカテゴリが選択されました。プログラムを終了します。")
        exit()
else:
    print("無効な入力です。プログラムを終了します。")
    exit()

# ニュースを取得してCSVに保存
fetch_news(selected_category)