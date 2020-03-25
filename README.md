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
