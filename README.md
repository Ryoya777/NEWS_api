# NEWS_api

NEWS_apiを使用して、指定したカテゴリの日本のニュースを取得できるPythonアプリです。このアプリでは、ビジネス、エンターテイメント、一般、健康、科学、スポーツ、テクノロジーの各カテゴリからニュースを取得することができます。

## 使い方

このアプリを使用する前に、[NewsAPI](https://newsapi.org/) からAPIキーを取得する必要があります。取得したAPIキーは、アプリのソースコード内で指定してください。

### 必要なライブラリのインストール

このアプリを実行するため、以下のコマンドを実行して必要なライブラリをインストールしてください。

```
pip install -r requirements.txt
```

### アプリの実行

アプリを実行するには、ターミナルまたはコマンドプロンプトで以下のコマンドを実行してください。

```
python main.py
```

アプリを実行すると、次のようにカテゴリの選択を促されます。

```
ニュースのカテゴリを選択してください。'ランダム'または'選択':
```
・ ランダム: カテゴリをランダムに選択します。  
・ 選択: 利用可能なカテゴリのリストからカテゴリを選択します。(business, entertainment, general, health, science, sports, technology)  
選択後、指定されたカテゴリの日本のトップニュース20件が取得され、News_folderディレクトリ内にcategory_time.csv形式で保存されます。ファイル名には、選択したカテゴリとニュースを取得した日付が含まれます。


### ニュースの取得とCSVファイルの保存
ニュースは自動的に取得され、指定された形式でCSVファイルに保存されます。ファイルはNews_folderディレクトリに保存され、ファイル名は選択したカテゴリと取得した日付に基づいています。例えば、ビジネスカテゴリのニュースを2024年2月10日に取得した場合、ファイル名はbusiness_20240210.csvとなります。

#### 参考
[Python と News API を使ってニュース記事を収集する](https://zenn.dev/uinoue/articles/660ee202373f64)
