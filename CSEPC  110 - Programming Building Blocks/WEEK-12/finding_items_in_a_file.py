largest_num = -1
largest_book = ""

print("which volume of scriptures they would like to learn about?")
users_scripture = input("(for example, Old Testament, New Testament, Book of Mormon, Doctrine and Covenants, Pearl of Great Price). : "
)

with open("/home/francisco/Downloads/books_and_chapters.txt") as books_file:
    for lines in books_file:

        clean_lines = lines.strip()
        parts = clean_lines.split(":")

        scripture = parts[2]
        book = parts[0]
        chapter = int(parts[1])

        if scripture.lower() == users_scripture.lower():

            if chapter > largest_num:

                largest_num = chapter
                largest_book = book

print(f"The book with the most chapters is: {largest_book}")
print(f"It has {largest_num} chapters.")
