import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    code_folder = 'Code'
    index_file = 'index.html'
    if os.path.isdir(code_folder):
        app.static_folder = os.path.abspath(code_folder)
        if os.path.isfile(os.path.join(app.static_folder, index_file)):
            app.run()
        else:
            print(f"{index_file} not found in {code_folder}")
    else:
        print(f"{code_folder} not found")

