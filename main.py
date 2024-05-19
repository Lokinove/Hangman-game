import random
print("Hangman Game!")
tries = 5
words_list = ["apple", "banana","pneumonoultramicroscopicsilicovolcanoconiosis"]
word = words_list[random.randint(0, len(words_list)-1)]

user_input = []
for i in word:
  user_input.append("_")
answer = []
for i in word:
  answer.append(i)
while tries > 0:

  if user_input == answer:
    print("\n You won!")
    break
  
  print("\n" + ' '.join(user_input))
  print(f"you have {tries} tries left")
  user_guess = str(input("which letter do you want to guess? ")) 
  
  print(user_input)
  if user_guess in answer:
    for i in range(len(answer)):
      if user_guess == answer[i]:
        user_input[i] = user_guess
  else:
    tries -= 1
    
if tries == 0:
    print ("You lose")