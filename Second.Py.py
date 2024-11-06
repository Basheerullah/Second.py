#python__quiz__game

questions=("How many elements are in the peridic table?:",
           "Which animal lays the largest egg?:",
           "what is the most absundant gas in the Earth atmosphere?:",
           "How many bones are in human body?:",
           "Witch planit in the solar system is the hottest?:")

Options=("A.116", "B.117", "C.118", "D.119"),
        ("A. Wale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
        ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
        ("A. 206", "B. 207", "C. 208", "D. 209"),
        ("A. Mercury", "B. Venus", "C. Earth", "D. Mars")

Answers=("C", "D", "A", "A", "B")
Guesses= []
Score= 0
question_num= 0

for question in questions:
    print("---------------")
    print(question)
    for option in options [question_num]:
        print(option)

guess= input("Enter(A, B, C, D,): ").upper()
guesses.append(guess)
if guess == answers[question_num]:
    Score += 1
    print("CORRECT!")
else:
    print("INCORRECT!")
    print(f"{answers[question_num]}  is the correct answer")
    question_num += 1

print("---------------")
print("    RESULTS    ")
print("---------------")

print("answer; ", end="")
for answer in answers:
    print(answer,end=" ")
    print()

print("guesses; ", end="")
for guess in guesses:
    print(guess,end=" ")
    print()

    score=int(score / len(questions) * 100)
    print(f"your score is: {score}%")