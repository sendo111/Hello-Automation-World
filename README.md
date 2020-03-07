# Hello-Automation-World
 - 本リポジトリは、技術書典8で頒布しました「はじめての自動化」のサンプルアプリです。
 - https://techbookfest.org/event/tbf08/circle/5629626760036352

---
## Versions
 - python 3.8.0
 - Django 2.2.10
 - nginx 1.16.1
 - uWSGI 2.0.18
 - mysql 5.7

---
## ローカル: アプリ起動方法
```
// manage.pyのディレクトリに移動
$ cd haw/

// 必要なパッケージのインストール
$ pip install -r requirements.txt

// modelからマイグレーションファイルを作成
$ python manage.py makemigrations

// 作成したマイグレーションファイルをDBに反映
$ python manage.py migrate

// サーバーを起動
$ python manage.py runserver

// ブラウザでアクセス
http://localhost:8000/
```

