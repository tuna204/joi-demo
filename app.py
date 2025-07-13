from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

products = [
    {'id': 1, 'name': 'Engine Oil 1L', 'price': 5000, 'image': 'oil1.jpeg'},
    {'id':2, 'name': 'Engine Oil 4L', 'price': 18000, 'image': 'oil4.jpeg'},
    {'id': 3, 'name': 'Synthetic Oil 5W-30', 'price': 22000, 'image':'synthetic.jpeg'}
]

@app.route('/')
def home():
    return render_template('home.html', products=products)

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        return redirect(url_for('confirmation'))
    return render_template('checkout.html')

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

if __name__=='__main__':
    app.run(debug=True)
