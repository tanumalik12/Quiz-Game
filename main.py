questions = ("Which planet has the most moons?: ",
             "How many Bones do we have in an Ear?: ",
             "What country has won the most World Cups?: ")
options = (("A.Uranus ","B.Earth ","C.Mars ","D.Saturn "),
           ("A.9 ","B.3 ","C.15 ","D.5 "),
           ("A.Australia ","B.Russia ","C.Brazil ","D.Japan "))
answers = ("D", "B", "C")
guesses=[]
score = 0
question_num = 0
for question in questions:
    print("--------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
guess = input("Enter (A, B, C, D): ").upper()
guesses.append(guess)
if guess == answers[question_num]:
    score += 1
    print("CORRECT!")
else:
    print("INCORRECT!")
    print(f"{answers[question_num]} is the correct answer")

question_num += 1

print("---------------------------------")
print("            RESULTS              ")
print("---------------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
    print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
    print()

score = (score / len(questions) * 100)
print(f"your score is: {score}%")
