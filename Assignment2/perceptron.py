
import sys
import csv_data
import my_perceptron


# TWEAKING VARIABLES

max_perceptron_training_iterations = 100



def main( argv ):
	if len( argv ) != 3:
		print( "Usage: \"python3 perceptron.py <train> <test> <model>\"" ); exit()

	Training_Data = csv_data.Data( argv[ 0 ] )
	# Testing_Data  = csv_data.Data( argv[ 1 ] )

	perceptron = my_perceptron.Perceptron()
	perceptron.perceptronTrain( Training_Data, max_perceptron_training_iterations )
	print( perceptron.perceptronTestResults( Training_Data ) )


if __name__=='__main__':
	main( sys.argv[1:] )
