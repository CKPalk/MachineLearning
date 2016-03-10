import sys
import os.path

def fileToUpper( argv ):

	input_filename  = argv[ 1 ]
	output_filename = argv[ 2 ]

	try:
		input_stream  = open( argv[ 1 ], 'r' )

		if os.path.isfile( output_filename ):

			while( True ): # Ask until you get a reasonable response
				user_response = input( "The contents of {} will be replaced, continue? Y/N: ".format( output_filename ) ).upper()

				if user_response == "Y":
					output_stream = open( output_filename, 'w+' )
					break
				elif user_response == "N":
					print( "Nothing was written to {}".format( output_filename ) )
					return
				else:
					print( "I'm not sure what that means, enter either 'Y' or 'N'." )
		else:
			output_stream = open( output_filename, 'w+' )


		output_stream.write( input_stream.read().upper() )

		print( "\n{}'s content was converted to uppercase and is in {}\n".format( input_filename, output_filename ) )
		return
	except IndexError:
		print( "Error ** format: 'python3 {} <input_file> <output_file>'".format( argv[0] ) )
		return

if __name__ == '__main__':
	fileToUpper( sys.argv )

