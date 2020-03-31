"""
test_transformdata.py
Jason Dinh
Created March 31, 2020
"""
import unittest
from problems.transformdata import *


class TestTransformData(unittest.TestCase):
    """
    Tests for Transform() methods
    """
    def setUp(self):
        """
        Setup for tests
        """
        self.transd = TransformData()

    def test_names_by_pos(self):
        """
        test case for names_by_pos
        """
        expected_result = {
        'C':[
        'DeAndre Jordan','Enes Kanter',
        'Hassan Whiteside','Marc Gasol',
        'Nikola Jokic','Rudy Gobert',
        'Steven Adams'
        ],
        'PF':[
        'Aaron Gordon','Al Horford',
        'Anthony Davis','Blake Griffin',
        'Giannis Antetokounmpo','Jabari Parker',
        'Joel Embiid','Kevin Love',
        'LaMarcus Aldridge','Paul Millsap',
        'Ryan Anderson','Serge Ibaka'
        ],
        'PG':[
        'Chris Paul','Damian Lillard',
        'George Hill','James Harden',
        'Jeff Teague','John Wall',
        'Jrue Holiday','Kyle Lowry',
        'Kyrie Irving','Mike Conley',
        'Russell Westbrook','Stephen Curry',
        'Zach LaVine'
        ],
        'SF':[
        'Andrew Wiggins','Chandler Parsons',
        'Danilo Gallinari','Gordon Hayward',
        'Harrison Barnes','Kawhi Leonard',
        'Kevin Durant','Otto Porter Jr.',
        'Paul George'
        ],
        'SG':[
        'Bradley Beal','CJ McCollum',
        'DeMar DeRozan','Jimmy Butler',
        'Klay Thompson','Nicolas Batum',
        'Tyler Johnson','Victor Oladipo',
        'Wesley Matthews'
        ]

        }
        actual_result = self.transd.names_by_pos()
        self.assertDictEqual(actual_result, expected_result)

    def test_mostplayedposition(self):
        """
        Test case for most_played_position() method
        """
        expected_result = {
        'C':7,'PF':12,'PG':13,'SF':9,'SG':9
        }
        actual_result = most_played_position()
        self.assertDictEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()
