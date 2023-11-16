# lottery_numbers

### Based on In-Class Exercise 3 from MGTC28

This is a program to generate Lotto 6/49 numbers.

The program allows users to do one or more draws at once. Currently, the program can only generate numbers randomly.

Users may use the generated numbers to pick ticket numbers when buying lottery tickets.


The generated numbers follow these constraints:
- One draw = six nonrepeating integers from 1-49
- If multiple draws are done at once, numbers in the last draw won't appear in the current draw


This program uses the **random library** to generate numbers:
- [random](https://www.codecademy.com/resources/docs/python/random-module)
