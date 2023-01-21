import json
from flask import Flask, jsonify, request
app = Flask(__name__)

students = [
    {   'id': 1, 'project_topic': 'hospital'},
    {   'id': 2, 'project_topic': 'office'},
    {   'id': 3, 'project_topic': 'school'}
]

  
@app.route('/students', methods = ['GET'])
def get_students():
    return jsonify(students)


@app.route('/students/<int:id>', methods=['GET'])
def get_student_by_id(id: int):
    student = get_student(id)
    if student is None:
        return jsonify( { 'error': 'Student does not exist'} ), 404
    return jsonify(student)

def get_student(id):
    return next( (s for s in students if s['id'] == id), None)

def student_is_valid(student):
    for key in student.keys():
        if key != 'project_topic':
            return False
    return True

@app.route('/students', methods=['POST'])
def create_student():
    global nextID
    student = json.loads(request.data)
    if not student_is_valid(student):
        return jsonify( { 'error': 'Invalid'} ), 400
    nextID = 4
    student['id'] = nextID
    nextID += 1
    students.append(student)
    return '', 201, { 'location': f'/students/{student["id"]}' }


@app.route('/students/<int:id>', methods = ['PUT'])
def update_student(id: int):
    student = get_student(id)
    if student is None:
        return jsonify( { 'error': 'Student does not exist.'} ), 404
    update_student = json.loads(request.data)
    if not student_is_valid(update_student):
        return jsonify( { 'error': 'Invalid'}), 400
    student.update(update_student)
    return jsonify(student)

@app.route('/students/<int:id>', methods = ['DELETE'])
def delete_student(id: int):
    global students
    student = get_student(id)
    if student is None:
        return jsonify( { 'error': 'Student does not exist.'} ), 404
    students = [s for s in students if s['id'] != id]
    return jsonify(student), 200

if __name__ == '__main__':
    app.run(debug = True)
