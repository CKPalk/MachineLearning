
import sys
import csv_data
import my_perceptron


# TWEAKING VARIABLES

max_perceptron_iterations = 100


def printResults( data_name, result_unrounded ):
	print( "RESULTS FOR", data_name.upper() )
	print( "{:.2f}% correct prediction on {}\n".format( round( result_unrounded, 2 ), data_name.lower() ) )



def main( argv ):
	if len( argv ) != 3:
		print( "Usage: \"python3 averagedPerceptron.py <train> <test> <model>\"" ); exit()

	# Read Data
	Training_Data = csv_data.Data( argv[ 0 ] )
	Testing_Data  = csv_data.Data( argv[ 1 ] )

	# Create Perceptron
	perceptron = my_perceptron.Perceptron()
	# He's about to go to school



	perceptron.averagedPerceptronTrain( Training_Data, max_perceptron_iterations )

	print( "\nPredictions results with", max_perceptron_iterations, "iterations of learning the training data:\n" )

	resultsPercentage = perceptron.perceptronPredictionResults( Training_Data )
	printResults( "Training Data", resultsPercentage )

	resultsPercentage = perceptron.perceptronPredictionResults( Testing_Data )
	printResults( "Testing Data", resultsPercentage )

	


	# Shuffle the training data and have the perceptron relearn using the shuffled rows
	Training_Data.shuffleRows()


	perceptron.averagedPerceptronTrain( Training_Data, max_perceptron_iterations )

	print( "\nPredictions results with", max_perceptron_iterations, "iterations of learning the shuffled training data:\n" )

	resultsPercentage = perceptron.perceptronPredictionResults( Training_Data )
	printResults( "Training Data", resultsPercentage )

	resultsPercentage = perceptron.perceptronPredictionResults( Testing_Data )
	printResults( "Testing Data", resultsPercentage )
	



	perceptron.outputModelToFile( argv[ 2 ] )


if __name__=='__main__':
	main( sys.argv[1:] )
