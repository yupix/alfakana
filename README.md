# ALFAKANA

このライブラリは[こちら](https://github.com/cod-sushi/alkana.py)からインスパイアを受け作成したライブラリです。インスパイア元のalkana.pyと同じように英単語を日本語に置き換えすることが可能です。

## 使い方

基本的な使い方は以下の通りです。
このライブラリでは辞書をデータベース形式でご自分で用意していただく必要があります。  
データベース概要:  
 テーブル名: dic  
 カラム1: key (英単語を大文字で)  
 カラム2: value(英単語の日本語訳をカ

※この動作での結果については私の辞書での結果です。私と同じ辞書を作る方法は[現在作成中](#)です
### 単語単体の場合
```python
import alfakana
db_path = './dic.db'
print(alfakana.change_kana('word'), db_path)
>>> ワード
```

### 単語と日本語の文字列の場合

```python
import alfakana
db_path = './dic.db'
print(alfakana.sentence_kana('私はTypeScriptが大好きです'), db_path)
>>> 私はタイプ・スクリプトゥが大好きです
```
