


class Node( object ):
	def __init__( self, attr, attrs, dataSet ):
		self.falsePath  = None	  # Destination Node for False
		self.truePath   = None	  # Destination Node for True
		self.attribute  = attr	  # Name of Attribute
		self.attributes = attrs	  # Remaining possible attributes
		self.dataSet	= dataSet # Subset of data from previous decision


	def nextNode( self, testPassed ):
		return self.truePath if testPassed else self.falsePath

	def newFalsePath( self, attr, dataSubset ): 
		falsePathAttributes = self.attributes[:] 
		falsePathAttributes.remove( attr ) 
		#print( "New False Path:", falsePathAttributes ) 
		self.falsePath = Node( attr, falsePathAttributes, dataSubset )

	def newTruePath( self, attr, dataSubset ):
		truePathAttributes = self.attributes[:]
		truePathAttributes.remove( attr )
		#print( "New True Path:", truePathAttributes )
		self.truePath  = Node( attr, truePathAttributes, dataSubset )

	def subsetWithLabel( self, attr_index, label ):
		return list( filter( lambda row: row[ attr_index ] == label, self.dataSet ) )

	def resultsOfSet( self, S ):
		no = len( list( filter( lambda row: row[-1] is False, S ) ) )
		return ( len( S ) - no, no )

	def makePrediction( self, indexOfAttr, pathBool ):
		subset = self.subsetWithLabel( indexOfAttr, pathBool )
		ratio = self.resultsOfSet( subset )
		return ratio[0] > ratio[1] # Trues > Falses



class DecisionTree( object ):

	def __init__( self, attrs ):
		self.root = None
		self.attributes = attrs
		return
   
	def newRoot( self, attr, attrs, data ):
		self.root = Node( attr, attrs, data )
		return

	def getRoot( self ):
		return self.root

	def printNode( self, node, depth, pathBool, output_file ):
		output = "| " * depth + node.attribute + " = " + ("1" if pathBool else "0") +  " : "
		if pathBool: 
			output += ( "1\n" if node.makePrediction( self.attributes.index( node.attribute ), True  ) else "0\n" if node.truePath  is None else "\n" )
		else: 
			output += ( "1\n" if node.makePrediction( self.attributes.index( node.attribute ), False ) else "0\n" if node.falsePath is None else "\n" )
		output_file.write( output )

	def preorderTraversal( self, node, depth, output_file ):
		if node is None: return
		self.printNode( node, depth, False, output_file )
		self.preorderTraversal( node.falsePath, depth + 1, output_file )
		self.printNode( node, depth, True,  output_file )
		self.preorderTraversal( node.truePath , depth + 1, output_file )

	def printTree( self, filename ):
		with open( filename, 'w+' ) as output_file:
			self.preorderTraversal( self.root, 0, output_file )

	def dataSetFromDecisions( self, decisionDict ):
		node = self.root
		nextNode = node.nextNode( decisionDict[ node.attribute ] )
		while nextNode is not None:
			node = nextNode
			nextNode = node.nextNode( decisionDict[ node.attribute ] )
		return node.dataSet

	def indexOfAttribute( attr ):
		return self.attributes.index( attr )





































































