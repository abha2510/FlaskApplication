from flask import Flask,request,redirect,render_template

app = Flask(__name__)

data={}

@app.route('/')
def welcome():
    return 'Welcome to the Flask App!'

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        key = request.form.get('key')
        value = request.form.get('value')
        if key and value:
            data[key] = value
            return redirect('/read')
    return '''
        <h1>Create New Entry</h1>
        <form action="/create" method="post">
            <label for="key">Key:</label>
            <input type="text" id="key" name="key"><br><br>
            <label for="value">Value:</label>
            <input type="text" id="value" name="value"><br><br>
            <input type="submit" value="Create">
        </form>
    '''

@app.route('/read')
def read():
    return f"<h1>Current State of Dictionary:\n</h1><pre>{data}</pre>"

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        key = request.form.get('key')
        value = request.form.get('value')
        if key and value:
            if key in data:
                data[key] = value
                return redirect('/read')
    return '''
        <h1>Update Entry</h1>
        <form action="/update" method="post">
            <label for="key">Key:</label>
            <input type="text" id="key" name="key"><br><br>
            <label for="value">New Value:</label>
            <input type="text" id="value" name="value"><br><br>
            <input type="submit" value="Update">
        </form>
    '''

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        key = request.form.get('key')
        if key in data:
            del data[key]
            return redirect('/')
    return '''
        <h1>Delete Entry</h1>
        <form action="/delete" method="post">
            <label for="key">Key:</label>
            <input type="text" id="key" name="key"><br><br>
            <input type="submit" value="Delete">
        </form>
    '''

if __name__ == '__main__':
    app.run()
