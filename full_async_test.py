# -*- coding: utf-8 -*-
import json
import os
import unittest


from transcribe import start


TEST_FILE_PATH = 'output.json'
TEST_FLAC_URI = 'gs://sam-to-text-audio/test.flac'


class FullAsyncTest(unittest.TestCase):

    def tearDown(self):
        if os.path.isfile(TEST_FILE_PATH):
            os.remove(TEST_FILE_PATH)

    def test_full_async(self):
        start(TEST_FLAC_URI, TEST_FILE_PATH)
        with open(TEST_FILE_PATH, 'r') as f:
            results = json.loads(f.read())
            import ipdb ; ipdb.set_trace()
            self.assertEqual(
                results['results'][0]['alternatives'][0]['transcript'],
                'Sam Harris is the Flying Spaghetti Monster'
            )


if __name__ == '__main__':
    unittest.main()
