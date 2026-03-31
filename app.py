from flask import Flask, render_template, request, send_file, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('submissions.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS subscriptions
                 (id INTEGER PRIMARY KEY, name TEXT, email TEXT, details TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS task_submissions
                 (id INTEGER PRIMARY KEY, task_id INTEGER, user_name TEXT, result TEXT, score INTEGER)''')
    conn.commit()
    conn.close()

init_db()

# Sample tasks
tasks = [
    {"id": 1, "description": "Analyze the dataset and find the average value.", "data_file": "data1.csv"},
    {"id": 2, "description": "Classify the images in the zip file.", "data_file": "images.zip"},
    {"id": 3, "description": "Solve the puzzle and submit the solution.", "data_file": "puzzle.txt"}
]

@app.route('/')
def index():
    conn = sqlite3.connect('submissions.db')
    c = conn.cursor()
    c.execute("SELECT user_name, SUM(score) as total_score FROM task_submissions GROUP BY user_name ORDER BY total_score DESC")
    leaderboard_data = c.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks, leaderboard=leaderboard_data)

@app.route('/subscribe', methods=['POST'])
def subscribe():
    name = request.form['name']
    email = request.form['email']
    details = request.form['details']
    conn = sqlite3.connect('submissions.db')
    c = conn.cursor()
    c.execute("INSERT INTO subscriptions (name, email, details) VALUES (?, ?, ?)", (name, email, details))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/download/<filename>')
def download(filename):
    return send_file(os.path.join('static', 'data', filename), as_attachment=True)

@app.route('/submit_task', methods=['POST'])
def submit_task():
    task_id = int(request.form['task_id'])
    user_name = request.form['user_name']
    result = request.form['result']
    # Simple scoring: random or based on result
    score = len(result)  # dummy score
    conn = sqlite3.connect('submissions.db')
    c = conn.cursor()
    c.execute("INSERT INTO task_submissions (task_id, user_name, result, score) VALUES (?, ?, ?, ?)", (task_id, user_name, result, score))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/leaderboard')
def leaderboard():
    conn = sqlite3.connect('submissions.db')
    c = conn.cursor()
    c.execute("SELECT user_name, SUM(score) as total_score FROM task_submissions GROUP BY user_name ORDER BY total_score DESC")
    leaderboard_data = c.fetchall()
    conn.close()
    return render_template('leaderboard.html', leaderboard=leaderboard_data)

if __name__ == '__main__':
    app.run(debug=True)