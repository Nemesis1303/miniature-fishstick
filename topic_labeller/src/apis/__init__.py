from flask_restx import Api

from .ns_topic_labeller import api_ns as ns1

api = Api(
    title="Topic Labeller API",
    version='1.0',
    description='This RESTful API ...',
)

api.add_namespace(ns1, path='/topiclabeller')

print("llega bien aquí")
