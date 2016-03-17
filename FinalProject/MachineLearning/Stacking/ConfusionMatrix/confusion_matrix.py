''' Work of Cameron Palk '''

import sys
import pandas as pd


def getDifferenceMatrix( csv ):

	df = pd.read_csv( csv )

	all_labels = sorted(df.Label.unique())

	RF_matrix = { label: [0 for _ in all_labels] for label in all_labels }
	P_matrix = { label: [0 for _ in all_labels] for label in all_labels }
	KNN_matrix = { label: [0 for _ in all_labels] for label in all_labels }

	for idx, row in df.iterrows():
		real_idx 		= row.Label

		RF_pred_idx 	= all_labels.index( row.Random_Forest )
		P_pred_idx 		= all_labels.index( row.Perceptron )
		KNN_pred_idx 	= all_labels.index( row.KNN )

		RF_matrix [ real_idx ][ RF_pred_idx  ] += 1
		P_matrix  [ real_idx ][ P_pred_idx   ] += 1
		KNN_matrix[ real_idx ][ KNN_pred_idx ] += 1

	return ({ 'Random_Forest':RF_matrix,
			 'Perceptron':P_matrix,
			 'KNN':KNN_matrix }, all_labels )

#


def main( argv ):
	try:
		csv = argv[ 1 ]
	except IndexError:
		print( "Error ** Usage: \"python3 {} <csv>\"".format( argv[ 0 ] ) ) 
	#

	differenceMatrix = getDifferenceMatrix( csv )

	for name, matrix in differenceMatrix[0].items():
		print( "\nConfusion Matrix for", name )
		df = pd.DataFrame( matrix, index=differenceMatrix[1] )
		df.to_csv( "{}_confusion_matrix.csv".format( name ) )
		print( "Saved confusion matrix for", name )
		
		'''
		s = [[str(e) for e in row] for row in matrix]
		lens = [max(map(len, col))-1 for col in zip(*s)]
		fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
		table = [fmt.format(*row) for row in s]
		print( '\n'.join(table) )
		'''


	print( "\nDone.\n" )
#


if __name__=='__main__':
	main( sys.argv )
#
