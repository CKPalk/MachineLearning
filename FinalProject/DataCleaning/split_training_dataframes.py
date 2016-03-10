
import pandas
import sys

def splitDataFrame( dataFrame, split=0.3 ):
	print(len( dataFrame ))

def main( argv ):
	df = pandas.read_csv( argv[ 1 ] )
	split_dfs = splitDataFrame( df )
	print( split_dfs )

if __name__=='__main__':
	main( sys.argv )
