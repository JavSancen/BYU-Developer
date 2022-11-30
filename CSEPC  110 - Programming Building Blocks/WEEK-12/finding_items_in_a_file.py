
with open("/home/francisco/Downloads/books_and_chapters.txt") as books:

    max_book = -1
    min_book = +1
    max_name = "" # It doesn't matter what you set this to, it just needs to be declared
    min_name = ""

    for item in books:
        item = item.strip()
        part = item.split(",")

        book_name = part[0] # name is the first part
        book = int(part[1])

        if books > max_book:
            # This is the new max
            max_book = books

            # Also save this product name as the max name
            max_book = book_name
        elif books < max_book and book < 10:
            min_book = books
            min_people = book_name

    print(f"The maximum age is: {max_book}")
    print(f"The person with the maximum age is: {max_book}")
    print(f"The maximum age is: {min_book}")
    print(f"The person with the minimum age is: {min_people}")