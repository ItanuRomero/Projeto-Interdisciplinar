from database import *


def initialize_visitor():
    while True:
        print('\nQuer tirar uma dúvida? Comece selecionando uma categoria\n')

        categories = select_all_categories()

        print('ID \tDescrição')
        for item in range(len(categories)):
            print(f'{categories[item][0]}  \t{categories[item][1]}')

        selected_category_id = str(input('\nSelecione uma categoria informando seu ID: '))

        response = select_category_by_id(selected_category_id)

        if response:
            break
    while True:
        print(f'\nCategoria selecionada: {response[0][1]}')

        questions = select_all_questions_by_category(selected_category_id)

        print('ID \tDescrição')
        for item in range(len(questions)):
            print(f'{questions[item][0]}  \t{questions[item][1]}')

        selected_question_id = str(input('Selecione uma pergunta informando seu ID: '))

        response = select_question_by_id(selected_question_id)

        if response:
            break

    while True:
        print(f'\nPergunta selecionada: {response[0][1]}')

        answers = select_all_questions_by_category(selected_category_id)

        print('ID \tDescrição')
        for item in range(len(answers)):
            print(f'{answers[item][0]}  \t{answers[item][1]}')

        print('\n0 - Nenhuma das respostas\n')

        selected_answers_id = str(input('Eleja uma resposta como a mais útil informando seu ID: '))

        if selected_answers_id == 0:
            print('\nEntre em contato com nossos assistentes!')
            print('00 0000-0000')
            break
        else:
            increment_answer_rank(selected_answers_id)
            print('Obrigado pelo feedback!')
            break
