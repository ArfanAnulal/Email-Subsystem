#Simple Mood Diary Script As An Example#

print('My Mood Diary')
mood = input('How are you feeling today? ')
#Saves the input as the variable 'mood'#
text_file = open("MoodDiary.txt", "a")
#Opens or creates the .txt file, sharing the directory of the script#
text_file.write('*')
text_file.write(mood)
text_file.write("\n")
#Writes the variable into the .txt file#
text_file.close()
#Closes the .txt file#
