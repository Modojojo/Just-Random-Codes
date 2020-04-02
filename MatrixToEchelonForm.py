import numpy as np

# NOTE: uncomment all the print statements to check line by line working if the program and how the matrix row changes after each operation in he console window.

class MatrixIsSingular(Exception):
	pass

def mainFunc(matrix):
	A = np.array(matrix, dtype = np.float_)
	ans = None
	try:
		ans = fixRows(A)
	except MatrixIsSingular:
		return "\nmatrix is not singular"

	print("\n==================Final Matrix====================\n")
	return ans


def fixRows(matrix):

	'''
	converts matrix to echelon form by row by row.
	returns converted matrix (numpy array)
	'''

	n_rows_from_zero = len(matrix)

	# iterate throughout the matrix
	for i in range(n_rows_from_zero):
		# print("_____________________________________________________\n\nRow : " +str(i))

		# iterate from 0 to i and replace the sub-diagonal elements to zero.
		for n in range(0,i):
			matrix[i] = matrix[i] - matrix[i,n] * matrix[n]
			# print("    *Setting sub diagonal to zero for j = ", n)
			# print("        Matrix row : ", matrix[i])

		# iterate from i to length (number of rows) of matrix
		for x in range(i+1, n_rows_from_zero):
			# Check if diagonal element is zero 
			if(matrix[i,i] == 0):
				# print("\n    found diagonal is zero and adding row[{}]".format(x))

				# if diagnoal element is zero try adding any of the next rows to make it non zero.
				matrix[i]  = matrix[i] + matrix[x]
				# print("        row[{}] : {}".format(i, matrix[i]))

				# iterate from 0 to the current row and make the sub-diagonal elements to zero.
				for n in range(0,i):

					# make the sub diagonal elements that is the elements before the diagonal position of the current row.
					matrix[i] = matrix[i] - matrix[i,n] * matrix[n]
					# print("    Setting sub diagonal to zero for j = ", n)
					# print("        Matrix row : ", matrix[i])


			# if the diagonal is not zero then break the loop.
			else:
				break

		# if all the rows have been traversed and still diagonal element is zero, raise an error	
		if(matrix[i,i] == 0):
			print("EXCEPTION : Diagonal still zero after applying all the rules.")
			raise MatrixIsSingular()

		# Transform row such as diagonal element is 1.

		matrix[i] = matrix[i]/matrix[i,i]
		# print("row[{}] After dividing it by the diagonal element [1,1] of to make it equal to 1 : {}".format(i, matrix[i]))

	return matrix

# change the matrix below and observe the answer

m = np.array([
        [0, 7, -5, 3],
        [2, 8, 0, 4],
        [3, 12, 0, 5],
        [1, 3, 1, 3]
    ], dtype=np.float_)


print(mainFunc(m))
