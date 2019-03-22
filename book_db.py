import book_shelf_db

#本棚オブジェクトを操作する処理
while True:

    select_mode = int(input("1:本棚を選択/2:本を追加する/3:一覧表示/4:検索/5:削除/[0:操作をやめる]"))

    if select_mode == 1:
        shelf_name = input("本棚の名前を決めてください:")
        shelf = book_shelf_db.BookShelf(shelf_name)
    elif select_mode == 2:
        author = input("著者を入力してください:")
        book = input("本のタイトルを入力してください:")
        shelf.add_book(author, book)
    elif select_mode == 3:
        shelf.list_book()
    elif select_mode == 4:
        author = input("検索したい著者名を入力してください:")
        shelf.search_book_by_author(author)
    elif select_mode == 5:
        id = input("idを指定して削除してください:")
        shelf.remove_book_by_id(id)
    elif select_mode == 0:
        break