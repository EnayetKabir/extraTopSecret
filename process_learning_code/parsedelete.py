APPLICATION_ID = "GyUfmGoQbBBvBCKyH9r7qGK1GgWo6kYKLdi4MPjA"
REST_API_KEY = "SmoaTb8g7ld84iheL13k568C7pT1ybPJjOJc0set"

from parse_rest.connection import register
# Alias the Object type to make clear is not a normal python Object
from parse_rest.datatypes import Object
#first register the app
register(APPLICATION_ID, REST_API_KEY)


#define a Python class that inherts from parse_rest.datatypes.Object
class tastyThangz(Object):
   pass

#delete our new object, by calling the save() method
bigDaddy.delete()


