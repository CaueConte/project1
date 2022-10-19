import pydf
import smtplib
import ssl
import email.message
from datetime import date

#dados
while True:
    nomecompleto = input("Digite o nome completo: ")
    emailpaciente = input("Digite o email: ")
    rg = input("Digite o RG: ")
    telefone = input("Digite o telefone: ")
    anonascimento = input("DIgite o ano de nascimento: ")
    calculoidade = date.today().year - int(anonascimento)
    nomedopdf = input("Digite um nome para o arquivo pdf: ")

    if calculoidade < 65:
        pdf = pydf.generate_pdf(f'<h1>{nomecompleto}</h1><p>{emailpaciente}</p><p>{rg}</p><p>{telefone}</p><p>{anonascimento}</p>')
        with open(f'{nomedopdf}.pdf', 'wb') as f:
            f.write(pdf)
    elif calculoidade > 65:
        pdf = pydf.generate_pdf(f'<h1>{nomecompleto}, EM GRUPO DE RISCO</h1><p>{emailpaciente}</p><p>{rg}</p><p>{telefone}</p><p>{anonascimento}</p>')
        with open(f'{nomedopdf}.pdf', 'wb') as f:
            f.write(pdf)
    else:
        print()

    #email de confirmacao
    msg = email.message.Message()
    msg['Subject'] = ("Clinica Saúde")


    body = f"""
    <p>Olá {nomecompleto}</p>
    <p>Sua consulta foi agendada, seus dados foram salvos em pdf</p>
    <p>Por favor confirme seus dados: telefone: {telefone}, rg: {rg}, ano de nascimento: {anonascimento}
    caso aja alguma divergencia contatar a clinica</p>


    <p>Atenciosamente, Recepção</p>
    """

    #por seugranca e privacidade retirei o email e a senha que usei do codigo. 
    msg['From'] = '' #digitar o email entre aspas
    password = '' #digitar senha do email entre aspas
    msg['To'] = emailpaciente
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body)

    context = ssl.create_default_context()
    with smtplib.SMTP('smtp.gmail.com', 587) as conexao:
        conexao.ehlo()
        conexao.starttls(context=context)
        conexao.login(msg['From'], password)
        conexao.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
    continuar = input("Deseja cadastrar outro paciente? sim/nao: ")
    if continuar in ["nao"]:
        break
    if continuar in ["sim"]:
        pass
    else:
        print("Opcao invalida, tente novamente")
        break
