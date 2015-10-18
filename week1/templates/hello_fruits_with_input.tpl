<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>Hello world!</title>
</head>
<body>
    <p>
        Welcome {{username}}
    </p>
    <ul>
        %for item in things:
            <li>{{item}}</li>
        %end
    </ul>
<form action="/favourite_fruit" method="POST">
    <label>
        What is your favourite fruit?
        <input type="text" name="fruit" size="40" value="">
    </label>
    <input type="submit" value="Submit">
</form>
</body>
</html>