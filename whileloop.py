time = 0
# while time != 10:
#     print("I love you")
#     time += 1

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False

while guess != secret_word:
    if guess_count < guess_limit:
        guess = input("please try a new word: ")
        guess_count += 1
    else:
        out_of_guess = True
        break
if out_of_guess:
    print("You loss, the secret word is {}".format(secret_word))
else:
    print("You win!")