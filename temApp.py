from db import get_connection

'''
try:
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call consulta_alumnos()')
        resulset = cursor.fetchall()
        for row in resulset:
            print(row)
except Exception as ex:
    print('ERROR')
'''
'''
try:
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call consulta_alumno(%s)', (12,))
        resulset = cursor.fetchall()
        for row in resulset:
            print(row)
except Exception as ex:
    print('ERROR')
'''

try:
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call agrega_alumno(%s,%s,%s)', ('Eduardo','Chia','chia@chia.com'))
    connection.commit()
    connection.close()
except Exception as ex:
    print('ERROR')