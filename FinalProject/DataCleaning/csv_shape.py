''' Work of Cameron Palk '''

import sys
import pandas as pd

def main( argv ):
	try:
		csv_data = pd.read_csv( argv[ 1 ] )

		print( csv_data.shape )

	except IndexError:
		print( "Error, usage: \"python3 data_analysis.py <csv>\"" ) 
	return

if __name__=='__main__':
	main( sys.argv )
