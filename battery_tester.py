"""This module calculates information about a lipo based on a voltage reading"""
import unittest


def cell_count(voltage):
    """Returns the number of cells in a lipo based on input voltage"""

    try:
        float(voltage)
    except ValueError:
        raise TypeError('{} is invalid, enter a number between 3.5 and 25.2'.format(voltage))
    else:
        try:
            if 3.5 <= voltage != 21:
                # this is the main calculation of number of cells
                return list([a + 1 for a in range(6) if voltage / (a + 1) <= 4.2])[0]

            elif voltage == 21:
                raise ValueError('21V could be 5 cell at 3.5V or 6 cell at 4.2V')
            elif voltage < 3.5:
                raise ValueError('Voltage {}V too small'.format(voltage))
        except IndexError:
            raise ValueError('Enter the voltage of a 6 cell battery or less')


def cell_voltage(voltage):
    """returns the average cell voltage of a lipo pack based on the input voltage"""

    return round(voltage / cell_count(voltage), 2)


class TestBatteryTester(unittest.TestCase):
    """testing suite for the two functions"""

    def test_cell_voltage(self):
        self.assertEqual(cell_voltage(3.9), 3.9)
        self.assertEqual(cell_voltage(7), 3.5)
        self.assertEqual(cell_voltage(12), 4)
        self.assertEqual(cell_voltage(16.8), 4.2)
        self.assertEqual(cell_voltage(19), 3.8)
        self.assertEqual(cell_voltage(22), 3.67)
        self.assertRaises(ValueError, cell_count, 21)
        self.assertRaises(ValueError, cell_count, 26)
        self.assertRaises(ValueError, cell_count, 2)
        self.assertRaises(TypeError, cell_count, '20V')

    def test_cell_count(self):
        self.assertEqual(cell_count(3.9), 1)
        self.assertEqual(cell_count(7), 2)
        self.assertEqual(cell_count(12), 3)
        self.assertEqual(cell_count(16.8), 4)
        self.assertEqual(cell_count(19), 5)
        self.assertEqual(cell_count(22), 6)
        self.assertRaises(ValueError, cell_count, 21)
        self.assertRaises(ValueError, cell_count, 26)
        self.assertRaises(ValueError, cell_count, 2)
        self.assertRaises(TypeError, cell_count, '20V')


if __name__ == "__main__":
    if False:  # change this to true to run some tests
        unittest.main()
    else:

        try:
            v = float(input("enter the voltage of a 1-6S lipo battery: "))
        except ValueError:
            print("Please enter a number")
        else:
            print("{}V is a {} cell battery with an average cell voltage of {}".format(v, cell_count(v), cell_voltage(v)))
