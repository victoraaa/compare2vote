import unittest

import poll_models

class TestPollModel(unittest.TestCase):

    def test_cant_add_two_options_with_same_name(self):
        poll = poll_models.Poll("title", "question")
        option = poll_models.PollOption("name", "image_url")
        poll.add_option(option)
        self.assertEquals(option, poll.get_option_by_name("name"))

        with self.assertRaises(Exception):
            poll.add_option(poll_models.PollOption("name", "image2"))


if __name__ == '__main__':
    unittest.main()