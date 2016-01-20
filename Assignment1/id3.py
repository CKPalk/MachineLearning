
import sys
import math

import CSVReader
import DecisionTree


# GLOBALS

attributes = list()
data = list(list())



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

def findBestAttribute( S, attrs ):
    bestAttributeAndGain = ( 'temp attribute', -1 )
    print( "+--  Gain  ---" )
    for attr in attrs:
        attrGain = Gain( S, attr )
        print( "|", attr, "%0.7f" % ( attrGain ) )
        if attrGain > bestAttributeAndGain[ 1 ]:
            bestAttributeAndGain = ( attr, attrGain )
    print( "+-------------" )
    print( " > Best attribute:", bestAttributeAndGain[0], "\n" )
    return bestAttributeAndGain[ 0 ]

def createNextNode( parent ):

	if len( parent.attributes ) == 0: # No remaining attributes
		return

	falseParentDataSubset = setWithLabel( parent.dataSet, parent.attribute, False )
	falseBestAttribute = findBestAttribute( falseParentDataSubset, parent.attributes )
	parent.newFalsePath( falseBestAttribute, falseParentDataSubset )

	trueParentDataSubset = setWithLabel( parent.dataSet, parent.attribute, True )
	trueBestAttribute = findBestAttribute( trueParentDataSubset, parent.attributes )
	parent.newTruePath( trueBestAttribute, trueParentDataSubset )

	createNextNode( parent.falsePath )
	createNextNode( parent.truePath  )



# ID3
def createDecisionTree():
    tree = DecisionTree.DecisionTree()

    rootAttributes = attributes[:-1]
    bestAttribute = findBestAttribute( data, rootAttributes )
    tree.newRoot( bestAttribute, rootAttributes, data )
    createNextNode( tree.root )

    return tree









# MAIN
def main( argv ):
    if len(argv) != 3:
        return print( "ERROR: Usage \"python3 id3 <train> <test> <model>\"" )

    tup = CSVReader.readBooleanCSV( argv[0] )
    global attributes; attributes  = tup[ 0 ]
    global data      ; data        = tup[ 1 ]


    print( "Attributes:\n", ', '.join( attributes ), "\n" )

    #print( indexOfAttribute( "XD" ) )
    #print( AttributeLabels( data, "XD" ) )

    #for row in setWithLabel( data, "XD", 1 ):
        #print( row )

    #print( resultsOfSet( setWithLabel( data, "XD", 1 ) ) )
    #print( Gain( data, "XF" ) )

    tree = createDecisionTree()
    
    temp = tree.dataSetFromDecisions( { "XD":0, "XE":1, "XF":0 } )
    print( resultsOfSet( temp ) )



if __name__=='__main__':
    main( sys.argv[1:] )
