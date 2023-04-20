from flask import Flask
from flask import request

app = Flask(__name__)
listofmessages = []


@app.route('/')
def hello_world():
    return 'hello friend!'


@app.route('/status')
def hello_mir():
    return {
        'messages_count': len(listofmessages)
    }


@app.route('/api/Messanger',methods=['POST'])
def SendMessage():
    msg = request.json
    print(msg)
    listofmessages.append(msg)
    msgtext = f"{msg['Username']}<{msg['TimeStamp']}>:{msg['MessageText']}"
    print(f"Всего сообщений {len(listofmessages)}. Посланное сообщение:{msgtext}")
    return f" Сообщение {msgtext} успепшно отправлено. Всего сообщений{len(listofmessages)}"


@app.route('/api/Messanger/<int:id>')
def  GetMessage(id):
    print(id)
    if id>=0 and id <len(listofmessages):
        print(listofmessages[id])
        return listofmessages[id],200
    else:
        return 'error 404'
if __name__ == '__main__':
        app.run()
