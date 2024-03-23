import os
from flask import Flask
from flask import request
from threading import Thread as th


class App:
    def __init__(self):

        app = Flask(__name__)

        self.path = f'/home/{os.getlogin()}'

        @app.post('/mypath')
        def mp():
            return f'{self.com("pwd")}'

        @app.post('/command')
        def command():
            c = request.form.get('command')
            
            return f"{self.com(c)}"

        @app.post('/file')
        def fl():
            text = request.form.get('data')
            name = request.form.get('name')
        
            with open(f'{self.path}/{name}', 'w') as fl:
                fl.write(text)

            return f"file: {name}"

        @app.post('/run')
        def rn():
            c = request.form.get('p')
            th(target=self.com, args=(c,)).start()

            return 'ok'

        @app.post('/ok')
        def ok():
            return 'ok'

        @app.post('/setpath')
        def setpath():
            self.path = request.form.get('path')

            return f'NONEOTV'

        @app.post('/cd')
        def cdp():
            self.path = self.path + '/' + request.form.get('path')

            return f'NONEOTV'

        app.run(debug=False, port=9090, host='localhost')

    def com(self, command):
        try:
            os.system(f'cd {self.path} && {command} > /home/{os.getlogin()}/.tmp')
            dat = open(f'/home/{os.getlogin()}/.tmp', 'r').read()
            os.remove(f'/home/{os.getlogin()}/.tmp')
            return dat.rstrip().strip()
        except:
            return 'error'


if __name__ == '__main__':
    App()