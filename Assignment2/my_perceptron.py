

class Perceptron( object ):

	def __init__( self ):
		self.w = None
		self.D = 0
		self.b = 0
		self.attrs = None

	# Algorithm Body:
	def perceptronTrain( self, Data, MaxIter ):
		self.w = [ 0 for _ in Data.attributes ]
		self.D = len( self.w )
		self.attrs = Data.attributes
		self.b = 0
		for i in range( MaxIter ):
			for x, y in Data.getRowsTuples():
				a = self.activation( x )
				if ( y * a ) <= 0:
					self.w = [ self.w[d] + ( y * x[d] ) for d in range( self.D ) ]
					self.b += y
					#print( "Updated weights:", self.w, "bias:", self.b )
			print( "Finished iteration", i )


	def perceptronTest( self, row ):
		a = self.activation( row )
		return self.sign( a )

	def perceptronPredictionResults( self, Data ):
		if self.w is None:
			print( "Perceptron must be trained first with .perceptronTrain( Data, MaxIter )" )
			return 0
		perceptron_results = [ self.perceptronTest( row ) for row in Data.rows ]
		return Data.compareTrueResultsWith( perceptron_results )

	def activation( self, row ):
		activation = 0
		for d in range( self.D ):
			activation += ( self.w[d] * row[d] )
		return activation + self.b

	
	# Support Methods: 
	def sign( self, a ):
		return 1 if a > 0 else -1

	def outputModelToFile( self, filename ):
		with open( filename, 'w+' ) as model_file:
			model_file.write( str(self.b) )
			for d in range( self.D ):
				model_file.write( str( self.attrs[d] ) + " " + str( self.w[d] ) + "\n" )
