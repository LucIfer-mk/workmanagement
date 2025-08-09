import unittest
from staff import add_staff, view_staff, update_staff, delete_staff
from login import login
from database import connect_to_database

class TestWorkManagement(unittest.TestCase):
    def setUp(self):
        self.conn = connect_to_database()

    def test_add_staff(self):
        result = add_staff(self.conn, "Test User", "Address", "2000-01-01", "12345")
        self.assertTrue(result)

    def test_view_staff(self):
        staff_list = view_staff(self.conn)
        self.assertIsInstance(staff_list, list)

    def test_update_staff(self):
        result = update_staff(self.conn, 1, "Updated Name", "Address", "2000-01-01", "12345")
        self.assertTrue(result)

    def test_delete_staff(self):
        result = delete_staff(self.conn, 1)
        self.assertTrue(result)

    def test_login(self):
        result = login(self.conn, "admin", "password")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
