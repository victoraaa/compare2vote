import unittest

import poll_models

class TestPollModel(unittest.TestCase):

    def test_add_option(self):
        poll = poll_models.Poll("title", "question")
        self.assertEquals("title", poll.title)

        # should raise an exception for an immutable sequence
        #self.assertRaises(TypeError, random.shuffle, (1,2,3))

    def test_cant_add_two_options_with_same_name(self):
        #element = random.choice(self.seq)
        #self.assertTrue(element in self.seq)
        pass


if __name__ == '__main__':
    unittest.main()