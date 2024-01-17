There are N children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:
1. Each child must have at least one candy.
2. Children with a higher rating get more candies than their neighbours.
What is the minimum candies you must give?
Input Format:
The first and the only argument contains N integers in an array A.
Output Format:
Return an integer, representing the minimum candies to be given.
Example:
Input 1:
A = [1, 2]
Output 1:
3
Each child must have at least one candy.
Children with a higher rating should get more candies than their neighbors.
Here's a brief explanation of the code:

Initialize an array candies with the same length as the input array A, filled with 1 candy for each child.

Perform a left-to-right pass through the array, and if a child has a higher rating than its left neighbor, give it one more candy than the left neighbor.

Perform a right-to-left pass through the array, and if a child has a higher rating than its right neighbor, update its candy count to be the maximum of its current count and the right neighbor's count plus one.

The final count of candies for each child is the maximum value obtained from the two passes.

Sum up the total number of candies distributed.

In the example with A = [1, 2], the algorithm determines that the children should receive 1 candy and 2 candies, respectively, satisfying the conditions. The total minimum number of candies is 3.
