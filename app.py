from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

products = [
    {'id': 1, 'name': 'Mobil 1 5W-30', 'price': 25000, 'image': 'mobil1.jpeg'},
    {'id': 2, 'name': 'Castrol GTX 10W-40', 'price': 22000, 'image': 'castrol.jpeg'},
    {'id': 3, 'name': 'Shell Helix Ultra 5W-40', 'price': 24000, 'image': 'shell.jpeg'},
    {'id': 4, 'name': 'Total Quartz 9000 5W-40', 'price': 23000, 'image': 'total.jpeg'},
    {'id': 5, 'name': 'Valvoline SynPower 5W-30', 'price': 21000, 'image': 'valvoline.jpeg'},
    {'id': 6, 'name': 'Pennzoil Platinum 5W-30', 'price': 20000, 'image': 'pennzoil.jpeg'},
    {'id': 7, 'name': 'Liqui Moly Synthoil 5W-40', 'price': 27000, 'image': 'liqui_moly.jpeg'},
    {'id': 8, 'name': 'ZIC X7 5W-30', 'price': 19000, 'image': 'zic.jpeg'},
    {'id': 9, 'name': 'Amsoil Signature Series 5W-30', 'price': 30000, 'image': 'amsoil.jpeg'},
    {'id': 10, 'name': 'Fuchs Titan GT1 5W-40', 'price': 28000, 'image': 'fuchs.jpeg'}
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
