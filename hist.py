from matplotlib import animation

"""
This module contains all functions needed to organize an output
from a sorting algorithm into a list of nxn arrays that can be
then plotted using imshow, animated and finally saved as a gif.
"""

# def insertionSort(alist):
#     """
#     Returning the history of running the insertion sorting 
#     algorithm on a one dimensional list
#     """
#     history = [alist[:]]
#     for index in range(1,len(alist)):
#         currentvalue = alist[index]
#         position = index
#         while position>0 and alist[position-1]>currentvalue:
#             alist[position]=alist[position-1]
#             alist[position-1]=currentvalue
#             position = position-1
#             history.append(alist[:])           
#         alist[position]=currentvalue
#     return history

def sort_hist_gen(matrix, sort_func):
    """
    For an input matrix, this function sorts (using the sort_func function)
    each row, and keeps an history of the state of the row at each
    operation. Then, it extends the smaller histories up to the longest
    history's size so that all histories have the same size.
    """
    history = []
    for i in range(len(matrix[0])):
        hist_item = sort_func(matrix[i][:])
        history.append(hist_item)
    hist_size = max(len(item) for item in history)
    for item in history:
        while len(item) < hist_size:
            item.append(item[-1])
    return history

def line2mat_hist(row_hist):
    """
    The output of sort_hist_gen is a list of histories for each row.
    Since we want to have a succession of matrices showing the state
    of the sorting of the whole matrix after each step, we need to
    convert a row_hist into a mat_hist.
    So this converts the output of sort_hist_gen (a list of histories of
    the sort_func sorting algorithm applied on a matrix line by line) to
    a list of matrix histories.
    """
    mat_hist = []
    mat = []
    for i in range(len(row_hist[0])):
        for j in range(len(row_hist[0][0])):
            mat.append(row_hist[j][i])
        mat_hist.append(mat)
        mat = []
    return mat_hist

def init():
	"""
	Initialisation of the animation to completely random state of matrix
	"""
	im.set_data(M)
	return [im]

def animate(i, M_hist, im):
	"""
	Animation: each image is extracted from the matrix histories.
	"""
	a = im.get_array()
	a = M_hist[i]
	im.set_array(a)
	return [im]

