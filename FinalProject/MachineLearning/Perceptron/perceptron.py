''' Work of Cameron Palk '''

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
	
	testing_X = Testing_DataFrame.ix[:,0:-1]
	testing_Y = Testing_DataFrame.ix[:,-1]


	'''
		Perceptron
	'''
	from sklearn.linear_model import Perceptron

	# Hyper Parameters:
	alpha 	= 0.0001
	n_iter 	= 20

	# Fit Classifier
	P_classifier = Perceptron( alpha = alpha, n_iter = n_iter )
	P_classifier.fit( X, Y )

	# Report results
	P_score = P_classifier.score( testing_X, testing_Y )

	print( "\nPerceptron Accuracy:", P_score )
	#



if __name__=='__main__':
	main( sys.argv )
