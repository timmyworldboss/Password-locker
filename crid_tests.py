from cridentials import Cridentials
import unittest


class TestCridentials(unittest.TestCase):
  def tearDown(self):
    '''
    clears user passwords before every test
    '''
    Cridentials.user_passwords = []

  def setUp(self):
    '''
    creates new instance of passwords class before every test
    '''
    self.new_password = Cridentials('betika','12211')

  def test_init(self):
    '''
    tests whether data entered can be returned
    '''
    self.assertEqual(self.new_password.site,'betika')
    self.assertEqual(self.new_password.password,'12211')
  
  def test_save_site(self):
    '''
    check whether value is added to passwords list
    '''
    self.new_password.save_site()
    self.assertEqual(len(Cridentials.user_passwords),1)

  def test_save_multiple(self):
    '''
    check addition of many passwords
    '''
    self.new_password.save_site()
    test_pass = Cridentials('betika','12211')
    test_pass.save_site()
    self.assertEqual(len(Cridentials.user_passwords),2)

  def test_delete_site(self):
    '''
    check if password can be deleted
    '''
    self.new_password.save_site()
    test_pass = Cridentials('betika','12211')
    test_pass.save_site()
    self.new_password.delete_site()
    self.assertEqual(len(Cridentials.user_passwords),1)

  def test_display_site(self):
    self.assertEqual(Cridentials.diplay_site(),Cridentials.user_passwords)

  def test_find_by_site(self):
    '''
    test to check if saved site pwd can be searched
    '''
    self.new_password.save_site()
    test_pass = Cridentials('betika','12211')
    test_pass.save_site()
    site_exists = Cridentials.site_exists('betika')
    self.assertTrue(site_exists)


if __name__ == '__main__':
  unittest.main()
  