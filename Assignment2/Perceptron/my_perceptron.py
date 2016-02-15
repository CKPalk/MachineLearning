
import random


class Perceptron( object ):

	randomize_w_and_b = False

	def __init__( self ):
		self.w = None
		self.D = 0
		self.b = 0
		self.attrs = None

	# Algorithm Body:
	def perceptronTrain( self, Data, MaxIter ):
		self.w = [ random.uniform( -1, 1 ) if self.randomize_w_and_b else 0 for _ in Data.attributes ]
		self.D = len( self.w )
		self.attrs = Data.attributes
		self.b = random.uniform( -1, 1 ) if self.randomize_w_and_b else 0
		for i in range( MaxIter ):
			changed = False
			for x, y in Data.getRowsTuples():
				a = self.activation( x )
				if ( y * a ) <= 0:
					changed = True
					self.w = [ self.w[d] + ( y * x[d] ) for d in range( self.D ) ]
					self.b += y
			if not changed:
				print( "Nothing changed on this pass, breaking out at", i, "iterations." )
				return


	def perceptronTest( self, row ):
		a = self.activation( row )
		return self.sign( a )

	def perceptronTestAndPrint( self, row ):
		a = self.activation( row )
		print( a )
		return self.sign( a )


	def perceptronPredictions( self, Data, printBool ):
		if self.w is None:
			print( "Perceptron must be trained first with .perceptronTrain( Data, MaxIter )" )
			return
		if printBool:
			return [ self.perceptronTestAndPrint( row ) for row in Data.rows ]
		else:
			return [ self.perceptronTest( row ) for row in Data.rows ]


	def perceptronPredictionResults( self, Data ):
		return Data.compareTrueResultsWith( self.perceptronPredictions( Data, False ) )


	def perceptronPredictionResultsAndPrintActivations( self, Data ):
		return Data.compareTrueResultsWith( self.perceptronPredictions( Data, True ) )


	def activation( self, row ):
		activation = 0
		for d in range( self.D ):
			activation += ( self.w[d] * row[d] )
		return activation + self.b

	
	# Support Methods: 
	
	def predictionFromRow( self, row ):
		return 1 if self.perceptronTest( row ) == 1 else 0

	def sign( self, a ):
		return 1 if a > 0 else -1

	def forceOneOrZero( self, result ):
		return 1 if result == 1 else 0

	def outputModelToFile( self, filename ):
		with open( filename, 'w+' ) as model_file:
			model_file.write( str( round( self.b, 2 ) ) + "\n" )
			for d in range( self.D ):
				model_file.write( str( self.attrs[d] ) + " " + str( round( self.w[d], 5 ) ) + "\n" )
