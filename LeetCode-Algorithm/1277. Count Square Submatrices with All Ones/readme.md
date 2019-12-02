### [1277\. Count Square Submatrices with All Ones](https://leetcode.com/contest/weekly-contest-165/problems/count-square-submatrices-with-all-ones/)
- https://leetcode.com/contest/weekly-contest-165/problems/count-square-submatrices-with-all-ones/

Difficulty: **Medium**

Given a `m * n` matrix of ones and zeros, return how many **square** submatrices have all ones.

**Example 1:**

```
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
```

**Example 2:**

```
Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1\.  
There is 1 square of side 2\. 
Total number of squares = 6 + 1 = 7.
```

**Constraints:**

*   `1 <= arr.length <= 300`
*   `1 <= arr[0].length <= 300`
*   `0 <= arr[i][j] <= 1`

#### Solution
- 题意：找出全1的子矩阵个数
- 我没优化，全暴力Python TLE了一次
- 改用Javascript，AC
- 其实至少可以用前缀和优化一下，降低一级复杂度

Language: **JavaScript**

```javascript
/**
 * @param {number[][]} matrix
 * @return {number}
 */
var countSquares = function(matrix) {
    const la = matrix.length;
    const lb = matrix[0].length;
    const l = Math.min(la,lb);
    let c =0;
    //let t=0;
    for(let size=1;size<=l;size++){
        //let st=0;
        for(let a=0;a<=la-size;a++){
            for(let b=0;b<=lb-size;++b){
                t=check(size,a,b,matrix);
                c+=t;
                //st+=t;
            }
        }
        //console.log(st)
    }
    return c;
};
​
function check(size,a,b,matrix){
    for(let i=0;i<size;++i){
        for(let j=0;j<size;++j){
            if(matrix[a+i][b+j]===0){
                return 0;
            }
        }
    }
    return 1;
}
```