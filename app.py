import sqlite3
from bottle import Bottle, request, template

app = Bottle()

# Create a SQLite database and a students table
conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')
conn.commit()

# Create - Add a new student
@app.route('/add', method='POST')
def add_student():
    name = request.forms.get('name')
    age = request.forms.get('age')
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO students (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    conn.close()
    return "Student added: {} (Age: {})".format(name, age)

# Read - List all students
@app.route('/')
def list_students():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()
    return template('student_list', students=students)

# Update - Edit an existing student
@app.route('/edit/<student_id>', method='GET')
def edit_student(student_id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
    student = cursor.fetchone()
    conn.close()
    if student:
        return template('student_update', student=student,student_id=student_id)
    else:
        return "Student not found"

@app.route('/update/<student_id>', method='POST')
def update_student(student_id):
    name = request.forms.get('name')
    age = request.forms.get('age')
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE students SET name = ?, age = ? WHERE id = ?', (name, age, student_id))
    conn.commit()
    conn.close()
    return "Student updated: {} (Age: {})".format(name, age)

# Delete - Remove a student
@app.route('/delete/<student_id>')
def delete_student(student_id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()
    return "Student deleted"

if __name__ == '__main__':
    app.run(host='localhost', port=8080)
