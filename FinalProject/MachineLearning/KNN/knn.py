''' Work of Cameron Palk '''

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def main( argv ):
	try:
		training_filename  = argv[ 1 ]
		testing_filename = argv[ 2 ]
		output_filename = argv[ 3 ]
	except IndexError:
		print( "Error, usage: \"python3 {} <training> <testing> <output>\"".format( argv[ 0 ] ) ) 
		return

	
	Training_DataFrame = pd.read_csv( training_filename )
	
	X = Training_DataFrame.ix[:,0:-1]
	Y = Training_DataFrame.ix[:,-1]


	Testing_DataFrame = pd.read_csv( testing_filename )
	
	test_X = Testing_DataFrame.ix[:,0:-1]
	test_Y = Testing_DataFrame.ix[:,-1]


	'''
		Perceptron
	'''
	from sklearn.neighbors import KNeighborsClassifier

	# Hyper Parameters:
	n_neighbors = 5

	# Fit Classifier
	KNN_classifier = KNeighborsClassifier( 
		n_neighbors = n_neighbors
	)

	print( "{} Started training".format( str( datetime.now() ) ) )
	KNN_classifier.fit( X, Y )
	print( "{} Stopped training".format( str( datetime.now() ) ) )

	# Report results
	print( "{} Started testing".format( str( datetime.now() ) ) )
	score = KNN_classifier.score( test_X, test_Y )
	print( "{} Stopped testing".format( str( datetime.now() ) ) )

	print( "\nK-NN with {} cluster has Accuracy: {}%".format( n_neighbors, round( score * 100, 3 ) ) )
	#



if __name__=='__main__':
	main( sys.argv )
