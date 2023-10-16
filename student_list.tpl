<!DOCTYPE html>
<html>
<head>
    <title>Student CRUD</title>
</head>
<body>
    <h1>Students:</h1>
    <ul>
        % for i, student in enumerate(students):
            <li>{{i + 1}}. Name: {{student[1]}}, Age: {{student[2]}} - <a href="/edit/{{student[0]}}">Edit</a> | <a href="/delete/{{student[0]}}">Delete</a></li>
        % end
    </ul>
    <form action="/add" method="post">
        <input type="text" name="name" placeholder="Name" required>
        <input type="number" name="age" placeholder="Age" required>
        <input type="submit" value="Add Student">
    </form>
</body>
</html>
