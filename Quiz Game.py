from questionsmarvel import quiz as marvel_quiz
from questionsdc import quiz as dc_quiz

def check_ans(question, answer, attempts, score, quiz):
      if quiz[question]['answer'].lower() == answer.lower():
            print(f"Correct Answer! \nYour score is {score + 1}!")
            return True
      else:
            print(f"Wrong Answer :( \nYou have {attempts - 1} attempts left. Try again...")
            return False

score = 0

for question in marvel_quiz:
    attempts = 3
    while attempts > 0:
        print(marvel_quiz[question]['question'])
        answer = input("Enter Answer: ")
        check = check_ans(question, answer, attempts, score, marvel_quiz)
        if check:
            score += 1
            break
        attempts -= 1
    
for question in dc_quiz:
    attempts = 3
    while attempts > 0:
        print(dc_quiz[question]['question'])
        answer = input("Enter Answer: ")
        check = check_ans(question, answer, attempts, score, dc_quiz)
        if check:
            score += 1
            break
        attempts -= 1
