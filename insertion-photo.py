import matplotlib.pyplot as plt
import random as rand
from matplotlib import animation
import argparse
import matplotlib.image as mpimg
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
    parser.add_argument("--picture", help="Path to the picture to be sorted", type=str)
    parser.add_argument("--gif_size", help="Size of the output gif", type=int)
    args = parser.parse_args()
    if args.gif_size:
        fig_size = args.gif_size
    else:
        fig_size = 3
    if args.picture:
        im_path = args.picture
    else:
        raise Exception()

    # Load Image
    img = mpimg.imread(im_path)

    # Apply the sorting algorithm on random matrix and get the list of matrix histories
    #M_hist = line2mat_hist(insertionSortMatrix(img.tolist()))
    M_hist = line2mat_hist(sort_hist_gen(img.tolist(), insertion_sort))
    
    # Prepares the imshow plot
    fig = plt.figure(figsize=(fig_size, fig_size))
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    ax.set_aspect(1)
    fig.add_axes(ax)
    im = plt.imshow(img, interpolation="none")
    plt.axis("off")

    # Animates and saves the animation
    anim = animation.FuncAnimation(fig, animate, fargs=(M_hist, im,), frames=len(M_hist), interval=20, blit=True)
    anim.save('insertion-photo.gif', writer='imagemagick', fps=60)