def store_answers(answers_list: list):
    with open('answers.txt', 'w') as f:
        f.write(str(answers_list))

answers = ['D', 'B', 'B,', 'B', 'D', 'D', 'C', 'A', 'A', 'A', 'D,', 'B', 'A', 'B', 'D', 'A', 'D', 'C', 'D', 'A', 'B', 'D', 'B', 'A', 'B', 'B', 'A', 'D', 'A', 'B', 'D', 'C', 'C', 'A', 'A', 'A', 'B', 'D', 'B', 'A']
store_answers(answers)
