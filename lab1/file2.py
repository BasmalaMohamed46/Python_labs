import random
#Question 1

list=[1,1,2,3,3,4,5,5,6,7,7,8,9,9]
print("Original list: ",list)
for i in list:
    if list.count(i)>1:
        list.remove(i)
print("List after removing duplicates: ",list)

#Question 2

def string_length(str):
    str_len = len(str)
    front = ""
    back = ""
    
    if str_len % 2 == 0:
        front = str[:str_len // 2]
        back = str[str_len // 2:]
    else:
        front = str[:(str_len + 1) // 2]
        back = str[(str_len + 1) // 2:]
    
    return front, back

str_input1 = input("Enter a string: ")
str_input2 = input("Enter a string: ")
front1, back1 = string_length(str_input1)
front2, back2 = string_length(str_input2)

print("fornt of str1 and str2: ", front1+front2)
print("back of str1 and str2: ", back1+back2)

#Question 3

def uniqness(list):
    for i in list:
        if list.count(i)>1:
            return False
    return True

list1=[1,1,2,3,3,4,5,5,6,7,7,8,9,9]
list2=[1,2,3,4,5,6,7,8,9]
print(uniqness(list1))
print(uniqness(list2))

#Question 4

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                swapped = True
        if(not swapped):
            break

arr = [12,5,88,23,40,2,46]
bubble_sort(arr)
print("Sorted array:", arr)

#Question 5

def guess_game(tries=10):
    random_number=random.randint(1,100)
    user_guesses=[]
    while(tries>0):
        user_guess=int(input("Enter your guess: "))
        if(user_guess>100 or user_guess<1):
            print("Please enter a number between 1 and 100")
            continue
        if(user_guess in user_guesses):
            print("You have already guessed that number")
            continue
        if(user_guess < random_number):
            print("The number is higher than your guess")
            tries-=1
            user_guesses.append(user_guess)
        elif(user_guess > random_number):
            print("The number is lower than your guess")
            tries-=1
            user_guesses.append(user_guess)
        elif(user_guess == random_number):
            print("Congratulations! You have guessed the number correctly")
            tries-=1
            if(tries<10):
                print("You have guessed the number in",10-tries,"tries")
                print("Now try to guess the new number")
                guess_game(tries)
            else:
                print("You have guessed the number in 10 tries")
                play_again=input("Do you want to play again? (yes/no): ")
                if(play_again=="yes"):
                    guess_game()
                else:
                    print("Thank you for playing")
                    return
            return
    print("You have run out of tries")
    play_again=input("Do you want to play again? (yes/no): ")
    if(play_again=="yes"):
        guess_game()
    else:
        print("Thank you for playing")
        return
print("Welcome to the number guessing game")    
guess_game()


        






