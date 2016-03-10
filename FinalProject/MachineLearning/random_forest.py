''' Work of Cameron Palk '''

import sys
import pandas as pd

def main( argv ):
	try:
		training_filename  = argv[ 1 ]
		testing_filename = argv[ 2 ]
		output_filename = argv[ 3 ]
	except IndexError:
		print( "Error, usage: \"python3 {} <training> <testing> <output>\"".format( argv[ 0 ] ) ) 

	
	Training_DataFrame = pd.read_csv( training_filename )
	
	X = Training_DataFrame.ix[:,0:-1]
	Y = Training_DataFrame.ix[:,-1]


	Testing_DataFrame = pd.read_csv( testing_filename )
	
	testing_X = Testing_DataFrame.ix[:,0:-1]
	testing_Y = Testing_DataFrame.ix[:,-1]

	from sklearn.ensemble import RandomForestClassifier
	
	my_n_estimators = 1000 # default 10

	classifier = RandomForestClassifier( n_estimators = my_n_estimators )
	classifier.fit( X, Y )

	predicted_cuisines = classifier.predict( testing_X )

	score = classifier.score( testing_X, testing_Y )

	
	print( "Your mean accuracy:", score )

	#



if __name__=='__main__':
	main( sys.argv )
