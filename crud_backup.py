import mysql.connector as conectar

conexao = conectar.connect(
host='localhost',
user='root',
password='221122jv',
database='to_do_crud'
)

cursor = conexao.cursor()

rodar = 0

state = ['to do','doing','done']
state1 = 0
state2 = 0
state3 = 0
while rodar == 0 :
    print('-Você gostaria de adicionar,editar,mostrar ou sair?')
    askcrud = str(input())
    if askcrud == 'adicionar':
        print('-Qual será sua tarefa?')
        task = str(input())
        state1 = 1
        comando = f'insert into tarefas values(default, "{task}", {state1}, {state2}, {state3});'
        cursor.execute(comando)
        conexao.commit()

    elif askcrud == 'editar':
        print('-Qual tarefa você irá editar?')
        task = str(input())
        print('-Qual será o estado?')
        askstate = str(input())
        if askstate == state[1]:
            state2 = 1
            comando = f'update tarefas set tarefas.doing = {state2} where task = "{task}";'
            comando2 = f'update tarefas set tarefas.to_do = {state1} where task = "{task}";'
            cursor.execute(comando)
            conexao.commit()
            cursor.execute(comando2)
            conexao.commit()
        elif askstate == state[2]:
            state3 = 1
            comando = f'update tarefas set tarefas.done = {state3} where task = "{task}";'
            comando2 = f'update tarefas set tarefas.doing = {state2} where task = "{task}";'
            cursor.execute(comando)
            conexao.commit()
            cursor.execute(comando2)
            conexao.commit()

    elif askcrud == 'mostrar':
        print('-Escolha: to do, doing ou done')
        task = str(input())
        if task == state[0]:
            comando = f'select task from tarefas where tarefas.to_do = 1'
            cursor.execute(comando)
            result = cursor.fetchall()
            print('-Tarefas para fazer:' + str(result))
        elif task == state[1]:
            comando = f'select task from tarefas where tarefas.doing = 1'
            cursor.execute(comando)
            result = cursor.fetchall()
            print('-Tarefas em execução:' + str(result))
        elif task == state[2]:
            comando = f'select task from tarefas where tarefas.done = 1'
            cursor.execute(comando)
            result = cursor.fetchall()
            print('-Tarefas feitas:' + str(result))
    elif askcrud == 'sair':
        rodar = 1
    else:
        print('-Código não compatível, por favor tente novamente')


cursor.close()
conexao.close()