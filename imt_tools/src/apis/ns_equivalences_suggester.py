from flask_restx import Namespace, Resource, reqparse
from src.core.equivalences_suggester import EquivalencesSuggester

# ======================================================
# Define namespace for managing collections
# ======================================================
api = Namespace("EquivalencesSuggester", description="Given an acronym/list of acronyms and a context, returns the disambiguated word(s).")

# Create TopicLabeller object
es = EquivalencesSuggester(model="gpt-4")

# Define parser to take inputs from user
parser1 = reqparse.RequestParser()
parser1.add_argument(
    'acronym', help="Acronym to disambiguate.", required=True)
parser1.add_argument(
    'context', help="Contenxt to disambiguate the acronym.", required=True)

parser2 = reqparse.RequestParser()
parser2.add_argument(
    'acronyms', help="List of strings, each string being an acronym to disambiguate.", required=True)
parser2.add_argument(
    'context', help="Contenxt to disambiguate the acronyms.", required=True)


@api.route('/disambiguateAcronym/')
class DisambiguateAcronym(Resource):
    @api.doc(
    parser=parser1,
    responses={
        200: 'Success: Acronym disambiguated successfully.',
        500: 'Internal Server Error: An error occurred while disambiguating the acronym.',
    })
    def get(self):
        args = parser1.parse_args()
        try:
            dis_word = es.get_dis(args['acronym'], args['context'])
            return dis_word, 200
        except Exception as e:
            return str(e), 500
        
@api.route('/disambiguateAcronyms/')
class DisambiguateAcronyms(Resource):
    @api.doc(
    parser=parser2,
    responses={
        200: 'Success: Acronyms disambiguated successfully.',
        500: 'Internal Server Error: An error occurred while disambiguating the acronyms.',
    })
    def get(self):
        args = parser2.parse_args()
        try:
            dis_words = es.get_dis_list(args['acronyms'], args['context'])
            return dis_words, 200
        except Exception as e:
            return str(e), 500