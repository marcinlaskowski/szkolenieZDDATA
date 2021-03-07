#
# with open("plik.txt", encoding="UTF-8") as f:
#     lines = f.readlines()
#
# print(lines)
# for line in lines:
#     print(line)
#
#     # Dodatkowo białe znaki
#     print(line.rstrip())

# 2 sposób
# with open("plik.txt", encoding="UTF-8") as f:
#     for line in f:
#         print(line.rstrip())

# with open("plik2.txt", "w", encoding="UTF-8") as f:
#     f.write("Hello world2")

with open("plik2.txt", "a", encoding="UTF-8") as f:
    f.write("\n Hello world2")

    f.writelines(["AB", "CD", "EF"])
    for word in ["AB", "CD", "EF"]:
        f.write(word + '\n')

