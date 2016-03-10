import json

json_str = open( 'train.json', 'r' ).read().upper()
python_recipes = json.loads( json_str )

attrs = []
for recipe in python_recipes:
	for ingredient in recipe["INGREDIENTS"]:
		ingredient = ingredient.replace( ',', '' )
		if ingredient not in attrs:
			attrs.append( ingredient )
attrs.append( "CUISINE" )

rows = []
for recipe in python_recipes:
	rows.append( ','.join( [ "1" if ingredient in recipe["INGREDIENTS"] else "0" for ingredient in attrs[:-1] ] + [ str(recipe["CUISINE"]) ] ) )

with open( 'train.csv', 'w+' ) as csv_stream:
	csv_stream.write( ','.join( attrs ) )
	csv_stream.write( '\n' )
	csv_stream.write( '\n'.join( rows ) )

