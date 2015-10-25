
<h1>M101P: MongoDB for developers</h1>

<p>All resources I am using for the M101P course by <a href="https://university.mongodb.com">MongoDB University</a></p>

<h2>Content</h2>
<h3>Week 1</h3>
<ul>
    <li>hello_bottle.py
        <p>A sample file to start running the Bottle framework <br/>
            <code>python hello_bottle.py</code>
        </p>
    </li>
    <li>hello_bottle.py
        <p>A sample file to connect a python file with Mongo <br/>

            To be able to execute this, you just need to do:<br/><br/>

            Execute this command in your terminal (This will start MongoDB in your machine, you need to install MongoDB first to be able to go through this): <br/>
            <code>SekthDroid-Mac:week1 SekthDroid$ mongod</code>
            <br/>
            <br/>
            Execute this one to execute the python file <br/>
            <code>SekthDroid-Mac:week1 SekthDroid$ python hello_pymongo.py</code>
        </p>
    </li>
    <li>hello_app.py
        <p>A file used like a glue for Bottle Framework and MongoDB. It can be executed and tested using a browser, in this case, using the url "http://localhost:8082/"<br/>

            <code>SekthDroid-Mac:week1 SekthDroid$ mongod</code>
            <br/>
            <code>SekthDroid-Mac:week1 SekthDroid$ python hello_app.py</code>
        </p>
    </li>
    <li>bottle_url_handler.py
      <p>A file used to setup some handlers for the urls, as we can see, there are 2 defined urls, one for the root web, which will pring <code>Hello World</code> and another one that will be executed when we access to the url http://localhost:8080/test_page and we will see the text <code>This is a test page</code></p>
    </li>
    <li>hello_bottle_things.py
      <p>A file used to setup templates with bottle framework, and pass it some values that will be rendered with the template processor.
      The content of the template is located in /week1/hello_world.tpl.</p>
    </li>
    <li>hello_bottle_things_2.py
      <p>This is a file that will get the data from a form request, and will render another template with the data the user wrote in the form</p>
    </li>
</ul>
<h3>Week 2</h3>
<p>In order to be able to work with the exercises, we will need to run the file within the folder <b>seeder</b>, which is a common js file that will seed a database
    with some dummy data. Just execute it in a shell like this: <br/><br/>
    <code>SekthDroid-Mac:Week2 SekthDroid$ mongo < create_student_collection.js</code>
    <br/>
    <br/>
    This will fill a db called school with 300 dummy data.</p>
<br/>
<ul>
    <li>using_find.py
        <p>This is a simple file that will execute a query to fetch only one element based in a query, then it will be printed.<br/>
            <code>python using_find.py</code>
        </p>
    </li>
</ul>
