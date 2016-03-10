import json
import sys

json_str = open( sys.argv[1], 'r' ).read().upper()
python_recipes = json.loads( json_str )

ingr_attr = "INGREDIENTS"


CSV_ATTRIBUTES = []


# Get bag of ingredient_bag
ingredient_bag = []

# Take the ingredient_bag from each recipe to create a new attribute 
for recipe in python_recipes:
	for ingredient in recipe[ ingr_attr ]:
		# Seperate the words of each ingredient to make more features
		ingredient_words = ingredient.replace( ',', '' ).split( ' ' )
		for ingredient_word in ingredient_words:
			if ingredient_word not in ingredient_bag:
				ingredient_bag.append( ingredient_word )

ingredient_bag.remove( "CUISINE" )



''' 
	Ingredient Cleaning:
		anything we do NOT want as an attribute should be removed here
'''

ingredients_removed = 0
for ingredient in ingredient_bag:

	# Remove attributes shorter than 3 letters as they are probably not ingredients ( of, a, is, etc. )
	if len( ingredient ) <= 2:
		ingredient_bag.remove( ingredient )
		ingredients_removed += 1

print( "Removed {} ingredients because the length was less than 3".format( ingredients_removed ) )


ingredients_removed = 0
for ingredient in ingredient_bag:

	# Remove non-letters attributes
	if not ingredient.isalpha():
		ingredient_bag.remove( ingredient )
		ingredients_removed += 1

print( "Removed {} ingredients because it has non-letters".format( ingredients_removed ) )



# Gather attributes here
for ingredient in ingredient_bag:
	CSV_ATTRIBUTES.append( ingredient )

CSV_ATTRIBUTES.append( "CUISINE" )







CSV_SAMPLES = []
for recipe in python_recipes:
	ingredient_words = ' '.join( recipe[ ingr_attr ] ).split( ' ' )
	CSV_SAMPLES.append( ','.join( [ "1" if ingredient in ingredient_words else "0" for ingredient in ingredient_bag ] + [ str( recipe[ "CUISINE" ] ) ] ) )

with open( sys.argv[2], 'w+' ) as csv_stream:
	csv_stream.write( ','.join( CSV_ATTRIBUTES ) )
	csv_stream.write( '\n' )
	csv_stream.write( '\n'.join( CSV_SAMPLES ) )

