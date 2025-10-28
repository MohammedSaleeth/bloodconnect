from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage (will reset when app stops)
donors = []
requests_list = []

@app.route('/')
def home():
    return render_template('home.html', donors=donors, requests=requests_list)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        donor = {
            'name': request.form['name'],
            'phone': request.form['phone'],
            'email': request.form['email'],
            'blood_type': request.form['blood_type'],
            'city': request.form['city'],
            'notes': request.form['notes']
        }
        donors.append(donor)
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/request', methods=['GET', 'POST'])
def request_blood():
    if request.method == 'POST':
        req = {
            'patient_name': request.form['patient_name'],
            'blood_type_needed': request.form['blood_type_needed'],
            'units': request.form['units'],
            'city': request.form['city'],
            'contact_name': request.form['contact_name'],
            'contact_phone': request.form['contact_phone'],
            'notes': request.form['notes']
        }
        requests_list.append(req)
        return redirect(url_for('home'))
    return render_template('request.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

