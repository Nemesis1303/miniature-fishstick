from flask_restx import Namespace, Resource, reqparse
from src.core.topic_labeller import TopicLabeller

# ======================================================
# Define namespace for managing collections
# ======================================================
api = Namespace("TopicLabeller", description="Given a chemical description or a list of chemical descritpions, returns the topic label or labels of the chemical description(s).")

# Create TopicLabeller object
tl = TopicLabeller(model="gpt-4")

# Define parser to take inputs from user
parser1 = reqparse.RequestParser()
parser1.add_argument(
    'chemical_description', help="String with the chemical description.", required=True)
parser2 = reqparse.RequestParser()
parser2.add_argument(
    'chemical_description', help="List of strings, each string being the chemical description of a different topic.", required=True)


@api.route('/getLabel/')
class GetLabel(Resource):
    #@api.doc(parser=parser1)
    @api.doc(
    parser=parser1,
    responses={
        200: 'Success: Labels generated successfully',
        500: 'Internal Server Error: An error occurred while generating labels.',
    })
    def get(self):
        args = parser1.parse_args()
        try:
            label = tl.get_label(args['chemical_description'])
            return label, 200
        except Exception as e:
            return str(e), 500

@api.route('/getLabels/')
class GetLabels(Resource):
    @api.doc(parser=parser2)
    def get(self):
        args = parser2.parse_args()
        try:
            labels = tl.get_labels(args['chemical_description'])
            return labels, 200
        except Exception as e:
            return str(e), 500
