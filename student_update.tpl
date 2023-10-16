<!DOCTYPE html>
<html>
<head>
    <title>Edit Student</title>
</head>
<body>
    <h1>Edit Student:</h1>
    <form action="/update/{{student[0]}}" method="post">
        <input type="text" name="name" value="{{student[1]}}" required>
        <input type="number" name="age" value="{{student[2]}}" required>
        <input type="submit" value="Update Student">
    </form>
</body>
</html>
