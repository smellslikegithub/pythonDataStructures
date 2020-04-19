from Stack import Stack as stack


# Stack to determine, if a string of paranthesis is balanced or not
# ({[]}) -> Balanced
# ([}]) -> not balanced

class Solution:
    def __init__(self):
        self.parenthesisOpen = ['(', '{', '[', '<']
        self.myStack = stack()
        self.isBalanced = True

    @staticmethod
    def check_pair(p1, p2):
        if p1 == '<' and p2 == '>':
            return True
        elif p1 == '(' and p2 == ')':
            return True
        elif p1 == '[' and p2 == ']':
            return True
        elif p1 == '{' and p2 == '}':
            return True
        else:
            return False

    def is_paranthesis_balanced(self, list):
        # user may give list like {([])}
        for e in list:
            if e in self.parenthesisOpen:
                self.myStack.push(e)
            else:
                if self.myStack.is_empty():
                    self.isBalanced = False
                else:
                    popped = self.myStack.pop()
                    if Solution.check_pair(popped, e) == False:
                        self.isBalanced = False
                    else:
                        self.isBalanced = True

        if self.myStack.is_empty() and self.isBalanced:
            return True
        else:
            return False


def main():
    solve = Solution()
    testList = ['(','{','<','>','}' ,')']
    print(solve.is_paranthesis_balanced(testList))


if __name__ == "__main__":
    main()
