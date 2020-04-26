import unittest

from LinkedList import LinkedList


class LinkedListTest(unittest.TestCase):

    # @Test
    def test_append_at_front_of_the_linked_list(self):
        # Given
        test_data = [10, 20, 30, 40]
        my_list = LinkedList()
        # When
        my_list.append_at_front(10)
        my_list.append_at_front(20)
        my_list.append_at_front(30)
        my_list.append_at_front(40)

        # Then
        self.assertEqual(my_list.head.data, 40)
        self.assertEqual(my_list.head.next.data, 30)
        self.assertEqual(my_list.head.next.next.data, 20)
        self.assertEqual(my_list.head.next.next.next.data, 10)

    def test_append_at_front_of_the_linked_list_with_different_type_pf_data(self):
        # Given
        test_data = [10, 1.34, "Hello", 40]
        my_list = LinkedList()
        # When
        my_list.append_at_front(test_data[0])
        my_list.append_at_front(test_data[1])
        my_list.append_at_front(test_data[2])
        my_list.append_at_front(test_data[3])

        # Then
        self.assertEqual(my_list.head.data, test_data[3])
        self.assertEqual(my_list.head.next.data, test_data[2])
        self.assertEqual(my_list.head.next.next.data, test_data[1])
        self.assertEqual(my_list.head.next.next.next.data, test_data[0])

    def test_insert_at_certain_position_in_the_linked_list(self):
        # Given
        test_data = [10, 20, 30, 50]
        my_list = LinkedList()
        my_list.append_at_end(10)
        my_list.append_at_end(20)
        my_list.append_at_end(30)
        my_list.append_at_end(50)
        # When
        my_list.append_at_position(100, 3)  # the data = 100, will be appended in the third slot of the list

        # Then
        self.assertEqual(my_list.head.data, 10)
        self.assertEqual(my_list.head.next.data, 20)
        self.assertEqual(my_list.head.next.next.data, 100) # the new appended values must be at this slot
        self.assertEqual(my_list.head.next.next.next.data, 30)
        self.assertEqual(my_list.head.next.next.next.next.data, 50)

        # Given
        test_data = [10, 20, 30, 40]
        my_list = LinkedList()
        # When
        my_list.append_at_front(10)
        my_list.append_at_front(20)
        my_list.append_at_front(30)
        my_list.append_at_front(40)

        # Then
        self.assertEqual(my_list.head.data, 40)
        self.assertEqual(my_list.head.next.data, 30)
        self.assertEqual(my_list.head.next.next.data, 20)
        self.assertEqual(my_list.head.next.next.next.data, 10)

    #@Test
    def test_printing_empty_list(self):
        # Given
        test_output = "Empty List!"
        my_list = LinkedList()

        # When
        output = my_list.printList()
        # Then
        self.assertEqual(output, test_output)
