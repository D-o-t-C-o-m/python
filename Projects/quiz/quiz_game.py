print("Welcome to the Computer Quiz!")

playing = input("Do you want to play? (Yes / No): ")

if playing.lower() != "yes":
    print("Maybe later.")
    quit()

print("Great! Let's get started.")
score = 0

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does GPU stand for? ")

if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does ram stand for? ")

if answer.lower() == "random access memory":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")

if answer.lower() == "power supply unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

score_percent = score * 25 

print(f"You got {score}/4 questions correct for a {score_percent}% total score!")