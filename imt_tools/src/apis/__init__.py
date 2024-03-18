from flask_restx import Api

from .ns_topic_labeller import api as ns1
from .ns_equivalences_suggester import api as ns2

api = Api(
    title="IMT Tools API",
    version='1.1',
    description='This RESTful API provides access to the IMT Tools: TopicLabeller and EquivalencesSuggester.',
)

api.add_namespace(ns1, path='/topiclabeller')
api.add_namespace(ns2, path='/equivalencessuggester')