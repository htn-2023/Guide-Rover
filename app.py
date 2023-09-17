from flask import Flask
import sys
sys.path.append('/communication')
from communication.recorder import record
from communication.decision import make_decisoin
from communication.transcriber import transcribe
import threading

app = Flask(__name__)


@app.route('/')
def main():
    # Record audio and chatgpt conversation
    c1 = threading.Thread(target=record)
    c2 = threading.Thread(target=transcribe)
    c3 = threading.Thread(target=make_decisoin)

    c1.start()
    c2.start()
    c3.start()

    c1.join()
    c2.join()
    c3.join()
    return {'analysis_result': 'The program is running'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
