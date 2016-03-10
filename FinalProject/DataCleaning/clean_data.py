import sys
import json
from difflib import SequenceMatcher


json_str = open( 'train.json', 'r' ).read().upper()
python_recipes = json.loads( json_str )

ingredients = []
for recipe in python_recipes:
	for ingredient in recipe["INGREDIENTS"]:
		ingredient = ingredient.replace( ',', '' )
		if ingredient not in ingredients:
			ingredients.append( ingredient )

similar_count = 0

for row in  sorted( [ list( set ( ingr.split() ) ) for ingr in ingredients ] ):
	print( row )
#print( "{:20}  <->  {:20}  :  {}%".format( ingr_1, ingr_2, round( ingr_match * 100, 3 ) ) )
print( similar_count )
