
import sys
import math

import CSVReader
import DecisionTree


# GLOBALS

attributes = list()
data = list(list())

pre_prune_tree = True


# MATH FUNCTIONS
def Entropy( yesNo ):
	yes = yesNo[0]; no = yesNo[1]
	if no == 0 or yes == 0: return 0
	total = no + yes
	return ( -( yes / total ) * math.log( yes / total, 2 ) 
			- ( no  / total ) * math.log( no  / total, 2 ) )

def Gain( S, Attr ):
	entropy_S = Entropy( resultsOfSet( S ) )
	entropy_sum = 0
	for label in AttributeLabels( S, Attr ):
		subset_S = setWithLabel( S, Attr, label )
		entropy_sum += ( ( len( subset_S ) / len( S ) ) * Entropy( resultsOfSet( subset_S ) ) )
	return entropy_S - entropy_sum




# HELPER
def indexOfAttribute( Attr ):
	return attributes.index( Attr )

def AttributeLabels( S, Attr ):
	index = indexOfAttribute( Attr )
	return list( set( [ row[ index ] for row in S ] ) )

def setWithLabel( S, Attr, Label ):
	return list( filter( lambda row: row[ indexOfAttribute( Attr ) ] == Label, S ) )

def resultsOfSet( S ):
	no = len( list( filter( lambda row: row[-1] is False, S ) ) )
	return ( len( S ) - no, no )

def convertRowToDict( row ):
	return { attributes[ i ] : row[ i ] for i in range( len( row ) ) }

def extractDecisions( S ):
	return [ row[-1] for row in S ]

def compareDecisions( D1, D2 ):
	return sum( [ 1 if D1[i] is D2[i] else 0 for i in range( min( len( D1 ), len( D2 ) ) ) ] ) / min( len( D1 ), len( D2 ) )

def findBestAttribute( S, attrs ):
	bestAttributeAndGain = ( None, -1 ) if not pre_prune_tree else ( None, 0 )
	#print( "+--  Gain  ---" )
	for attr in attrs:
		attrGain = Gain( S, attr )
		#print( "|", attr, "%0.7f" % ( attrGain ) )
		if attrGain > bestAttributeAndGain[ 1 ]:
			bestAttributeAndGain = ( attr, attrGain )
	#print( "+-------------" )
	#print( " > Best attribute:", bestAttributeAndGain[0], "\n" )
	return bestAttributeAndGain[ 0 ]


# Prediction is by higher percentage
def getPrediction( S ):
	res = resultsOfSet( S )
	return True if res[ 0 ] > res[ 1 ] else False

def createNextNodes( parent ):

	if len( parent.attributes ) == 0: # No remaining attributes
		return

	trueParentDataSubset = setWithLabel( parent.dataSet, parent.attribute, True )
	trueBestAttribute = findBestAttribute( trueParentDataSubset, parent.attributes )
	if trueBestAttribute is not None:
		parent.newTruePath( trueBestAttribute, trueParentDataSubset )
		createNextNodes( parent.truePath  )

	falseParentDataSubset = setWithLabel( parent.dataSet, parent.attribute, False )
	falseBestAttribute = findBestAttribute( falseParentDataSubset, parent.attributes )
	if falseBestAttribute is not None:
		parent.newFalsePath( falseBestAttribute, falseParentDataSubset )
		createNextNodes( parent.falsePath )





# ID3
def createDecisionTree( attrs, rows ):

	tree = DecisionTree.DecisionTree( attrs )

	rootAttributes = attrs[:-1]
	bestAttribute = findBestAttribute( rows, rootAttributes )
	
	allSame = True
	outcomes = [ row[-1] for row in rows ]
	for outcome in outcomes:
		if outcome != outcomes[0]: allSame = False; continue

	if allSame:
		tree.newRoot( None, rootAttributes, rows )
	else:
		tree.newRoot( bestAttribute, rootAttributes, rows )
		createNextNodes( tree.root ) # Recursively builds tree

	return tree





# MAIN
def main( argv ):
	if len(argv) != 3:
		return print( "ERROR: Usage \"python3 id3.py <training-set> <test-set> <model-file>\"" )

	training_tup = CSVReader.readBooleanCSV( argv[ 0 ] )
	global attributes; attributes = training_tup[ 0 ]
	global data	  	 ; data		  = training_tup[ 1 ]

	testing_tup = CSVReader.readBooleanCSV( argv[ 1 ] )
	test_attributes = testing_tup[ 0 ]
	test_data		= testing_tup[ 1 ]
	test_decisions  = extractDecisions( test_data )
	
	print( "Attributes" )
	print( ', '.join( attributes ), "\n" )

	tree = createDecisionTree( attributes, data )

	predictions = [ getPrediction( tree.dataSetFromDecisions( convertRowToDict( row ) ) ) for row in test_data ]

	print( "\nPrediction accuracy vs. testing data:", "{}%\n\n".format( 100 * compareDecisions( predictions, test_decisions ) ) )

	tree.printTree( argv[2] )




if __name__=='__main__':
	main( sys.argv[1:] )
