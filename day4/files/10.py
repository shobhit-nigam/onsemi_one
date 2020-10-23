# files
# write
# seek

fa = open("new_data.txt", "w")

fa.write("love you 3000 times\n")
fa.write("why so serious")

print(fa.tell())
fa.seek(0)
print(fa.tell())
fa.close()
