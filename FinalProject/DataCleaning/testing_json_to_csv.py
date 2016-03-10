''' Work of Cameron Palk '''

import sys
import pandas as pd
import json
import numpy as np

def main( argv ):
	try:
		json_str = open( argv[ 1 ], 'r' ).read().upper()
		testing_json = json.loads( json_str )

		training_df = pd.read_csv( argv[ 2 ] )

		ingredient_attrs = training_df.columns.values[:-1]

		ingr_attr = "INGREDIENTS"
		TESTING_SAMPLES = []
		for recipe in testing_json:
			ingredient_words = ' '.join( recipe[ ingr_attr ] ).split( ' ' )
			TESTING_SAMPLES.append( 
				','.join( [ "1" if ingredient in ingredient_words else "0" for ingredient in ingredient_attrs ] + [ str( recipe[ "CUISINE" ] ) ] ) 
			)

		with open( argv[ 3 ], 'w+' ) as testing_stream:
			testing_stream.write( ','.join( training_df.columns.values ) )
			testing_stream.write( '\n' )
			testing_stream.write( '\n'.join( TESTING_SAMPLES ) )

	except IndexError:
		print( "Error, usage: \"python3 {} <testing_json> <training_csv> <output_csv>\"".format( argv[ 0 ] ) ) 
	return

if __name__=='__main__':
	main( sys.argv )
