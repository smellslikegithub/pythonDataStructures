import unittest
from Problems.StackProblems.IntegerToBinary import IntegerToBinary

class TestIntegerToBinary(unittest.TestCase):

    #@Test
    def test_integer_to_binary_conversion_with_correct_parameter_sent(self):
        #Given
        i = IntegerToBinary()
        param = 242
        #When
        output = i.convert_unsigned_integer_to_binary(param)
        #Then
        self.assertEqual(output, "11110010", "The feature output should match with the result")

    #@Test
    def test_integer_to_binary_conversion_with_relatively_large_number(self):
        # Given
        i = IntegerToBinary()
        param = 188898989876666776767676
        # When
        output = i.convert_unsigned_integer_to_binary(param)
        # Then
        self.assertEqual(output, "101000000000000011110000011001001111110001011000100000111101010100110010111100",
                         "The feature output should match with the result")
    #@Test
    def test_integer_to_binary_conversion_with_zero_as_param(self):
        # Given
        i = IntegerToBinary()
        param = 0
        # When
        output = i.convert_unsigned_integer_to_binary(param)
        # Then
        self.assertEqual(output, "0",
                         "The feature output should match with the result")
