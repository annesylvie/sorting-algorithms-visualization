# Visualization of sorting algorithms
Inspired by reddit user [morolin](https://www.reddit.com/user/morolin)'s [post](https://www.reddit.com/r/dataisbeautiful/comments/78fywy/sorting_algorithms_visualized_oc/) in the dataisbeautiful subreddit, I decided to try to reproduce and adapt some of his/her data visualizations in Python.

The main idea is that a sorting algorithm is applied on a matrix, row by row. Each step of the sorting process is stored, and an animated gif is then created. By using different sorting algorithms, one can then produce different gifs that showcase the features and specificities of each method.

## Insertion sort
The first sorting algorithm I chose to look at is the [insertion sort](https://en.wikipedia.org/wiki/Insertion_sort) one. I first applied it to a square n x n matrix for which each row was a shuffled list of numbers from 0 to n-1. Here is the result for n = 64:

![Insertion sort, size 64, to be added]()


This result can be obtained by running the `insertion.py` file. The size of the matrix can be adapted by specifying the option `--size`, e.g.:
``` python insertion.py --size 24 ```
will produce a file `insertion24.gif`:

![Insertion sort, size 24](https://media.giphy.com/media/1wpOLbs2TrpV94zEuO/giphy.gif)

## More to come!
