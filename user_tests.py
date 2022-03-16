from users import Users
import unittest

class TestUsers(unittest.TestCase):
  def tearDown(self):
      Users.user_info = []

  def setUp(self):
    '''
    runs before every test occurs
    '''
    self.new_user = Users('Timothy','Ndungu','user014','3000')

  def test_init(self):
    '''
    test case to test if object properly initialized
    '''
    self.assertEqual(self.new_user.fname,'Timothy')
    self.assertEqual(self.new_user.sname,'Ndungu')
    self.assertEqual(self.new_user.username,'user014')
    self.assertEqual(self.new_user.password,'3000')

  def test_new_acc(self):
    '''
    test to see if an account is added
    '''
    self.new_user.new_acc()
    test_user = Users('Timothy','Ndungu','user014','3000')
    test_user.new_acc()
    self.assertEqual(len(Users.user_info),2)

  def test_del_acc(self):
    '''
    test delete account function
    '''
    self.new_user.new_acc()
    test_user = Users('Timothy','Ndungu','user014','3000')
    test_user.new_acc()
    self.new_user.del_acc()
    self.assertEqual(len(Users.user_info),1)

  def test_find_by_username(self):
    '''
    test find user function
    '''
    self.new_user.new_acc()
    test_user = Users('Timothy','Ndungu','user014','3000')
    test_user.new_acc()
    find_user = Users.find_by_username('user014')
    self.assertEqual(find_user.username, test_user.username)

  def test_user_exists(self):
    '''
    test user exists function
    '''
    self.new_user.new_acc()
    test_user = Users('Timothy','Ndungu','user014','3000')
    test_user.new_acc()
    user_exists = Users.user_exists('user014')
    self.assertTrue(user_exists)

  def test_display_users(self):
    '''
    test display function
    '''
    self.assertEqual(Users.display_users(),Users.user_info)


if __name__ == '__main__':
  unittest.main()