# 1.本棚に本を追加する機能
# 2.本棚にある本の情報を一覧取得できる機能
# 3.本棚から本を取り除く(削除する)機能

# クラスの定義の部分のみを記述する
# そこからシェル上でインポートして上記のインスタンス以降のコードを書いて行くのが直感的でわかりやすい

# >>> from book_shelf import BookShelf
# >>> shelf = BookShelf("お気に入り")
# >>> shelf.add_book("論語と算盤", "渋沢栄一")
# 追加したよ(￣･ω･￣)

import os
import sqlite3

PATH = os.path.join(os.getcwd(), "bk_shelf.db")
connect = sqlite3.connect(PATH)
cursor = connect.cursor()

class BookShelf:
    #インスタンスされた時点でテーブルを作成
    def __init__(self, name):
        self.name = name
        create_tb_sql = """CREATE TABLE if not exists {0}
                        (id integer Primary key AUTOINCREMENT,
                        author text,
                        book_name text)
                        """.format(self.name)
        cursor.execute(create_tb_sql)
        print("created")
    
    def __str__(self):
        message = "本棚[{0}]".format(self.name)
        return message

    #データを追加する処理
    def add_book(self, title, author):
        add_data_sql = "INSERT INTO {0} VALUES(null, '{1}', '{2}')".format(self.name, title, author)
        cursor.execute(add_data_sql)
        connect.commit()
        print("追加したよ(￣･ω･￣)")

    #情報の一覧取得処理
    def list_book(self):
        search_all_sql = "SELECT * FROM {0}".format(self.name)
        cursor.execute(search_all_sql)
        result = cursor.fetchall()
        dt_exist_flag = 1 if len(result) != 0 else 0

        if dt_exist_flag:
            print(">--{0:^10}--<".format("一覧"))
            for row in result:
                id = row[0]
                author = row[1]
                book_name = row[2]
                print("{0:<10}| {1:<10}| {2:<10}".format(id, author, book_name))
        else:
            print("棚には何もありません")
    
    #著者名で本を検索して抽出する処理
    def search_book_by_author(self, author):
        search_sql = "SELECT * FROM  {0} WHERE author='{1}'".format(self.name, author)
        cursor.execute(search_sql)
        result = cursor.fetchall()
        dt_exist_flag = 1 if len(result) != 0 else 0

        if dt_exist_flag:
            print(">--{0:^10}--<".format("検索結果"))
            for row in result:
                id = row[0]
                author = row[1]
                book_name = row[2]
                print("{0:<10}| {1:<10}| {2:<10}".format(id, author, book_name))
        else:
            print("\n該当するデータは見つかりませんでした。")

    #idを指定してデータを削除する処理
    def remove_book_by_id(self, id):
        del_flag = int(input("削除していいの(´･ω･`)?[0:NG/1:OK]"))
        del_sql = "DELETE FROM {0} WHERE id='{1}'".format(self.name, id)
        if del_flag:
            cursor.execute(del_sql)
            connect.commit()
            print("id:{0}のデータを削除しました".format(id))
        else:
            pass

# shelf = BookShelf("お気に入り")
# インスタンスしたオブジェクトの名前
# print(shelf)
# 追加
# shelf.add_book("論語と算盤", "渋沢栄一")
# shelf.add_book("脳・心・人工知能", "甘利俊一")
# shelf.add_book("留魂録", "吉田松陰")
# 一覧表示
# shelf.list_book()
# 削除
# shelf.remove_book("論語と算盤")
# 一覧表示
# shelf.list_book()