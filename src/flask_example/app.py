import secrets
import string
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# Список для зберігання паролів
passwords = []
password_id_counter = 0


@app.route('/')
def index():
  return render_template('index.html', passwords=passwords)


# Додавання нового запису (сервіс, логін, пароль)
@app.route('/add', methods=['POST'])
def add():
  global password_id_counter
  service = request.form['service']
  username = request.form['username']
  password = request.form['password']

  if service and username and password:
    password_id_counter += 1
    new_entry = {
        'id': password_id_counter,
        'service': service,
        'username': username,
        'password': password,
    }
    passwords.append(new_entry)
  return redirect(url_for('index'))


# Видалення запису за ID
@app.route('/delete/<int:id>')
def delete(id):
  global passwords
  passwords = [item for item in passwords if item['id'] != id]
  return redirect(url_for('index'))


# Генерація випадкового надійного пароля
@app.route('/generate')
def generate():
  alphabet = string.ascii_letters + string.digits + '!@#$%^&*'
  generated_pass = ''.join(secrets.choice(alphabet) for _ in range(12))
  return {'password': generated_pass}


if __name__ == '__main__':
  app.run(debug=True)