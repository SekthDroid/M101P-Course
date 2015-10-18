
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
</ul>
