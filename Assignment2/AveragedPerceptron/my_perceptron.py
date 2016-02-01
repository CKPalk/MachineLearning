

class Perceptron( object ):

	def __init__( self ):
		self.w = None
		self.u = None
		self.D = 0
		self.b = 0
		self.B = 0
		self.attrs = None

	# Algorithm Body:
	def averagedPerceptronTrain( self, Data, MaxIter ):
		self.w = [ 0 for _ in Data.attributes ]
		self.u = [ 0 for _ in Data.attributes ]
		self.D = len( self.w )
		self.attrs = Data.attributes
		self.b = 0
		self.B = 0
		c = 1
		for _ in range( MaxIter ):
			for x, y in Data.getRowsTuples():
				a = self.activation( x )
				if ( y * a ) <= 0:
					self.w = [ self.w[d] + ( y * x[d] ) for d in range( self.D ) ]
					self.b += y
					self.u = [ self.u[d] + ( y * c * x[d] ) for d in range( self.D ) ]
					self.B += y * c
				c += 1
		self.w = [ self.w[d] - ( self.u[d] / c ) for d in range( self.D ) ]
		self.b -= self.B / c


	def perceptronTest( self, row ):
		a = self.activation( row )
		return self.sign( a )


	def perceptronPredictions( self, Data ):
		if self.w is None:
			print( "Perceptron must be trained first with .perceptronTrain( Data, MaxIter )" )
			return
		return [ self.perceptronTest( row ) for row in Data.rows ]


	def perceptronPredictionResults( self, Data ):
		return Data.compareTrueResultsWith( self.perceptronPredictions( Data ) )


	def perceptronPredictionResultsAndPrintActivations( self, Data ):
		perceptronPredictions = self.perceptronPredictions( Data )
		for i in range( len( perceptronPredictions ) ):
			print( "Row", i, "returned:", self.forceOneOrZero( perceptronPredictions[ i ] ) )
		return Data.compareTrueResultsWith( perceptronPredictions )


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
			model_file.write( str(self.b) + "\n" )
			for d in range( self.D ):
				model_file.write( str( self.attrs[d] ) + " " + str( self.w[d] ) + "\n" )
