import unittest
from IPLDataTransformer import IPLDataTransformer

class TestIPLDataTransformer(unittest.TestCase):
    def setUp(self):
        self.data_transformer = IPLDataTransformer("mock_matches.csv")

    def test_matches_per_year(self):
        expected_result = {'2017': 8, '2008': 11}
        result = self.data_transformer.matches_per_year()
        self.assertEqual(result, expected_result)


    def test_matches_won_per_year(self):
        expected_result = {
            '2008': {
                'Chennai Super Kings': 2,
                'Deccan Chargers': 1,
                'Kings XI Punjab': 3,
                'Kolkata Knight Riders': 2,
                'Mumbai Indians': 1,
                'Rajasthan Royals': 2
            },
            '2017': {
                'Gujarat Lions': 1,
                'Kings XI Punjab': 1,
                'Mumbai Indians': 3,
                'Rising Pune Supergiant': 1,
                'Sunrisers Hyderabad': 2
            }
        }

        result = self.data_transformer.matches_won_per_year()
        self.assertEqual(result, expected_result)

        
    def test_matches_conceded(self):
        expected_result = {}
        result = self.data_transformer.matches_conceded()

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
