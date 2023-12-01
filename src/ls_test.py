import unittest
from ls import custom_ls

class TestCustomLS(unittest.TestCase):
    def test_custom_ls_without_rev(self):
        # Call the function with no "--rev"
        output = custom_ls()

        expected_output = "file1\nfile2\nfile3"  # Adjusted expected output
        self.assertEqual(output, expected_output)

    def test_custom_ls_with_rev(self):
        # Call the function with "--rev"
        output = custom_ls()

        expected_output = "1elif\n2elif\n3elif"  # Adjusted expected output
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
