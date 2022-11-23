with open("/home/francisco/Downloads/books.txt") as books_list:
    for line in books_list:
        line = line.strip()

        parts = line.split("\n")

        book_name = parts[0]

        print(book_name)

