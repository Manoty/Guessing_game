secret_number = 8
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    try:
        guess = int(input('guess: '))
        guess_count += 1
        if guess == secret_number:
            print('You won!')
            break
    except ValueError:
        print("please enter a valid no")
else:
    print("sorry, you failed")    