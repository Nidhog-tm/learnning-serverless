勉強用
==============================================
## build 用 カウンター
2

## 仮装開発環境作成
```
python3 -m venv .venv_2
source .venv_2/bin/activate
```

## パッケージインストール
`pip install -r requirements.txt`

## テスト実行
```
python -m unittest tests.test_handler -v
python -m unittest tests.test_get_db_list -v
```

## 構成図

![API Gateway](https://user-images.githubusercontent.com/52826519/91540138-52de1700-e955-11ea-9f7a-90c7d0d9ff89.png)
