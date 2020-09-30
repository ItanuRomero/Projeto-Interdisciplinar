from database import *


def initialize():           
    while True:
        options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

        print('\nO que você gostaria de fazer?\n')
        print('1 - Visualizar todas as categorias')
        print('2 - Inserir nova categoria')
        print('3 - Remover uma categoria')

        print('\n')

        print('4 - Visualizar perguntas de uma categoria')
        print('5 - Inserir uma nova pergunta para uma categoria')
        print('6 - Remover uma pergunta')

        print('\n')

        print('7 - Visualizar respostas de uma pergunta')
        print('8 - Inserir uma nova resposta para uma pergunta')
        print('9 - Remover uma resposta')

        print('\n')

        print('10 - SAIR')

        userChoice = str(input('\n'))

        if userChoice not in options:
            print('\nCódigo inserido não é inválido\n')

        if userChoice == '1':
            print(f'\nOpção selecionada: {userChoice} - Visualizar todas as categorias\n')

            categories = select_all_categories()

            print('ID \tDescrição')
            for item in range(len(categories)):
                print(f'{categories[item][0]}  \t{categories[item][1]}')

        elif userChoice == '2':
            print(f'\nOpção selecionada: {userChoice} - Inserir nova categoria\n')

            insert_category(str(input('Insira o nome da categoria: ')))

            print('\nCategoria inserida\n')

        elif userChoice == '3':
            print(f'\nOpção selecionada: {userChoice} - Remover uma categoria\n')

            categoryId = str(input('Insira o ID da categoria: '))

            category = select_category_by_id(categoryId)

            if not category:
                print('\nCategoria não encontrada')
            else:
                delete_category(categoryId)
                print('\nCategoria removida')

        elif userChoice == '4':
            print(f'\nOpção selecionada: {userChoice} - Visualizar perguntas de uma categoria\n')

            categoryId = str(input('Insira o ID da categoria: '))

            category = select_category_by_id(categoryId)

            if not category:
                print('\nCategoria não encontrada')
            else:
                questions = select_all_questions_by_category(categoryId)

                print(f'\nCategoria selecionada: {category[0][1]}')
                print('\nID \tPergunta')
                for item in range(len(questions)):
                    print(f'{questions[item][0]}  \t{questions[item][1]}')

        elif userChoice == '5':
            print(f'\nOpção selecionada: {userChoice} - Inserir uma nova pergunta para uma categoria\n')

            categoryId = str(input('Insira o ID da categoria: '))

            category = select_category_by_id(categoryId)

            if not category:
                print('\nCategoria não encontrada')
            else:
                print(f'\nCategoria selecionada: {category[0][1]}')

                question = str(input('Informe a pergunta: '))

                insert_question(categoryId, question)

                print('\nPergunta inserida')

        elif userChoice == '6':
            print(f'\nOpção selecionada: {userChoice} - Remover uma pergunta\n')

            questionId = str(input('Insira o ID da pergunta: '))

            question = select_question_by_id(questionId)

            if not question:
                print('\nPergunta não encontrada')
            else:
                delete_question(questionId)
                print('\nPergunta removida')

        elif userChoice == '7':
            print(f'\nOpção selecionada: {userChoice} - Visualizar respostas de uma pergunta\n')

            questionId = str(input('Insira o ID da pergunta: '))

            question = select_question_by_id(questionId)

            if not question:
                print('\nPergunta não encontrada')
            else:
                print(f'\nPergunta selecionada: {question[0][1]}')

                answers = select_all_answers_by_question_id(questionId)

                print('\nID \tResposta')
                for item in range(len(answers)):
                    print(f'{answers[item][0]}  \t{answers[item][1]}')

        elif userChoice == '8':
            print(f'\nOpção selecionada: {userChoice} - Inserir uma nova resposta para uma pergunta\n')

            questionId = str(input('Insira o ID da pergunta: '))

            question = select_question_by_id(questionId)

            if not question:
                print('\nPergunta não encontrada')
            else:
                print(f'\nPergunta selecionada: {question[0][1]}')

                answer = str(input('Informe a resposta: '))

                insert_answer(questionId, answer)

                print('\nResposta inserida')

        elif userChoice == '9':
            print(f'\nOpção selecionada: {userChoice} - Inserir uma nova resposta para uma pergunta\n')

            answerId = str(input('Insira o ID da resposta: '))

            answer = select_answer_by_id(answerId)

            if not answer:
                print('\nResposta não encontrada')
            else:
                delete_answer(answerId)
                print('\nResposta removida')

        elif userChoice == '10':
            break