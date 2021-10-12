
import pymysql
import json

def lambda_handler(event, context):
    tabela = 'Usuario'
    connection = pymysql.connect(host='',
                             user='',
                             password='',
                             database='',
                             cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        acao = ''
        if 'acao' in event:
            acao = event['acao']
            payload = event
        else:
            try:
                payload =  json.loads(event['body'])
                acao = payload['acao']
            except Exception as ex:
                print(ex)

        if acao == 'inserir':
            sql = "INSERT INTO {} (nome, idade,cargo) VALUES ('{}', {}, '{}')".format(
                tabela,
                payload['nome'],
                payload['idade'],
                payload['cargo']
            )
            cursor.execute(sql)
            connection.commit()
            connection.close()
            return {'statusCode': 201,'body': json.dumps("Adicionado")}
        
        if acao == "selecionaId":
            sql = "SELECT * FROM {} WHERE id={} ;".format(tabela, payload['id'])
            cursor.execute(sql)
            result = cursor.fetchone()
            connection.close()
            return {'statusCode': 200,'body': json.dumps(result)}

        if acao == "atualizar":
            sql = "UPDATE {} set nome='{}', idade={}, cargo='{}'  WHERE id= {}".format(
                tabela,
                payload['nome'],
                payload['idade'],
                payload['cargo'],
                payload['id']
            )
            cursor.execute(sql)
            connection.commit()
            connection.close()
            return {'statusCode': 200,'body': json.dumps('atualizado com sucesso')}

        if acao == "buscaTodos":
            cursor.execute('SELECT * from {}'.format(tabela))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            connection.close()
            return {'statusCode': 200,'body': json.dumps(rows)}

        if acao == "excluirId":
            sql = 'DELETE from {} where id={} '.format(tabela, payload['id'])
            cursor.execute(sql)
            connection.commit()
            connection.close()
            return {'statusCode': 200,'body': json.dumps('Removido com sucesso')}

        
        connection.close()
        return {'statusCode': 400,'body': json.dumps('acao invalida')}

      

 





