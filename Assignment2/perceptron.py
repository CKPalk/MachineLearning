
import sys
import csv_data
import my_perceptron


# TWEAKING VARIABLES

max_perceptron_training_iterations = 50
max_perceptron_testing_iterations  = 50


def printResults( data_name, result_unrounded ):
	print( "RESULTS FOR", data_name.upper() )
	print( "{:.2f}% correct prediction compared to given results".format( round( result_unrounded, 2 ) ) )



def main( argv ):
	if len( argv ) != 3:
		print( "Usage: \"python3 perceptron.py <train> <test> <model>\"" ); exit()

	# Read Data
	Training_Data = csv_data.Data( argv[ 0 ] )
	Testing_Data  = csv_data.Data( argv[ 1 ] )

	# Create Perceptron
	perceptron = my_perceptron.Perceptron()

	# Train Perceptron from Training Data
	perceptron.perceptronTrain( Training_Data, max_perceptron_training_iterations )

	# Use perceptron to predict results
	resultsPercentage = perceptron.perceptronPredictionResults( Training_Data )
	printResults( "Training Data", resultsPercentage )

	resultsPercentage = perceptron.perceptronPredictionResults( Testing_Data )
	printResults( "Testing Data", resultsPercentage )
	
	perceptron.outputModelToFile( argv[ 2 ] )


if __name__=='__main__':
	main( sys.argv[1:] )
