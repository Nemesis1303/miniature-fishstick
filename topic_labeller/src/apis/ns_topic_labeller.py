from flask_restx import Namespace, Resource, reqparse
from src.core.promt import TopicLabeller

# ======================================================
# Define namespace for managing collections
# ======================================================
api_ns = Namespace("TopicLabeller", description="API.")

# Create TopicLabeller object
tl = TopicLabeller(model="gpt-4")

# Define parser to take inputs from user
parser1 = reqparse.RequestParser()
parser1.add_argument(
    'chemical_description', help="String with the chemical description.", required=True)
parser2 = reqparse.RequestParser()
parser2.add_argument(
    'chemical_description', help="List of strings, each string being the chemical description of a different topic.", required=True)


@api_ns.route('/getLabel/')
class GetLabel(Resource):
    @api_ns.doc(parser=parser1)
    def get(self):
        args = parser1.parse_args()
        try:
            label = tl.get_label(args['chemical_description'])
            return label, 200
        except Exception as e:
            return str(e), 500


@api_ns.route('/getLabels/')
class GetLabels(Resource):
    @api_ns.doc(parser=parser2)
    def get(self):
        args = parser2.parse_args()
        try:
            labels = tl.get_labels(args['chemical_description'])
            return labels, 200
        except Exception as e:
            return str(e), 500
