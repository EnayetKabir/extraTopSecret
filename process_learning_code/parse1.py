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

#creating Object subclass by string name
objectName = "favoriteShit"
myObject = Object.factory(objectName)

#instantiate new class with some parameters
brownSugar = tastyThangz(fuxGiven=1337, they_call_me='Brown Sugar', extraFresh=False)

#change or set new parameters afterwards
brownSugar.extraFresh = True
brownSugar.amountOfSwag = 11


#creating Object subclass by string name
objectName2 = "favoriteShit"
myObject2 = Object.factory(objectName2)

#instantiate new class with some parameters
bigDaddy = tastyThangz(fuxGiven=0, they_call_me='Big Daddy', extraFresh=True)

#change or set new parameters afterwards
bigDaddy.amountOfSwag = 20

#save our new object, by calling the save() method
bigDaddy.save()
brownSugar.save()
print bigDaddy.objectId
print brownSugar.objectId

