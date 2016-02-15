
import csv_utilities
from collections import namedtuple

class Data( object ):

	def __init__( self, filename, reader_fun, converter_fun ):
		Row = namedtuple( 'Row', [ 'X', 'Y' ] )
		reader_data 	= converter_fun( reader_fun( filename ) )
		self.attributes = reader_data[ 0 ][ :-1 ] # Remove 'class' attribute
		self.rows  		= [ Row( row[ :-1 ], row[ -1 ] ) for row in reader_data[ 1 ] ] # Named tuple Row( X: row_0, ..., row_n-1, Y: row_n )
		self.attributeCount = len( self.attributes )

	def getRowsTuples( self ):
		return [ ( row[:-1], row[-1] ) for row in self.rows ]

	def getTrueResults( self ):
		return [ row[ -1 ] for row in self.rows ]

	def compareTrueResultsWith( self, results ):
		rows_count = len( results )
		if rows_count != len( self.rows ):
			print( "Error while comparing results." ); return None
		correct_rows_count = 0
		for row in range( rows_count ):
			correct_rows_count += ( 1 if results[ row ] == self.rows[ row ][ -1 ] else 0 )
		return ( correct_rows_count / rows_count ) * 100
