''' Work of Cameron Palk '''

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

classes = [
		'NONE',
		'SOUTHERN_US', 
		'FILIPINO', 
		'INDIAN', 
		'ITALIAN', 
		'MEXICAN', 
		'CHINESE', 
		'BRITISH', 
		'THAI', 
		'VIETNAMESE', 
		'CAJUN_CREOLE', 
		'BRAZILIAN', 
		'FRENCH',
		'JAPANESE', 
		'JAMAICAN', 
		'IRISH', 
		'KOREAN', 
		'SPANISH', 
		'MOROCCAN', 
		'RUSSIAN',
		'GREEK'
]

def printAccuracy( c_name, acc ):
	print( "\t{:20} Accuracy: {}".format( c_name, toPercent( acc ) ) )

def toPercent( x, decimals=2 ):
	return "{}%".format( round( x * 100, decimals ) )

def num_to_str( x ):
	return classes[ x ]

def str_to_num( x ):
	return classes.index( x )

def getColumnAccuracy( X, Y ):
	correct = 0
	incorrect = 0
	total = len( Y )
	for idx in range( total ):
		if X[ idx ] == Y[ idx ]:
			correct += 1
		else:
			incorrect += 1
	return ( correct/total, correct, incorrect )

def print_individual_classifier_accuracies( df ):
	print( "\nClassifier Accuracies: " )
	X = df.ix[:,0:-1]
	Y = df.ix[:,-1]
	for column in X.columns:
		accuracy_stats = getColumnAccuracy( X[ column ], Y )
		printAccuracy( column, accuracy_stats[0] )




def main( argv ):
	try:
		input_csv  = argv[ 1 ]
		output_model = argv[ 2 ]
	except IndexError:
		print( "Error, usage: \"python3 {} <input_csv> <output_csv>\"".format( argv[ 0 ] ) ) 
		return

	
	df = pd.read_csv( input_csv )

	convert_to_num = True

	print_individual_classifier_accuracies( df )


	# Split data into test and train
	msk = np.random.rand( len( df ) ) < 0.8

	Training_DataFrame = df[ msk ].copy()
	if convert_to_num:
		X = Training_DataFrame.ix[:,0:-1].applymap( str_to_num )
		Y = Training_DataFrame.ix[:,-1].map( str_to_num )
	else:
		X = Training_DataFrame.ix[:,0:-1]
		Y = Training_DataFrame.ix[:,-1]


	Testing_DataFrame = df[ ~msk ].copy()
	if convert_to_num:
		testing_X = Testing_DataFrame.ix[:,0:-1].applymap( str_to_num )
		testing_Y = Testing_DataFrame.ix[:,-1].map( str_to_num )
	else:
		testing_X = Testing_DataFrame.ix[:,0:-1]
		testing_Y = Testing_DataFrame.ix[:,-1]

	print( "\nTraining on Classifier Predictions:" )


	''' LINEAR CLASSIFIERS '''
	print( "Linear Classifiers\n" )


	''' Logistic Regression '''
	from sklearn.linear_model import LogisticRegression

	# Hyper Parameters:
	tol = 0.0001

	# Fit Classifier
	LR_classifier = LogisticRegression( )
	LR_classifier.fit( X, Y )

	# Report results
	LR_score = LR_classifier.score( testing_X, testing_Y )

	printAccuracy( "Logistic Regression", LR_score )
	#

	''' Perceptron '''
	from sklearn.linear_model import Perceptron

	# Hyper Parameters:

	# Fit Classifier
	P_classifier = Perceptron( )
	P_classifier.fit( X, Y )

	# Report results
	P_score = P_classifier.score( testing_X, testing_Y )

	printAccuracy( "Perceptron", P_score )
	#

	''' Gaussian Naive Bayes '''
	from sklearn.naive_bayes import GaussianNB

	# Hyper Parameters

	# Fit Classifier
	MNB_classifier = GaussianNB( )
	MNB_classifier.fit( X, Y )

	# Report results
	MNB_score = MNB_classifier.score( testing_X, testing_Y )
	
	printAccuracy( "Gaussian Naive Bayes", MNB_score )
	#

	''' Linear Support Vector Machine ( SVM ) '''
	from sklearn.svm import LinearSVC

	# Hyper Parameters

	# Fit Classifier
	LSVC_classifier = LinearSVC( )
	LSVC_classifier.fit( X, Y )

	# Report results
	LSVC_score = LSVC_classifier.score( testing_X, testing_Y )
	
	printAccuracy( "Linear SVM", LSVC_score )
	#



	''' NONLINEAR ALGOS '''
	print( "\nNonlinear Classifiers\n" )

	''' Decision Tree '''
	from sklearn.tree import DecisionTreeClassifier

	# Hyper Parameters

	# Fit Classifier
	DT_classifier = DecisionTreeClassifier( )
	DT_classifier.fit( X, Y )

	# Report results
	DT_score = DT_classifier.score( testing_X, testing_Y )
	
	printAccuracy( "Decision Tree", DT_score )
	#

	''' Random Forest '''
	from sklearn.ensemble import RandomForestClassifier

	# Hyper Parameters
	n_estimators = 22

	# Fit Classifier
	RF_classifier = RandomForestClassifier( 
		n_estimators=n_estimators 
	)
	RF_classifier.fit( X, Y )

	# Report results
	RF_score = RF_classifier.score( testing_X, testing_Y )
	
	printAccuracy( "Random Forest", RF_score )
	#

	''' KNN '''
	from sklearn.neighbors import KNeighborsClassifier

	# Hyper Parameters
	n_neighbors = 20

	# Fit Classifier
	KNN_classifier = KNeighborsClassifier( )
	KNN_classifier.fit( X, Y )

	# Report results
	KNN_score = KNN_classifier.score( testing_X, testing_Y )
	
	printAccuracy( "KNN", KNN_score )
	#


	''' VOTING '''
	print( "\nMajority Vote Classifier\n" )

	V_correct = 0
	V_incorrect = 0
	V_total = len( testing_X )

	for idx, row in testing_X.iterrows():
		prediction = Counter( row ).most_common()[0][0]
		if testing_Y[ idx ] == prediction:
			V_correct += 1
		else:
			V_incorrect += 1

	printAccuracy( "Voting", V_correct / V_total )


	print( "\n\nDone." )





if __name__=='__main__':
	main( sys.argv )
