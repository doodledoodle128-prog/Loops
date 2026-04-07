string = input("Choose your word: ")
char = input("Choose your letter: ")

count = 0
i = 0

while i < len(string):

    if (string[i] == char):
        count = count + 1
    i = i + 1

print("There are",count,char, "in the word")
