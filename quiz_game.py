print("Welcome to the Quiz Game!")
playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()
    
    if playing.upper() != "YES":
        quit()

print("Okay! Let's Play :)")
score = 0

answer = input("What does CPU stands for?") 
if answer == "Central Processing Unit":
    print("Correct!")
    score += 1
    score = score + 1
else:
    print("It's Incorrect!")
    score -= 1

answer = input("Who is the Founder of Python?")
if answer == "Guido Van Rosseum":
    print("Correct!")
    score += 1
else:
    print("It's Incorrect!")
    score -= 1

answer = input("Which year was Python created?")
if answer == "1991":
    print("Correct!")
    score += 1
else:
    print("It's Incorrect!")
    score -= 1

answer = input("what does GPU stands for?")
if answer == "Graphics Processing Unit":
    print("Correct!")
    score += 1
else:
    print("It's Incorrect!")
    score -= 1
    
    print("Your final Score you got " + str(score) + " questions correct!")
    
    print("You got " + str((score/5)* 100) + " %.")
    
             
    
    
            
          
          