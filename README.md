### record_per_row()
```
def record_per_row(self):
    """
    Writes a CSV file with as many records as the size of any of the lists
    A record is a row in the file, with three columns, corresponding to
    a name, salary, and position.
    """
```
* Create 3-field records from the three attributes such that
    * a **record** has elements at the same position in the three lists.
* Format a record as a string with the three elements separated by comma
* Write each record to the **nba.txt** text file

We use the accumulation pattern with **accumulator** `nab_file`
* Iteration is over three sequences simultaneously, the class attributes
    * three loop variables `n`, `s`, `p` get hold of elements in `self.names`,
    `self.salaries`, `self.positions` which have the same positions
    * we use `zip()` built-in function to allow for parallel processing
    * we assemble string representations of the elements including the commas
    and store in `nba_row` string local variable
    * we write `nba_row` to the file object **accumulator** `nba_file`

### names_by_pos()
```
def names_by_pos(self):
      """
      Returns a dictionary whose keys are the positions and values
      are lists of the names corresponding to each position.

      input = list of positions, list of names... lists corresponds to e/o.
      returns dictionary
          key = positions
          value = list of names
      """
```
* Instantiate an empty accumulator dictionary named `posnamedict`.
* iterate over two lists, position and names, simultaneously.
  * we use `zip()` built-in function to allow for parallel processing
  * Iteration variables will be `pos` and `name`.
  * Each loop will have conditional if position is in the dictionary as a key.
    * if not then add position as new key and value is empty list.
  * append name of position to list.
  * sort lists in values of keys for organization.
* return the accumulator dictionary.

### most_played_position()
```
def most_played_position(self):
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
```
* Assign variable input to Call the method names_by_pos for the dictionary.
* Instantiate a new dictionary named numposdict.
* Iterate through input and Iteration variable will be key.
  * each loop will assign key to new key in numposdict, value will be length of the list of the value at key of input.
* return numposdict
