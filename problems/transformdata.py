"""
dataset.py
Mihaela
March 11, 2020
"""


class TransformData():
    """
    Data processing functionality
    """

    def __init__(self):
        """
        Creates and initializes the class attributes.
        Attributes: three parallel lists
            names: list of strings
            salaries: list of integers
            positions: list of 2-character strings
        """
        self.names = [
            'Stephen Curry', 'Russell Westbrook', 'Chris Paul', 'James Harden',
            'Blake Griffin', 'Gordon Hayward', 'Kyle Lowry', 'Paul George',
            'Mike Conley', 'Kevin Durant', 'Paul Millsap', 'Al Horford',
            'Damian Lillard', 'DeMar DeRozan', 'Otto Porter Jr.',
            'Jrue Holiday', 'CJ McCollum', 'Joel Embiid', 'Andrew Wiggins',
            'Bradley Beal', 'Anthony Davis', 'Hassan Whiteside',
            'Nikola Jokic', 'Steven Adams', 'Giannis Antetokounmpo',
            'Marc Gasol', 'Kevin Love', 'Chandler Parsons', 'Harrison Barnes',
            'Nicolas Batum', 'Rudy Gobert', 'Kawhi Leonard', 'DeAndre Jordan',
            'LaMarcus Aldridge', 'Serge Ibaka', 'Aaron Gordon',
            'Danilo Gallinari', 'Victor Oladipo', 'Jimmy Butler',
            'Ryan Anderson', 'Kyrie Irving', 'Jabari Parker', 'Zach LaVine',
            'Tyler Johnson', 'John Wall', 'Jeff Teague', 'George Hill',
            'Klay Thompson', 'Enes Kanter', 'Wesley Matthews'
        ]
        self.salary = [
            37457154, 35654150, 35654150, 35650150, 32088932, 31214295,
            31200000, 30560700, 30521115, 30000000, 29230769, 28928709,
            27977689, 27739975, 26011913, 25976111, 25759766, 25467250,
            25467250, 25434263, 25434263, 25434262, 24605181, 24157303,
            24157303, 24119025, 24119025, 24107258, 24107258, 24000000,
            23241573, 23114067, 22897200, 22347015, 21666667, 21590909,
            21587579, 21000000, 20445779, 20421546, 20099189, 20000000,
            19500000, 19245370, 19169800, 19000000, 19000000, 18988725,
            18622514, 18622514
        ]
        self.position = [
            'PG', 'PG', 'PG', 'PG', 'PF', 'SF', 'PG', 'SF', 'PG', 'SF', 'PF',
            'PF', 'PG', 'SG', 'SF', 'PG', 'SG', 'PF', 'SF', 'SG', 'PF', 'C',
            'C', 'C', 'PF', 'C', 'PF', 'SF', 'SF', 'SG', 'C', 'SF', 'C', 'PF',
            'PF', 'PF', 'SF', 'SG', 'SG', 'PF', 'PG', 'PF', 'PG', 'SG', 'PG',
            'PG', 'PG', 'SG', 'C', 'SG'
        ]

    def record_per_row(self):
        """
        Writes a CSV file with as many records as the size of any of the lists
        A record is a row in the file, with three columns, corresonding to
        a name, salary, and position.
        """
        with open('nba.txt', 'w') as nba_file:
            for num, sal, pos in zip(self.names, self.salary, self.position):
                nsp_row = num + ',' + str(sal) + ',' + pos + '\n'
                nba_file.write(nsp_row)

    def names_by_pos(self):
        """
        Returns a dictionary whose keys are the positions and values
        are lists of the names corresponding to each position.

        input = list of positions, list of names... lists corresponds to e/o.
        returns dictionary
            key = positions
            value = list of names
        """
        posnamedict = {}
        for pos, name in zip(self.position, self.names):
            if pos in posnamedict:
                posnamedict[pos].append(name)
            else:
                posnamedict[pos] = [name]
            posnamedict[pos].sort()
        return posnamedict

    @classmethod
    def most_played_position(cls):
        """
        Uses dictionary created from names_by_pos to create a new dictionary
        whose keys are positions and the values are the length of lists
        of the players for each position.
        input = dictionary
            key = position
            value = list of names
        returns dictionary
            key = positions
            value = length of lists of names
        """
        inputdata = TransformData().names_by_pos()
        numposdict = {}
        for key in inputdata:
            numposdict[key] = len(inputdata[key])
        return numposdict

    @classmethod
    def main(cls):
        """
        Shortens calling methods in the class TransformData()
        """
        transd = TransformData()
        transd.record_per_row()
        transd.names_by_pos()
        transd.most_played_position()


if __name__ == '__main__':
    TransformData().main()
