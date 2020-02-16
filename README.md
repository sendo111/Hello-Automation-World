# ブランチ運用
大前提として、個別のブランチは章ごと(チケットごと)に切って作業する。  
また、事故った時のためにマージ後のブランチも残しておく。  
・ブランチの命名規則 ： feature/ + JIRAチケット番号(feature/HAW-30)  
・マージ先 ： featureブランチ -> developブランチ  

---
## Versions
 - python 3.8.0
 - Django 2.2

---
## アプリ起動方法
```
// 必要なパッケージのインストール
pip install -r requirements.txt

// manage.pyのディレクトリに移動
cd haw/

// modelからマイグレーションファイルを作成
python manage.py makemigrations

// 作成したマイグレーションファイルをDBに反映
python manage.py migrate

// サーバーを起動
python manage.py runserver

// ブラウザでアクセス
http://127.0.0.1:8000/
```

---
## テスト実行方法
```
@前提条件
アプリ起動方法の手順に記載のある '必要なパッケージのインストール' が行われていること

// manage.pyのディレクトリに移動
cd haw

// テストを実行
python manage.py test
```
