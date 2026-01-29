user_name=input("Enter username: ")
new_username=user_name.capitalize()
print("Username: " + str(new_username))


paragraph = input("Enter a paragraph: ")
count_word = input("Enter the word that you want to count: ")
x=str(count_word)
print("Number of times the word '" + str(count_word) + "' is repeated in the given sentence is : " + str(paragraph.count(x)))