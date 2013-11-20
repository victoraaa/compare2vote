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


    def test_vote_changes_ranking(self):
        poll = poll_models.Poll("title", "question")
        option1 = poll_models.PollOption("option1", "image_url")
        option2 = poll_models.PollOption("option2", "image_url")
        poll.add_option(option1)
        poll.add_option(option2)
        poll.vote(option1, option2)

        self.assertEquals([option1, option2], poll.ranking)

        poll.vote(option2, option1)
        poll.vote(option2, option1)
        self.assertEquals([option2, option1], poll.ranking)

    def test_cant_get_inexistent_option(self):
        poll = poll_models.Poll("title", "question")
        option1 = poll_models.PollOption("option1", "image_url")
        option2 = poll_models.PollOption("option2", "image_url")
        poll.add_option(option1)
        poll.add_option(option2)

        with self.assertRaises(KeyError):
            poll.get_option_by_name("inexistent_option")

    def test_win_against_stronger_is_better(self):
        poll = poll_models.Poll("title", "question")
        option1 = poll_models.PollOption("option1", "image_url")
        option2 = poll_models.PollOption("option2", "image_url")
        option3 = poll_models.PollOption("option3", "image_url")
        option4 = poll_models.PollOption("option4", "image_url")
        poll.add_option(option1)
        poll.add_option(option2)
        poll.add_option(option3)
        poll.add_option(option4)
        poll.vote(option1, option2)

        poll.vote(option3, option1)
        poll.vote(option4, option2)
        self.assertEquals([option3, option4, option1, option2], poll.ranking)

if __name__ == '__main__':
    unittest.main()