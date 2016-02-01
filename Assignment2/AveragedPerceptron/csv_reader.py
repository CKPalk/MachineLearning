import sys

def readStringCSV( filename ):
	data = readCSV( filename )
	attributes = data[0].split(',')
	relations = [ line.split(',') for line in data[1:] ]
	return ( attributes, relations )

def readBooleanCSV( filename ):
	data = readCSV( filename )
	attributes = data[0].split(',')
	relations = [ [ True if elem is '1' else False for elem in line.split(',') ] for line in data[1:] ]
	return ( attributes, relations )

def readIntegerCSV( filename ):
	data = readCSV( filename )
	attributes = data[0].split(',')
	relations = [ [ 1 if elem is '1' else 0 for elem in line.split(',') ] for line in data[1:] ]
	return( attributes, relations )

def convertToPosNegOne( data ):
	return( data[0], [ [ 1 if elem is 1 else -1 for elem in row ] for row in data[1] ] )

def readCSV( filename ):
	data = None
	with open( filename, 'r' ) as file_data:
		data = file_data.read().split()
	return data
		

