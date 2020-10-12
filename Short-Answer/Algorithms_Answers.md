#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
O(n)
Recursive addition (x1), Additional Processing for n (x2), Recursive multiplication as loop (x3).
Based on the size of n, growth is exponential.


b)
O(n^2) 
Has to iterate twice to find an output that meets the demands of the solution.
Nested loop.

c)
O(n) - Direct input, simple Output.
Recursion.

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

n = size of array
f <= break limit
anything Under f doesn't break.
f is unknown

O(log n) - Binary Search Tree would be the best effort that once a break is found at say the largest input, then you scale back on the input size to be under the first break point, then check each subsequent reverse to see if the egg breaks. Once it doesn't break, then check between those two points where the last lowest break and the largest non-break to find the point that defines f.
Halve the hight of n, create m element. Median. Check between Middle and hight of n. n[:2]. Change m to continue to be middle. m[:2] until f is found.