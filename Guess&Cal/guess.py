secret_num= 8
guess_cou = 0
guess_limit =3

while guess_cou < guess_limit:
   
    guess = int(input("Guess: "))
    guess_cou += 1
    if guess == secret_num:
        print("Yess! You Win!")
        break
else:
    print("OHHO! Sorry ;__; Try again!")
