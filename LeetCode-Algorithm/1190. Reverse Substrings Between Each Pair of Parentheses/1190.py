class Solution:
    def reverseParentheses1(self, s: str) -> str:
        stack = []
        tmp = ""
        for c in s:
            if c == '(':
                if tmp:
                    stack.append(tmp)
                    tmp = ""
                stack.append('(')
            elif c == ')':
                while True:
                    top = stack.pop()
                    if top == "(":
                        break
                    tmp = top + tmp
                stack.append(tmp[::-1])
                tmp = ""
            else:
                tmp += c

        res = ''.join(stack) + tmp
        print(res)
        return res

    def reverseParentheses(self, s: str) -> str:
        stack = ['']  # 默认空串，保证第一个字母可以直接添加
        for c in s:
            if c == '(':
                stack.append('')
            elif c == ')':
                add = stack.pop()[::-1]  # 顶部元素取出，并倒序， 【即把左右括号里的都取出，倒序】
                stack[-1] += add  # 添加到前一个元素尾部，即和前一层左括号的元素合并
            else:
                stack[-1] += c  # 把c添加到stack顶部元素末尾
        return stack.pop()  # 此时所以对应括号里的元素都合并到最后一个字母里了


if __name__ == '__main__':
    assert Solution().reverseParentheses('a(bc)d') == 'acbd'
    assert Solution().reverseParentheses("(abcd)") == "dcba"
    assert Solution().reverseParentheses("(u(love)i)") == "iloveu"
    assert Solution().reverseParentheses("(ed(et(oc))el)") == "leetcode"
    assert Solution().reverseParentheses("a(bcdefghijkl(mno)p)q") == "apmnolkjihgfedcbq"
