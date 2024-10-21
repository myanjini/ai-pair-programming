import unittest
from Dog import Dog

class TestDog(unittest.TestCase):
    def setUp(self):
        self.dog = Dog("Buddy", "Golden Retriever", 3)

    def test_bark(self):
        self.assertEqual(self.dog.bark(), "Woof!")

    def test_run(self):
        self.assertEqual(self.dog.run(), "Buddy is running!")

    def test_attributes(self):
        self.assertEqual(self.dog.name, "Buddy")
        self.assertEqual(self.dog.breed, "Golden Retriever")
        self.assertEqual(self.dog.age, 3)

if __name__ == '__main__':
    unittest.main()