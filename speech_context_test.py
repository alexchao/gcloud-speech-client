# -*- coding: utf-8 -*-
import unittest

from speech_context import read_phrases_from_file


TEST_FILE_PATH = 'test-data/sample-speech-context.json'


class SpeechContextImportTestCase(unittest.TestCase):

    def test_read_from_file(self):
        self.assertEqual(
            read_phrases_from_file(TEST_FILE_PATH),
            ['flying spaghetti monster', 'philosophy', 'sam harris']
        )


if __name__ == '__main__':
    unittest.main()
