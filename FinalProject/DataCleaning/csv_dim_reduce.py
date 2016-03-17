''' Work of Cameron Palk '''

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main( argv ):
	try:
		csv_in  = argv[ 1 ]
		csv_out = argv[ 2 ]
	except IndexError:
		print( "Error, usage: \"python3 {} <input csv> <output csv>\"".format( argv[ 0 ] ) ) 
		return

	
	df = pd.read_csv( csv_in )
	
	X = df.ix[:,0:-1]
	Y = df.ix[:,-1]

	print( df.shape )
	toDrop = []
	for column in X:
		column_sum = sum( X[ column ] )
		if column_sum < 2:
			toDrop.append( column )

	print( toDrop )

	df.drop( toDrop, inplace=True, axis=1 )

	print( df.shape )

	df.to_csv( csv_out, index=False )

	print( "Csv written to", csv_out )
	




if __name__=='__main__':
	main( sys.argv )
