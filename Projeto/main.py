from database import *

print('Bem vindo ao PinaTalk!\n')

while True:
  print('\nQual tipo de usuário você é?\n')
  print('1 - Administrador')
  print('2 - Visitante')
  print('3 - SAIR')

  userType = str(input('\n'))

  options = ['1', '2', '3']

  if userType == '3':
    break

  if userType == '1':
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

        categories = selectAllCategories()

        print('ID \tDescrição')      
        for item in range(len(categories)):
          print(f'{categories[item][0]}  \t{categories[item][1]}')

      elif userChoice == '2':
        print(f'\nOpção selecionada: {userChoice} - Inserir nova categoria\n')
        
        insertCategory(str(input('Insira o nome da categoria: ')))

        print('\nCategoria inserida\n')

      elif userChoice == '3':
        print(f'\nOpção selecionada: {userChoice} - Remover uma categoria\n')

        categoryId = str(input('Insira o ID da categoria: '))

        category = selectCategoryById(categoryId)

        if not category:
          print('\nCategoria não encontrada')
        else: 
          deleteCategory(categoryId)
          print('\nCategoria removida')

      elif userChoice == '4':        
        print(f'\nOpção selecionada: {userChoice} - Visualizar perguntas de uma categoria\n')

        categoryId = str(input('Insira o ID da categoria: '))

        category = selectCategoryById(categoryId)

        if not category:
          print('\nCategoria não encontrada')
        else: 
          questions = selectAllQuestionsByCategory(categoryId)

          print(f'\nCategoria selecionada: {category[0][1]}')
          print('\nID \tPergunta')      
          for item in range(len(questions)):
            print(f'{questions[item][0]}  \t{questions[item][1]}')
                        
      elif userChoice == '5':
        print(f'\nOpção selecionada: {userChoice} - Inserir uma nova pergunta para uma categoria\n')
        
        categoryId = str(input('Insira o ID da categoria: '))

        category = selectCategoryById(categoryId)

        if not category:
          print('\nCategoria não encontrada')
        else:
          print(f'\nCategoria selecionada: {category[0][1]}')

          question = str(input('Informe a pergunta: '))
          
          insertQuestion(categoryId, question)

          print('\nPergunta inserida')        
        
      elif userChoice == '6':
        print(f'\nOpção selecionada: {userChoice} - Remover uma pergunta\n')

        questionId = str(input('Insira o ID da pergunta: '))

        question = selectQuestionById(questionId)

        if not question:
          print('\nPergunta não encontrada')
        else: 
          deleteQuestion(questionId)
          print('\nPergunta removida')
          
      elif userChoice == '7':
        print(f'\nOpção selecionada: {userChoice} - Visualizar respostas de uma pergunta\n')

        questionId = str(input('Insira o ID da pergunta: '))

        question = selectQuestionById(questionId)

        if not question:
          print('\nPergunta não encontrada')
        else:
          print(f'\nPergunta selecionada: {question[0][1]}')

          answers = selectAllAnswersByQuestionId(questionId)

          print('\nID \tResposta')      
          for item in range(len(answers)):
            print(f'{answers[item][0]}  \t{answers[item][1]}')
      
      elif userChoice == '8':
        print(f'\nOpção selecionada: {userChoice} - Inserir uma nova resposta para uma pergunta\n')

        questionId = str(input('Insira o ID da pergunta: '))

        question = selectQuestionById(questionId)

        if not question:
          print('\nPergunta não encontrada')
        else:
          print(f'\nPergunta selecionada: {question[0][1]}')

          answer = str(input('Informe a resposta: '))
          
          insertAnswer(questionId, answer)

          print('\nResposta inserida')
      
      elif userChoice == '9':
        print(f'\nOpção selecionada: {userChoice} - Inserir uma nova resposta para uma pergunta\n')

        answerId = str(input('Insira o ID da resposta: '))

        answer = selectAnswerById(answerId)

        if not answer:
          print('\nResposta não encontrada')
        else: 
          deleteAnswer(answerId)
          print('\nResposta removida')

      elif userChoice == '10':
        break  

  if userType == '2':
    while True:
      print('\nQuer tirar uma dúvida? Comece selecionando uma categoria\n')
    
      categories = selectAllCategories()
    
      print('ID \tDescrição')      
      for item in range(len(categories)):
        print(f'{categories[item][0]}  \t{categories[item][1]}')
    
      selectedCategoryId = str(input('\nSelecione uma categoria informando seu ID: '))
    
      response = selectCategoryById(selectedCategoryId)

      if response:
        break
    
    while True:
      print(f'\nCategoria selecionada: {response[0][1]}')

      questions = selectAllQuestionsByCategory(selectedCategoryId)
    
      print('ID \tDescrição')      
      for item in range(len(questions)):
        print(f'{questions[item][0]}  \t{questions[item][1]}')
    
      selectedQuestionId = str(input('Selecione uma pergunta informando seu ID: '))

      response = selectCategoryById(selectedCategoryId)

      if response:
        break
    
    while True:
      print(f'\nPergunta selecionada: {response[0][1]}')

      answers = selectAllQuestionsByCategory(selectedCategoryId)

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
        incrementAnswerRank(selectedAnswersId)
        print('Obrigado pelo feedback!')
        break

  if userType not in options:
    print('\nCódigo inserido não é inválido\n')