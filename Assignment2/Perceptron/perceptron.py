
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
		print( "Usage: \"python3 perceptron.py <train> <test> <model>\"" ); exit()

	# Read Data
	Training_Data = csv_data.Data( argv[ 0 ] )
	Testing_Data  = csv_data.Data( argv[ 1 ] )

	# Create Perceptron
	perceptron = my_perceptron.Perceptron()

	print( "\n\nPredictions results with", max_perceptron_iterations, "iterations of learning:\n" )
	perceptron.perceptronTrain( Training_Data, max_perceptron_iterations )

	resultsPercentage = perceptron.perceptronPredictionResults( Training_Data )
	printResults( "Training Data", resultsPercentage )

	resultsPercentage = perceptron.perceptronPredictionResultsAndPrintActivations( Testing_Data )
	printResults( "Testing Data", resultsPercentage )

	perceptron.outputModelToFile( argv[ 2 ] )
	print( "Weights and bias recorded for", max_perceptron_iterations, "iterations in", argv[ 2 ], "\n" );



	print( "\n\nAlso predictiong results with 50 iterations of learning because I get better percentages:\n" )
	perceptron.perceptronTrain( Training_Data, 50 )

	resultsPercentage = perceptron.perceptronPredictionResults( Training_Data )
	printResults( "Training Data", resultsPercentage )

	resultsPercentage = perceptron.perceptronPredictionResults( Testing_Data )
	printResults( "Testing Data", resultsPercentage )

	print( "Weights and bias of output file will still reflect the", max_perceptron_iterations, "iteration test above.\n\n" )




if __name__=='__main__':
	main( sys.argv[1:] )
