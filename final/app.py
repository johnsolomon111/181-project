from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/restaurant', methods=['GET'])
def index():
	return render_template('louie.html')

@app.route('/delivery', methods=['GET'])
def delivery():
	return render_template('delivery.html')

@app.route('/menu', methods=['GET'])
def menu():
	return render_template('menu.html')

@app.route('/contact', methods=['GET'])
def contact():
	return render_template('contact.html')

@app.route('/customer', methods=['GET'])
def customer():
	return render_template('customer.html')


if __name__ == '__main__':
	app.run(debug=True)
