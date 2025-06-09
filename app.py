@app.route('/brokers')
def list_brokers():
    cursor.execute("SELECT * FROM brokers")
    brokers = cursor.fetchall()
    return render_template("brokers.html", brokers=brokers)

@app.route('/add_broker', methods=["GET", "POST"])
def add_broker():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cursor.execute("INSERT INTO brokers (name, email, phone) VALUES (%s, %s, %s)", 
                       (name, email, phone))
        conn.commit()
        return redirect('/brokers')
    return render_template("add_broker.html")
