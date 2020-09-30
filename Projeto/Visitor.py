from database import *


def initialize():
    while True:
            print('\nQuer tirar uma dúvida? Comece selecionando uma categoria\n')

            categories = select_all_categories()

            print('ID \tDescrição')
            for item in range(len(categories)):
                print(f'{categories[item][0]}  \t{categories[item][1]}')

            selectedCategoryId = str(input('\nSelecione uma categoria informando seu ID: '))

            response = select_category_by_id(selectedCategoryId)

            if response:
                break

        while True:
            print(f'\nCategoria selecionada: {response[0][1]}')

            questions = select_all_questions_by_category(selectedCategoryId)

            print('ID \tDescrição')
            for item in range(len(questions)):
                print(f'{questions[item][0]}  \t{questions[item][1]}')

            selectedQuestionId = str(input('Selecione uma pergunta informando seu ID: '))

            response = select_category_by_id(selectedCategoryId)

            if response:
                break

        while True:
            print(f'\nPergunta selecionada: {response[0][1]}')

            answers = select_all_questions_by_category(selectedCategoryId)

            print('ID \tDescrição')
            for item in range(len(answers)):
                print(f'{answers[item][0]}  \t{answers[item][1]}')

            print('\n0 - Nenhuma das respostas\n')

            selectedAnswersId = str(input('Eleja uma resposta como a mais útil informando seu ID: '))

            if selectedAnswersId == 0:
                print('\nEntre em contato com nossos assistentes!')
                print('00 0000-0000')
                break
            else:
                increment_answer_rank(selectedAnswersId)
                print('Obrigado pelo feedback!')
                break
