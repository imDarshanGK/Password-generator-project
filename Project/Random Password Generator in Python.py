import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','-','+']
print("Welcome to Password Generator!")
num_letters = int(input("How many letters you want in you password?\n"))
num_numbers = int(input("How many numbers you want in you password?\n"))
num_symbols = int(input("How many symbols you want in you password?\n"))
password_list = []
for paswld in range(1,num_letters+1):
   chr = random.choice(letters)
   password_list+=chr
for paswld in range(1,num_numbers+1):
   chr = random.choice(numbers)
   password_list+=chr
for paswld in range(1,num_symbols+1):
   chr = random.choice(symbols)
   password_list+=chr
random.shuffle(password_list)
password = ''.join(password_list)
print(f"Your generated password is: {password}")
