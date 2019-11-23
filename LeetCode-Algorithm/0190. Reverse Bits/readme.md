### [190\. Reverse Bits](https://leetcode.com/problems/reverse-bits/)

Difficulty: **Easy**


Reverse bits of a given 32 bits unsigned integer.

**Example 1:**

```
Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
```

**Example 2:**

```
Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
```

**Note:**

*   Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
*   In Java, the compiler represents the signed integers using . Therefore, in **Example 2** above the input represents the signed integer `-3` and the output represents the signed integer `-1073741825`.

**Follow up**:

If this function is called many times, how would you optimize it?


#### Solution
- 水题，注意可以用 int(num_or_string, base) 转换进制，第一个参数可以是数字或字符串

Language: **Python**

```python
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bin_str = bin(n)[2:]
​
        ch = ['0'] * 32
        for id, bi in enumerate(reversed(bin_str)):
            ch[id] = str(bi)
        b2 = ''.join(ch)
        print(b2)
​
        return int(b2, 2)
​
    def reverseBits2(self, n):
        bin_str = bin(n)[2:]
        print(bin_str)
​
        r_bit_32 = '{:0>32}'.format(bin_str)[::-1]
        print(r_bit_32)
​
        res = int(r_bit_32, 2)
        print(res)
        return res
​
​
if __name__ == '__main__':
    assert Solution().reverseBits(43261596) == 964176192
​
```