from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://lvjcfvnbjpypnp:b72e0c4572c5e73b5af3c451d2f4cfb69d77f569a11fcb406b5fb470a46ba848@ec2-54-83-197-230.compute-1.amazonaws.com:5432/dpnm7g9f3mtrb'
