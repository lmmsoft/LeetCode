# Link
- https://leetcode.com/contest/biweekly-contest-5/problems/parallel-courses/
- https://leetcode.com/submissions/detail/247383849/
- https://leetcode.com/contest/biweekly-contest-5
- https://leetcode.com/contest/biweekly-contest-5/ranking/

# 1136. Parallel Courses Copy for Markdown

User Accepted: 384

User Tried: 484

Total Accepted: 392

Total Submissions: 794

Difficulty: Hard

There are N courses, labelled from 1 to N.

We are given relations[i] = [X, Y], representing a prerequisite relationship between course X and course Y: course X has to be studied before course Y.

In one semester you can study any number of courses as long as you have studied all the prerequisites for the course you are studying.

Return the minimum number of semesters needed to study all courses.  If there is no way to study all the courses, return -1.

 

Example 1:



Input: N = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: 
In the first semester, courses 1 and 2 are studied. In the second semester, course 3 is studied.
Example 2:



Input: N = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: 
No course can be studied because they depend on each other.
 

Note:

1 <= N <= 5000
1 <= relations.length <= 5000
relations[i][0] != relations[i][1]
There are no repeated relations in the input.

# Solution
- 比赛时候没做出来，其实是道 拓扑排序 的题目
- 这题是求拓扑排序的层数，即每层把入度为0的节点移除，求有多少层，如果最后还有层的入度不为0，说明有环，返回-1