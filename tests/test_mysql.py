import unittest
import subprocess

class TestDatabaseSetup(unittest.TestCase):
    def setUp(self):
        # Define the SQL file paths
        self.mysql_dev_setup_file = 'setup_mysql_dev.sql'
        self.mysql_test_setup_file = 'setup_mysql_test.sql'

    def test_mysql_dev_setup(self):
        # Execute the MySQL dev setup SQL script
        result = subprocess.run(
            ['mysql', '--user=root', '--password=root_pwd', '--host=localhost', 'hbnb_dev_db'],
            stdin=open(self.mysql_dev_setup_file, 'rb'),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        self.assertEqual(result.returncode, 0, f"Error executing {self.mysql_dev_setup_file}: {result.stderr}")

    def test_mysql_test_setup(self):
        # Execute the MySQL test setup SQL script
        result = subprocess.run(
            ['mysql', '--user=root', '--password=root_pwd', '--host=localhost', 'hbnb_test_db'],
            stdin=open(self.mysql_test_setup_file, 'rb'),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        self.assertEqual(result.returncode, 0, f"Error executing {self.mysql_test_setup_file}: {result.stderr}")

if __name__ == '__main__':
    unittest.main()
