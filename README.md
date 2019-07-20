# django-vuejs
Django + Vue.js で簡単なWEBアプリケーションを作成する
![title](https://github.com/mila411/django-vuejs/blob/master/title.png)

[DjangoとVue.jsで作るWEBアプリ（その1: 設定編）](https://nmomos.com/tips/python/2019/07/17/django-vuejs-1/ "DjangoとVue.jsで作るWEBアプリ（その1: 設定編）")  
[DjangoとVue.jsで作るWEBアプリ（その2: 認証機能編）](https://nmomos.com/tips/python/2019/07/18/django-vuejs-2/ "DjangoとVue.jsで作るWEBアプリ（その2: 認証機能編）")  
[DjangoとVue.jsで作るWEBアプリ（その3: API実装編）](https://nmomos.com/tips/python/2019/07/19/django-vuejs-3/ "DjangoとVue.jsで作るWEBアプリ（その3: API実装編）")  


# 実行方法
## 1. リポジトリのクローン
```bash
https://github.com/mila411/django-vuejs.git
```
***
## 2. バックエンド実行
### 2-1. パッケージのインストール
```bash
cd server
pip install -r requirements.txt
```
### 2-2. マイグレート
```bash
python manage.py migrate
```
### 2-3. 開発サーバ起動
```bash
python manage.py runserver
```
***
## 3. フロントエンド実行

### 3-1. セットアップ
```bash
npm install
```
### 3-2. 実行
```basu
npm run serve
```
