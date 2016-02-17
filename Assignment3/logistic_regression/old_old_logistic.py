
import sys
import csv_data
import csv_reader
import math



def upsidedownDeltaL( Data, weights, bias, sigma ):
	gradient = [ 0 ] * Data.attributeCount()
	lamb = 1 / ( 2 * pow( sigma, 2 ) )
	for col in range( Data.attributeCount() ):
		s = 0
		for row in Data.rows:
			prediction = sum( [ weights[ c ] * row[ c ] for c in range( Data.attributeCount() ) ] ) + bias
			print( -1 * row[-1] * prediction )
			math.exp( -1 * row[-1] * prediction )
			s += row[-1] * row[col] * math.exp( -1 * row[-1] * prediction ) + ( lamb * weights[ col ] )
		gradient[ col ] = -1 * s
	print( gradient )
	return gradient
	return [ -1 * sum( [ row[ -1 ] * row[ c ] * math.exp( -1 * row[ -1 ] * ( weights[ c ] * row[ c ] + bias ) ) for row in Data.rows ] ) + ( ( 1 / ( 2 * pow( sigma, 2 ) ) ) * weights[ c ] ) for c in range( Data.attributeCount() ) ]


def gradientDescent( Data, MaxIters, LearningRate, sigma ):
	weights = [ 0 ] * Data.attributeCount()
	bias 	= 0
	for iteration in range( MaxIters ):
		gradient = upsidedownDeltaL( Data, weights, bias, sigma )
		weights = [ weights[ col ] - ( LearningRate * gradient[ col ] ) for col in range( len( weights ) ) ]
	return weights



def main( argv ):
	if len( argv ) != 5:
		print( "ERROR: \"python3 logisitic.py <train> <test> <eta> <sigma> <model>\"" ); return
	
	Data = csv_data.Data( argv[0], csv_reader.readIntegerCSV, csv_reader.convertToPosNegOne )

	print( gradientDescent( Data, 100, float( argv[2] ), float( argv[3] ) ) )

	

if __name__=='__main__':
	main( sys.argv[ 1: ] )




'''
def createRegularizedObjective( loss_fun, regularizer_fun ):
	def newRegularizedObjective( Data, weights, bias ):
		return
	return newRegularizedObjective
'''

'''
gradient = [ 0 ] * Data.attributeCount()
lamb = 1 / ( 2 * pow( sigma, 2 ) )
for col in range( Data.attributeCount() ):
	s = 0
	for row in Data.rows:
		prediction = sum( [ weights[ c ] * row[ c ] for c in range( Data.attributeCount() ) ] ) + bias
		s += row[-1] * row[col] * math.exp( -1 * row[-1] * prediction ) + ( lamb * weights[ col ] )
	gradient[ col ] = -1 * s
return gradient
'''
