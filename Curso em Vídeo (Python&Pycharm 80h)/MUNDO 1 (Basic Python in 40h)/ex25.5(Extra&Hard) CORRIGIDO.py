# A DIFERENÇA DESSE PARA O OUTRO É QUE NO OUTRO EU CHECAVA SE TINHA OU NÃO, E EM ALGUNS CASOS O
# QUE NÃO TINHA PASSAVA E O QUE TINHA ERA BARRADO. AQUI EU SÓ CHECO O QUE NÃO TEM, SE TEM ELE IGNORA.
# O OUTRO CÓDIGO ALÉM DE MAIS DEVAGAR QUE ESSE, TINHA MUITAS BRECHAS PARA ERROS.
# ALÉM DE USO DO REGEX DE UMA FORMA UM POUCO CONTURBADA



import re

# Pergunta se é uma lista de e-mails
listaoun = input('É uma lista de e-mails? (Y/N)\n-> ').strip().title()

if listaoun == 'Y':
    print('Ainda não sei fazer, estamos juntos!')
    quit()
else:
    email = input('Digite o seu e-mail: ').strip()

# Verifica se o e-mail contém exatamente um "@"
if email.count('@') != 1:
    print('Email inválido. \nO e-mail deve conter exatamente um "@". \nPrograma fechando!')
    quit()

# Divide o e-mail em nome de usuário e domínio
emaildiv = email.split('@')
usuario, dominio = emaildiv[0], emaildiv[1]

# Verifica o domínio
if dominio not in ['empresa.com', 'empresa.com.br', 'empresaglobal.com']:
    print('Email inválido. \nO domínio DEVE ser "@empresa.com", "@empresa.com.br" ou "@empresaglobal.com". \nPrograma fechando!')
    quit()

# Verifica o nome de usuário
if not re.match(r'^[a-z][a-z0-9._]{4,14}$', usuario):
    print('Email inválido. \nO nome de usuário deve começar com uma letra minúscula e conter apenas letras minúsculas, números, pontos (.) ou underlines (_). \nPrograma fechando.')
    quit()

# Se passou por todas as verificações, o e-mail é válido
print(f'O e-mail "{email}" foi aprovado! \n-> A empresa irá entrar em contato assim que possível!')