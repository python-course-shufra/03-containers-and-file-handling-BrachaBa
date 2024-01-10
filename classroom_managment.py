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


def index_of_student(name):
    for i, student in enumerate(classroom):
        if student['name'] == name:
            return i


def add_student(name, email=None):
    if email is None:
        email = f'{name.lower()}@example.com'
    classroom.append({'name': name, 'email': email, 'grades': []})


def delete_student(name):
    index = index_of_student(name)
    del classroom[index]


def set_email(name, email):
    classroom[index_of_student(name)]['email'] = email


def add_grade(name, profession, grade):
    classroom[index_of_student(name)]['grades'].append((profession, grade))


def avg_grade(name, profession):
    for student in classroom:
        if student['name'] == name:
            grades = [g[1] for g in student['grades'] if g[0] == profession]
            return sum(grades) / len(grades) if grades else None


def get_professions(name):
    for g in classroom[index_of_student(name)]['grades']:
        if (g[0] not in list):
            list.append(g[0])
    return list
