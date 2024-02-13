import unittest
import pandas as pd
from FileOperation import FileOperation


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.file_op = FileOperation(data=None)

    def test_read_excel(self):
        file_path = "YafeNof.csv"
        self.file_op.read_excel(file_path)
        self.assertIsInstance(self.file_op.data, pd.DataFrame)


if __name__ == '__main__':
    unittest.main()
