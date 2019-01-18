from question import Question
question_prompt=[
    "What is the color of the apple?\n(a)Red/Green\n(b)Purple\n(c)Orange\n\n",
    "What is the color of the banana?\n(a)Red/Pink\n(b)Yellow\n(c)Orange\n\n",
    "What is the color of the Mango?\n(a)Red/Blue\n(b)Green\n(c)Orange\n\n"
]
questions=[
    Question(question_prompt[0],"a"),
    Question(question_prompt[1],"b"),
    Question(question_prompt[2],"b")
]
def run_test(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got "+str(score)+" out of "+str(len(questions))+" Questions")

run_test(questions)