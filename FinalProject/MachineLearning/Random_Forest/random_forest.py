''' Work of Cameron Palk '''

import sys
import os.path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def displayAccuracyGraph( X, Y ):

	# convert Y to perceptage strings
	Y = [ y * 100 for y in Y ]

	plt.plot( X, Y, 'bo' )
	plt.title( 'Random Forest: Accuracy vs. Tree Count' )
	plt.ylabel( 'Accuracy' )
	plt.xlabel( 'Trees in Forest' )
	plt.grid( True )
	plt.show()


def main( argv ):

	try:

		training_filename  	= argv[ 1 ]
		testing_filename 	= argv[ 2 ]
		temp_filename 		= argv[ 3 ]
		output_filename 	= argv[ 4 ]

	except IndexError:
		print( "Error, usage: \"python3 {} <training> <testing> <temp> <output>\"".format( argv[ 0 ] ) ) 
		return


	'''
		Random Forest
	'''
	from sklearn.ensemble import RandomForestClassifier

	# Hyper Parameters
	max_n_estimators = 100 # default 10

	temp_rows = []
	if os.path.isfile( temp_filename ):
		with open( temp_filename, 'r' ) as temp_stream:
			temp_raw = temp_stream.read().strip()
			temp_rows = temp_raw.split( '\n' ) if len( temp_raw ) > 0 else []
		
	tree_accuracies = []
	for row in temp_rows:
		row_split = row.split( ':' )
		tree_accuracies.append( ( int( row_split[0] ), float( row_split[1] ) ) )

	start_idx = len( tree_accuracies ) + 1 # Start where our previous progress ended


	if start_idx < max_n_estimators:
		if start_idx > 1:
			print( "Resuming progress at {:4} trees.".format( start_idx ) )
		else:
			print( "No progress found in temp file, starting with {:4} trees.".format( start_idx ) )

		# Read training data
		Training_DataFrame = pd.read_csv( training_filename )
	
		X = Training_DataFrame.ix[:,0:-1]
		Y = Training_DataFrame.ix[:,-1]

		# Read testing data
		Testing_DataFrame = pd.read_csv( testing_filename )
		
		test_X = Testing_DataFrame.ix[:,0:-1]
		test_Y = Testing_DataFrame.ix[:,-1]
	
		for n_trees in range( start_idx, max_n_estimators + 1 ):
	
			RF_classifier = RandomForestClassifier( 
				n_estimators = n_trees,
				min_samples_split = 10
			)
			RF_classifier.fit( X, Y )
	
			RF_score = RF_classifier.score( test_X, test_Y )
			tree_accuracies.append( ( n_trees, RF_score ) )
	
			# Write progress to file
			with open( temp_filename, 'a' ) as temp_stream_append:
				temp_stream_append.write( "{}:{}\n".format( n_trees, RF_score ) )
	
			print( "Completed {:4} / {} trees : accuracy = {}%".format( n_trees, max_n_estimators, round( RF_score * 100, 3 ) ) )
		
	X_labels = [ label[ 0 ] for label in tree_accuracies ]
	Y_labels = [ label[ 1 ] for label in tree_accuracies ]

	displayAccuracyGraph( X_labels, Y_labels )
#


if __name__=='__main__':
	main( sys.argv )
