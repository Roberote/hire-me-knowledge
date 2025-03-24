# Uma empresa precisa de um programa para validar os e-mails dos funcionários.
# O e-mail corporativo deve seguir as seguintes regras:
# O domínio do e-mail deve ser @empresa.com.
# O nome de usuário (parte antes do @) deve:
# Conter apenas letras minúsculas, números, pontos (.) ou underlines (_).
# Começar com uma letra.
# Ter entre 5 e 15 caracteres.
# Tarefa:
# Crie um programa em Python que:
# Peça ao usuário para digitar um e-mail.
# Verifique se o e-mail é válido de acordo com as regras acima.
# Informe ao usuário se o e-mail é válido ou não.
# ==============================================
# Exemplos de e-mails válidos:
# joao.silva@empresa.com
# maria_123@empresa.com
# carlos.souza@empresa.com
# Exemplos de e-mails inválidos:
# joao@empresa.com (nome de usuário muito curto)
# 123mario@empresa.com (nome de usuário começa com número)
# joao.silva@outlook.com (domínio incorreto)
# joão.silva@empresa.com (caractere inválido no nome de usuário)
import re # Importei o módulo regex para usar no código.

listaoun = (input('É uma lista de emails?(Y/N) \n->'))

listaoun1 = listaoun.title()

if listaoun1 == 'Y':
    print('Ainda não sei fazer, estamos juntos!')
    quit()
else:
    email = str(input('Digite o seu email: ')) # Lê o email do usuário
if email.count('@') >= 1:
    emaildiv = email.split('@',2) # Cria uma variavel pra trabalhar com a parte antes do @ e depois do @, por isso o comando email.split('@', 2). o @ fala onde deve ser a separação, o 2 fala o máximo de separações, não é necessário mas queria garantir que ia ficar tudo certinho.
else:
    print('Digite um email, não um texto!')

emaildiv1 = emaildiv[0] # Aqui eu crio uma variavel pra parte antes do @ para checar o tamanho usando o comando len(emaildiv1), me facilitou um pouco.

print(emaildiv[0])
print(emaildiv[1])


if emaildiv[1] not in ['empresa.com', 'empresa.com.br', 'empresaglobal.com']: # Aqui eu crio um "checador" pra confirmar se a parte depois do @ tem os domínios solicitados.
    print('Email inválido. \nO domínio DEVE ser "@empresa.com", "@empresa.com.br" ou "empresaglobal.com". \nPrograma fechando!') # Mensagem de erro caso não tenha o domínio solicitado.
    quit() # encerra a análise já que deu inválido.
elif not re.match(r'^[a-z0-9._]+$', emaildiv[0]): # Aqui eu crio uma análise um pouco complexa, ele analisa usando o código re.match (do módulo regex), o r serve pra falar que a string é crua, depois '^(o circunflexo demarca o inicio da interpretação da string pelo re.match, daí eu coloco o que eu quero que seja permitido, no caso a-z (minusculas de "a" até "z"), 0-9 (numeros de "1" a "9"), "_" e ".", depois eu uso o + pra confirmar que tem um ou mais desse no email (pelo menos um desses vai ter na hora de digitar o email, obrigatoriamente) e uso o $ pra fechar a interpretação da string q o ^ tinha iniciado, depois coloco emaildiv[0], que é o que eu quero analisar (parte antes do @) e pronto, linha explicada.
    print('Email inválido. \nApenas letras minúsculas, números, pontos (.) ou underlines (_) e letras sem acentuação. \nPrograma fechando.') # Erro caso tenha algum caractere não permitido.
    quit() # encerra a análise já que deu inválido.
elif not emaildiv[0].islower(): # Aqui eu checo se o email começa com uma letra, e não tem o possível problema de iniciar com uma letra maiúscula, já que uma das validações necessárias é que TODAS as letras sejam minúsculas.
    print('Email inválido. \nO email deve começar com uma letra. \nPrograma fechando.')  # Mensagem de erro caso não comece com uma letra.
    quit() # encerra a análise já que deu inválido.
elif len(emaildiv1) <= 5: # Garante que a parte anterior ao @ do email tem mais de 5 dígitos
    print('Email inválido. \nEmail muito curto!. \nPrograma fechando.') # Mensagem de erro por ter menos de 5 digitos
    quit() # encerra a análise já que deu inválido.
elif len(emaildiv1) >= 15: # Garante que a parte anterior ao @ do email tem menos de 15 dígitos
    print('Email inválido. \nEmail muito longo!. \nPrograma fechando.')# Mensagem de erro por ter mais de 15 digitos
    quit() # encerra a análise já que deu inválido.
else:
    print(f'O email {email} foi aprovado! \n-> A empresa irá entrar em contato assim que possível!') # Mensagem de sucesso com o email válido!

