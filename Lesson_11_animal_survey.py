from Lesson_11_survey import survey

question = 'What is ur fav animals?'
surv = survey(question)

surv.show_question()
print('Enter Q for quitting')
while True:
    answer = input('Animal: ')
    if answer == 'q':
        break
    surv.save_answer(answer)

surv.show_results()