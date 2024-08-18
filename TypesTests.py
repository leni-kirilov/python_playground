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

    def test_string_multiplication(self):
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

        # list of lists
        innerList1 = [1, 5, 10]
        innerList2 = ["father", "mother"]
        outterlist = [innerList1, innerList2]
        self.assertEqual(2, len(outterlist))

        # remove an item from a list
        del listCopy[0]
        self.assertEqual(3, len(listCopy))

    def test_if(self):
        number = int("0 1 2"[-1])
        if number < -1:
            number = number + 5
        elif number < 5:
            number += 1
        else:
            number *= 2

        self.assertEqual(3, number)

    def test_loop(self):
        words = ["one", "book", "cover"]
        numberOfLetters = 0
        for word in words:
            numberOfLetters += len(word)
        self.assertEqual(12, numberOfLetters)

        # range
        self.assertListEqual([1, 2, 3], list(range(1, 4)))
        self.assertListEqual([1, 3, 5], list(range(1, 6, 2)))
        self.assertEqual(10, sum(range(0, 5)))  # sum works with generators

        for indexAndWord in enumerate(words):
            self.assertEqual(int, type(indexAndWord[0]))
            self.assertEqual(str, type(indexAndWord[1]))

        for index in range(len(words)):
            self.assertEqual(int, type(index))
            self.assertEqual(str, type(words[index]))

        # TODO zip - combine 2 lists in touples

        # set reversed sorted
        self.assertListEqual([5, 4, 3, 2], list(reversed(sorted(set([4, 3, 4, 2, 5, 4])))))

        # continue
        oddNumbersSum = 0
        for number in range(-5, 5):
            if number % 2 == 0: continue
            oddNumbersSum += number
        self.assertEqual(-5, oddNumbersSum)

        # break
        brokenSum = 0
        for i in range(5):
            if i == 0:
                break
            brokenSum += i
        else:
            # not executed if we hit break in the loop
            brokenSum = 100
        self.assertEqual(0, brokenSum)

    def test_pass(self):
        pass  # Remember to implement this test!

    def test_match(self):
        # match is a regex switch
        result = 0
        number = 5
        match number:
            case 1 | 2 | 11:
                result = 10
            case _:
                result = number
        self.assertEqual(number, result)

        # unpacking a map to variables with a guard
        a_map = {1: "ala", 5: "bala"}
        unpackingResult = 0;
        for entry in a_map.items():
            match entry:
                case (key, _) if key > 1:
                    unpackingResult += key
                case (key, value):
                    unpackingResult += key * 2
                case _:
                    unpackingResult += -1
        self.assertEqual(7, unpackingResult)

    def test_functions(self):
        #TODO next - https://docs.python.org/3/tutorial/controlflow.html#defining-functions
        pass