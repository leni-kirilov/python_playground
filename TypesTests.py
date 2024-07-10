import unittest
import os

class TypesTests(unittest.TestCase):

    def test_numbers(self):
        self.assertEqual(int, type(1))
        self.assertEqual(float, type(5 / 1))

    def test_string(self):
        self.assertEqual(str, type("this is str"))
        self.assertEqual(str, type('this is str, too in single quotes'))

    def test_string_path(self):
        # this doesn't work -> print(r'C:\this\will\work\')
        self.assertEqual("C:\\this\\will\\work\\", os.path.join(r'C:\this\will\work', ''))

    def test_string_mulitplication(self):
        self.assertEqual('baba', 2 * 'ba')
        self.assertEqual('baba', "ba" 'ba')
        self.assertEqual('baba', "ba" + 'ba')

    def test_string_slicing(self):
        word = "word"
        self.assertEqual("Word", "W" + word[1:], "Strings are immutable")
        self.assertEqual(4, len(word))

        self.assertEqual('w', word[0], "first letter of word is ")
        self.assertEqual('d', word[-1], "last letter of word is ")

        self.assertEqual('or', word[1:3], "middle of word is ")
        self.assertEqual('rd', word[2:100], "bigger slice of short word produces no err")
        self.assertEqual('', word[100:200], "out of scope slice produces empty string")

        print(r'this is a raw string. No \ are escaped. c:\programFiles\some_folder ')
        self.assertEqual('just a string',
                         "just "
                         "a "
                         "string",
                         "string on multiple lines is concatinated"
                         )

    def test_list(self):
        numbers = [1, 2, 5]
        # indexing, slicing, concat too
        numbers[1] = 10  # but muttable
        print(numbers)
        self.assertEqual([1, 10, 5], numbers)

        numbers.append(0)
        self.assertEqual([1, 10, 5, 0], numbers)

        # copy a list
        listCopy = numbers[:]
        listCopy[0] = 0
        self.assertNotEqual(listCopy[0], numbers[0])  # 0 1
