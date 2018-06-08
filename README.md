# Visualization of sorting algorithms
Inspired by reddit user [morolin](https://www.reddit.com/user/morolin)'s [post](https://www.reddit.com/r/dataisbeautiful/comments/78fywy/sorting_algorithms_visualized_oc/) in the dataisbeautiful subreddit, I decided to try to reproduce and adapt some of his/her data visualizations in Python.

The main idea is that a sorting algorithm is applied on a matrix, row by row. Each step of the sorting process is stored, and an animated gif is then created. By using different sorting algorithms, one can then produce different gifs that showcase the features and specificities of each method.

## Insertion sort
The first sorting algorithm I chose to look at is the [insertion sort](https://en.wikipedia.org/wiki/Insertion_sort) one. I first applied it to a square n x n matrix for which each row was a shuffled list of numbers from 0 to n-1. Here is the result for n = 64:

![Insertion sort, size 64](https://thumbs.gfycat.com/HiddenKindlyDeviltasmanian-size_restricted.gif)


This result can be obtained by running the `insertion.py` file. The output can be adapted by specifying the options `--pixel` to set the size of the matrix (default value: 64) and `--gif_size` to set the size of the output gif (default value: 3), e.g.:
``` python insertion.py --pixel 24 --fig_size 3 ```
will produce a file `insertion24.gif`:

![Insertion sort, size 24](https://thumbs.gfycat.com/AmusingIdenticalBigmouthbass-size_restricted.gif)

The insertion sort algorithm can also be applied on other things than a random matrix. Here is an example with a photo, using the `insertion-photo` file, with arguments `--picture path_to_picture` and `--gif_size size_of_output_gif` (by default set to 3).

![Insertion sort, picture](https://thumbs.gfycat.com/ImperturbableSpotlessBlackrhino-size_restricted.gif)

## More to come!
