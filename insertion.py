import matplotlib.pyplot as plt
import random as rand
from matplotlib import animation
import argparse
from hist import *


def insertion_sort(alist):
    """
    Returns the history of running the insertion sorting 
    algorithm on a list of numbers, i.e. saves the state of
    the list after each step of the algorithm.
    """
    history = [alist[:]]
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            alist[position-1]=currentvalue
            position = position-1
            history.append(alist[:])           
        alist[position]=currentvalue
    return history


if __name__ == '__main__':
    
    # Gets argument from command line if specified or set it to default value
    parser = argparse.ArgumentParser()
    parser.add_argument("--pixel", help="Size (number of pixels) of the matrix to be generated", type=int)
    parser.add_argument("--gif_size", help="Size of the output gif", type=int)
    args = parser.parse_args()
    if args.pixel:
        sq_size = args.pixel
    else:
        sq_size = 64
    if args.gif_size:
        fig_size = args.gif_size
    else:
        fig_size = 3

    # Generates square matrix of size sq_size, where each row is a list of numbers from 1 to sq_size that is then shuffled.
    sorted_row = list(range(sq_size))
    M = [sorted_row[:] for _ in range(sq_size)]
    for row in M:
        rand.shuffle(row)

    # Apply the sorting algorithm on random matrix and get the list of matrix histories
    M_hist = line2mat_hist(sort_hist_gen(M, insertion_sort))

    # Prepares the imshow plot
    fig = plt.figure(figsize=(fig_size, fig_size))
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    ax.set_aspect(1)
    fig.add_axes(ax)
    im = plt.imshow(M, interpolation="none")
    plt.axis("off")

    # Animates and saves the animation
    anim = animation.FuncAnimation(fig, animate, fargs=(M_hist, im,), frames=len(M_hist), interval=20, blit=True)
    anim.save(f'insertion{sq_size}.gif', writer='imagemagick', fps=60)