from flask import Flask, render_template, jsonify, request
import processor


app = Flask(__name__)

app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'


@app.route('/', methods=["GET"])
def index():
    return render_template('chat.html')



@app.route('/get', methods=["GET", "POST"])
def chatbotResponse():

     
    the_question = request.form['question']

    response = processor.chatbot_response(the_question)

    return str(response)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
