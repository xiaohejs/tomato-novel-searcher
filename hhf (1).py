import requests as req

def search_books():
    key = input("请输入搜索关键词：")
    page = 1

    while True:
        #API
        url = f"https://api5-normal-lf.fqnovel.com/reading/bookapi/search/page/v/?query={key}&aid=1967&channel=0&os_version=0&device_type=0&device_platform=0&iid=466614321180296&passback={{(page-1)*10}}&version_code=999"
        response = req.get(url)

        if response.status_code == 200:
            data = response.json()
            if data['code'] == 0:
                books = data['data']
                if not books:
                    print("没有找到相关书籍。")
                    break
                for i, book in enumerate(books):
                    book_data = book['book_data'][0]
                    print(f"{i + 1}. 名称：{book_data['book_name']} 作者：{book_data['author']} ID：{book_data['book_id']} 字数：{book_data['word_number']}")
                
                #选择搜索结果
                while True:
                    choice_ = input("请选择一个结果, 输入 r 以重新搜索：")
                    if choice_ == "r":
                        break
                    elif choice_.isdigit() and 1 <= int(choice_) <= len(books):
                        chosen_book = books[int(choice_) - 1]
                        book_id = chosen_book['book_data'][0]['book_id']
                        print(f"已选择书籍：{chosen_book['book_data'][0]['book_name']}")
                        return book_id
                    else:
                        print("输入无效，请重新输入。")
            else:
                print(f"搜索出错，错误码：{data['code']}")
                break
        else:
            print(f"请求失败，状态码：{response.status_code}")
            break

if __name__ == "__main__":
    book_id = search_books()
    if book_id:
        print(f"返回的书籍 ID: {book_id}")