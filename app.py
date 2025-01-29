from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta de bienvenida
@app.route('/')
def welcome():
    return render_template('welcome.html')

# Ruta del Curriculum Vitae (CV)
@app.route('/cv')
def cv():
    return render_template('index.html')

# Ruta de agradecimiento
@app.route('/thankyou', methods=['POST'])
def thank_you():
    user_name = request.form.get('userName')
    if user_name:
        message = f"Thank you, {user_name}, for visiting my CV!"
    else:
        message = "Please enter your name to receive a thank you message."
    return render_template('thankyou.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
