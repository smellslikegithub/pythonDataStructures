import unittest
from Problems.StackProblems.BalancedParanthesis import Solution


class TestSolution(unittest.TestCase):

    # @Test
    def test_balanced_paranthesis_with_no_arguments(self):
        # Given
        testlist = ['(']
        s = Solution()
        # When
        result = s.is_paranthesis_balanced(testlist)
        # Then result should be false
        self.assertFalse(result, "The solution should return false")

    # @Test
    def test_balanced_paranthesis_with_balanced_paranthesis(self):
        # Given
        testList = ['(','{','<','>','}' ,')']
        s = Solution()
        # When
        result = s.is_paranthesis_balanced(testList)
        # Then result should be false
        self.assertTrue(result, "The solution should return true")

        # @Test

    def test_balanced_paranthesis_with_unbalanced_paranthesis(self):
        # Given
        testList = ['(', '{', '<', '>', '}', '>']
        s = Solution()
        # When
        result = s.is_paranthesis_balanced(testList)
        # Then result should be false
        self.assertFalse(result, "The solution should return false")

    def test_balanced_paranthesis_with_unbalanced_paranthesis_but_no_starting_braces(self):
        # Given
        testList = ['>',')']
        s = Solution()
        # When
        result = s.is_paranthesis_balanced(testList)
        # Then result should be false
        self.assertFalse(result, "The solution should return false")

    def test_balanced_paranthesis_with_unbalanced_paranthesis_with_arbitrary_characters(self):
        # Given
        testList = ['!',',','*']
        s = Solution()
        # When
        result = s.is_paranthesis_balanced(testList)
        # Then result should be false
        self.assertFalse(result, "The solution should return false")

    def test_run_for_demo_code(self):
        for x in range(0, 3):
            print("We're on time %d" % (x))


if __name__ == '__main__':
    unittest.main()
