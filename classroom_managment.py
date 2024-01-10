classroom = [
    {
        'name': 'Alice',
        'email': 'alice@example.com',
        'grades': [
            ('math', 91),
            ('english', 78),
            ('math', 90),
            ('history', 34),
            ('math', 95),
        ],
    },
    {
        'name': 'Bob',
        'email': 'bob@example.com',
        'grades': [
            ('math', 85),
            ('english', 92),
            ('history', 75),
        ],
    },
    {
        'name': 'Charlie',
        'email': 'charlie@example.com',
        'grades': [
            ('physics', 78),
            ('english', 81),
            ('english', 89),
            ('history', 68),
            ('english', 82),
            ('physics', 91),
        ],
    },
]


def add_student(name, email=None):
    """Add a new student to the classroom
    with the following keys:
    'name': the given name
    'email': if email is given use it otherwise use <name>@example.com
             in lowercase, you can use the `s.lower()` method
    'grade': initialize with empty list
    """
    if email is None:
        email = f'{name.lower()}@example.com'
    classroom.append({'name': name, 'email': email, 'grades': []})
    pass


def delete_student(name):
    """Delete a student from the classroom"""
    global classroom
    classroom = [student for student in classroom if student['name'] != name]
    pass


def set_email(name, email):
    """Sets the email of the student"""
    for student in classroom:
        if student['name'] == name:
            student['email'] = email
    pass


def add_grade(name, profession, grade):
    """Adds a new grade to the student grades"""
    for student in classroom:
        if student['name'] == name:
            student['grades'].append((profession, grade))
    pass


def avg_grade(name, profession):
    """Returns the average of grades of the student
    in the specified profession
    """
    for student in classroom:
        if student['name'] == name:
            grades = [g[1] for g in student['grades'] if g[0] == profession]
            return sum(grades) / len(grades) if grades else None
    pass


def get_professions(name):
    """Returns a list of unique professions that student has grades in"""
    for student in classroom:
        if student['name'] == name:
            return list(set(g[0] for g in student['grades']))
        return []
    pass
