'''wt i ve to make:
35 quiz question files
each file has 50 questions
each question has 4 options(1 of them right other 3 wrong)
question sequence for each file should be random
36 answer files
each file has answers for the exact sequence in which questions were asked
'''

'''how i ll do it:
import random and os
make 2 new directories called quiz questions and quiz answers
make a list called useful material
for 50 times
make a list called answers of any 3 random capitals using random.choice and add to the list capital[i]
shuffle the list
add to useful material a formatted question like:
'capital of {state[i]} is:
a)answers[0]
b)answers[1]
c)answers[2]
d)answers[3]
acutal answer:capital[i]'
now exit the loop
for 35 times
shuffle useful material
create questions list from useful material
create answers list from useful material
change directory to quiz questions
open new txt file called quiz{i}
for question in question
write the question to quiz{i}
close quiz{i}
change directory to quiz answers
open new txt file called answers{i}
for answer in answers
write the answer to answers{i}
close answers{i}

'''
import random, os
states_capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
states = list(states_capitals.keys())
capitals = list(states_capitals.values())
useful_material = []
for i in range(50):
    answers = []
    req = capitals.pop(i)
    for y in range(3):
        answers.append(str(random.choice(capitals)))
    answers.append(req)
    capitals.insert(i, req)
    random.shuffle(answers)
    useful_material.append(f'''
capital of {states[i]} is
a){answers[0]}
b){answers[1]}
c){answers[2]}
d){answers[3]}
actual answer:{capitals[i]}''')

for x in range(1, 36):
    random.shuffle(useful_material)
    questions = []
    answers = []
    for string in useful_material:
        question, answer = string.split('actual answer:')
        questions.append(question)
        answers.append(answer)


    os.chdir('E:\\pranil\\python\\automate the boring shit\\quiz questions')
    quiz_f = open(f'quiz_st{x}', 'w')
    count = 1
    for que in questions:
        quiz_f.write(f'\n{count}) '+ que)
        count += 1
    quiz_f.close()
    os.chdir('..\\quiz answers')
    quiz_ans_f = open(f'answers_st{x}', 'w')
    count_new = 1
    for ans in answers:
        quiz_ans_f.write(f'{count_new})'+ ans + '\n')
        count_new += 1
    quiz_ans_f.close()












