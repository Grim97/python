import time

'''
A very simple quiz game inspired fron internet - youtube.
@param questions is a list of dictionaries which has questions, answers and options.
@function run_quiz utilizes this questions to present data to the user CLI.
Based on user input will be validated and Score is displayed at the end.
'''

questions = [
{
    'question': "What does the range() function return?",
    'options': ['a) A list of integers', 'b) A range object', 'c) A tuple of integers', 'd) A dictionary of integers'],
    'answer': 'b'
},
{
    'question': "What is the output of bool([])?",
    'options': ['a) True', 'b) False', 'c) None', 'd) Error'],
    'answer': 'b'
},
{
    'question': "How do you check if a key exists in a dictionary?",
    'options': ['a) Using the find() method', 'b) Using the in keyword', 'c) Using the exists() function', 'd) Using the contains() method'],
    'answer': 'a'
}
]

def run_quiz():
    score = 0
    for que in questions:
        print(que['question'])
        time.sleep(1)
        for option in que['options']:
            print(option)
        user_response = input("Enter your choice - a or b or c or d ??? ").lower()
        if user_response == que['answer']:
            score += 1
    
    print("Great job!!! Calculating your score!")
    time.sleep(5)
    print(f"You have scored - {score} out of {len(questions)}")


def main():
    run_quiz()


if __name__ == '__main__':
    main()