import re
import sqlite3
from alfakana.exceptions import NoSuchTable


def add_dic(key, value, db_path):
    """
    与えられた`key`と`value`を元に与えられたデータベースに辞書を追加します。
    Parameters
    ----------
    key : str
        英単語を受け取ります
    value : str
        英単語の日本語(カタカナ)を受け取ります
    Returns
    -------
    None : None
        送信限定です。
    """
    with sqlite3.connect(f'{db_path}') as conn:
        sql = "INSERT INTO dic (key, value) values (?,?)"
        try:
            conn.execute(sql, [key, value])
        except sqlite3.IntegrityError:
            pass

def sentence_kana(text, db_path):
    """
    Parameters
    ----------
    text : str
        カタカナに変換したい日本語を含んだ文字列を受け取ります
    db_path : str
        .dbファイルへのパスを受け取ります
    Returns
    -------
    output : str
        wordをカタカナに変更したものを返します
        wordが見つからなかった場合そのままになります
    """
    output = ''
    while word := re.search(r'[a-zA-Z]{4,}', text):  # 4文字以上の物を順番に検索
        output += text[:word.start()] + change_kana(word.group(), db_path)
        text = text[word.end():]

    return output + text


def change_kana(text, db_path: str = None):
    """
    渡された英単語をカタカナにして返します

    Parameters
    ----------
    text : str
        The alphabetical string you want to get the katakana reading.
        The case of string is ignored.
    path : str
        sqliteのデータベースへのパスを指定。
        (例) ./dic.sql

    Returns
    ----------
    text : str
        英単語をカタカナにしたもの
    """
    conn = sqlite3.connect(f'{db_path}')
    cur = conn.cursor()
    try:
        return cur.execute(f"SELECT * FROM dic WHERE key == '{text.upper()}';").fetchone()[1]
    except sqlite3.OperationalError:
        raise NoSuchTable
    except TypeError:
        if re.fullmatch(r'(?:[A-Z][a-z]{3,}){2,}', text):
            m = re.match(r'[A-Z][a-z]{3,}', text)
            first = change_kana(m.group(), db_path)
            second = change_kana(text[m.end():], db_path)
            return first + second
        return text
