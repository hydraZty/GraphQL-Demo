GraphQL Live demo for Decentfox internal sharing meeting
================================

Getting started
---------------

First you'll need to get the source of the project. Do this by cloning the
whole demo repository:

```bash
# Get the example project code
git clone https://github.com/hydraZty/GraphQL-Demo.git
cd GraphQL-Demo
```

It is good idea (but not required) to create a virtual environment
for this project.

```bash
# Create a virtualenv in which we can install the dependencies
pipenv shell
```

Now we can install our dependencies:

```bash
pip install -r requirements.txt
```

We also need to change the postgresql location in

```
./database.py
```

Now the following command will setup the database, and start the server:

```bash
./app.py

```


Now head on over to
[http://127.0.0.1:5000/graphql](http://127.0.0.1:5000/graphql)
and run some queries!
