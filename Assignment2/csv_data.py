
import csv_reader

class Data( object ):

	attributes = None
	rows 	   = None

	def __init__( self, filename ):
		reader_data 	= csv_reader.convertToPosNegOne( csv_reader.readIntegerCSV( filename ) )
		self.attributes = reader_data[ 0 ][:-1] # Remove 'class' attribute
		self.rows  		= reader_data[ 1 ]		# All rows in a [[]]

	def getRowsTuples( self ):
		return [ ( row[:-1], row[-1] ) for row in self.rows ]

	def compareTrueResultsWith( self, results ):
		rows_count = len( results )
		if rows_count != len( self.rows ):
			print( "Error while comparing results." ); return None
		correct_rows_count = 0
		for row in range( rows_count ):
			correct_rows_count += 1 if results[ row ] is self.rows[ row ] else 0
		return ( correct_rows_count / rows_count ) * 100
