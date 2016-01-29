

class Perceptron( object ):

	def __init__( self ):
		self.w = None
		self.D = 0
		self.b = 0

	# Algorithm Body:
	def perceptronTrain( self, Data, MaxIter ):
		self.w = [ 0 for _ in Data.attributes ]
		self.D = len( self.w )
		self.b = 0
		for i in range( MaxIter ):
			for x, y in Data.getRowsTuples():
				a = self.activation( x )
				if ( y * a ) <= 0:
					self.w = [ self.w[d] + ( y * x[d] ) for d in range( self.D ) ]
					self.b += y
			print( "Finished iteration", i )


	def perceptronTest( self, row ):
		a = self.activation( row )
		return self.sign( a )

	def perceptronTestResults( self, Data ):
		if self.w is None:
			print( "Perceptron must be trained first with .perceptronTrain( Data, MaxIter )" ); return 0
		perceptron_results = [ self.perceptronTest( row ) for row in Data.rows ]
		print( perceptron_results )
		return Data.compareTrueResultsWith( perceptron_results )

	def activation( self, row ):
		activation = 0
		for d in range( self.D ):
			activation += ( self.w[d] * row[d] )
		return activation + self.b

	
	# Support Methods: 
	def sign( self, a ):
		return 1 if a > 0 else 0
	
