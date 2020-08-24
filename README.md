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
