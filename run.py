from threading import Thread as th
import os

def run_servcon():
    os.system('python3 ./server.py')

def run_serveo():
    os.system('ssh -R 80:localhost:9090 serveo.net')

if __name__ == '__main__':
    th(target=run_serveo).start()
    th(target=run_servcon).start()