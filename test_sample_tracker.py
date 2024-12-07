import json
import os
import unittest
from sample_tracker import load_samples

class TestLoadSamples(unittest.TestCase):
    def setUp(self):
        # Create a sample JSON file for testing
        self.test_file = 'samples.json'
        with open(self.test_file, 'w') as f:
            json.dump([{"sample_id": "1", "sample_type": "Type A", "location": "Location A", "status": "Active"}], f)

    def tearDown(self):
        # Remove the test file after the test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load_samples(self):
        samples = load_samples()
        self.assertEqual(len(samples), 1)
        self.assertEqual(samples[0]['sample_id'], "1")
        self.assertEqual(samples[0]['sample_type'], "Type A")
        self.assertEqual(samples[0]['location'], "Location A")
        self.assertEqual(samples[0]['status'], "Active")

if __name__ == '__main__':
    unittest.main()
