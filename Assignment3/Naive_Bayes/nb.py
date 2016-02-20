
import sys
from csv_data import Data
from csv_utilities import readIntegerCSV
from csv_utilities import convertToZeroOne
from statistics import mean
from math import log

def dotProduct( arr1, arr2 ):
	return sum( [ arr1[idx] * arr2[idx] for idx in range( len( arr1 ) ) ] )
#
def dataSubsetWithY( data, y ):
	return [ row for row in data.rows if row.Y == y ]
#
def probabilityXisZero( data, idx, beta ):
	return ( 1 - probabilityXisOne( data, idx, beta ) )
#
def probabilityXisOne ( data, idx, beta ):
	return ( mean( ( [ 1, 0 ] * ( beta - 1 ) ) + [ row.X[ idx ] for row in data ] ) )
#
def probabilityXY( data, x, idx, y, beta ):
	return ( probabilityXisOne( dataSubsetWithY( data, y ), idx, beta ) if x == 1 else probabilityXisZero( dataSubsetWithY( data, y ), idx, beta ) )
#
def probabilityYisZero( data, beta ):
	return ( 1 - probabilityYisOne( data, beta ) )
#
def probabilityYisOne ( data, beta ):
	return ( mean( ( [ 1, 0 ] * ( beta - 1 ) ) + [ row.Y for row in data.rows ] ) )
#
def findBias( data, beta ):
	return ( log( probabilityYisZero( data, beta ) / probabilityYisOne( data, beta ), 2 ) 
			+ sum( [ log( probabilityXY( data, 0, idx, 1, beta ) / probabilityXY( data, 0, idx, 0, beta ), 2 ) for idx in range( data.attributeCount ) ] ) )
#
def findWeights( data, beta ):
	return ( [ log( probabilityXY( data, 1, idx, 1, beta ) / probabilityXY( data, 1, idx, 0, beta ), 2 ) 
			 - log( probabilityXY( data, 0, idx, 1, beta ) / probabilityXY( data, 0, idx, 0, beta ), 2 ) for idx in range( data.attributeCount ) ] )
#
def rowPrediction( X, W, b ):
	return ( 1 if ( dotProduct( X, W ) + b >= 0 ) else 0 )
#
def getResults( testing_data, W, b ):
	return ( len( [ 1 for row in testing_data.rows if row.Y == rowPrediction( row.X, W, b ) ] ) / len( testing_data.rows ) )
#
def printModel( model_stream, attrs, W, b ):
	model_stream.write( "{}\n".format( round( b, 4 ) ) )
	for idx, attr in enumerate( attrs ):
		model_stream.write( "{:16}\t{}\n".format( attr, round( W[ idx ], 4 ) ) )


def main( argv ):
	try:
		training_data 	= Data( argv[ 0 ], readIntegerCSV, convertToZeroOne )
		testing_data  	= Data( argv[ 1 ], readIntegerCSV, convertToZeroOne )
		beta 			= int ( argv[ 2 ] )
		model			= open( argv[ 3 ], 'w+' )

		b = findBias( training_data, beta )
		W = findWeights( training_data, beta )

		rez = getResults( testing_data, W, b )
		print( rez )

		printModel( model, training_data.attributes, W, b )

	except IndexError:
		print( "ERROR: \"python3 nb.py <train> <test> <beta> <model>\"" )
	finally:
		model.close()
#

if __name__=='__main__':
	main( sys.argv[ 1: ] )
