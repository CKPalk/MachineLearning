
class Node( object ):
    def __init__( self, attr, attrs, dataSet ):
        self.falsePath  = None      # Destination Node for False
        self.truePath   = None      # Destination Node for True
        self.attribute  = attr      # Name of Attribute
        self.attributes = attrs     # Remaining possible attributes
        self.dataSet    = dataSet   # Subset of data from previous decision

    def nextNode( self, testPassed ):
        return self.truePath if testPassed else self.falsePath

    def newFalsePath( self, attr, dataSubset ):
        falsePathAttributes = self.attributes
        falsePathAttributes.remove( attr )
        print( "New False Path:", self.attributes )
        self.falsePath = Node( attr, falsePathAttributes, dataSubset )

    def newTruePath ( self, attr, dataSubset ):
        truePathAttributes = self.attributes
        truePathAttributes.remove( attr )
        print( "New True Path:", truePathAttributes )
        self.truePath  = Node( attr, truePathAttributes, dataSubset )




class DecisionTree( object ):

    def __init__( self ):
        self.root = None
        return
   
    def newRoot( self, attr, attrs, data ):
        self.root = Node( attr, attrs, data )
        return

    def getRoot( self ):
        return self.root

    def dataSetFromDecisions( self, decisionDict ):
        node = self.root
        nextNode = node.nextNode( decisionDict[ node.attribute ] )
        while nextNode is not None:
            node = nextNode
            nextNode = node.nextNode( decisionDict[ node.attribute ] )
        return node.dataSet
