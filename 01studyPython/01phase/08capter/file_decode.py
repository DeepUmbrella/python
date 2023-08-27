# open file

file = open("opentext.txt", "w", encoding="utf-8")
file.write(input("Enter your text: "))
file.close()

# use with open file API syntax:
# with open("opentext.txt", "w", encoding="utf-8") as file:    this api can automatic close the file
#     file.write(input("Enter your text: "))

with open("opentext.txt", "+w", encoding="utf-8") as file01:
    file01.write("nihao\nnimen\n")

    # use file01.flush() to flush the buffer to disk
    file01.flush()
