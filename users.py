class Users:
  def __init__(self,fname,sname,username,password):
    self.fname = fname
    self.sname = sname
    self.username = username
    self.password = password

  user_info = []

  def new_acc(self):
    '''
    add an account to the list
    '''
    Users.user_info.append(self)

  def del_acc(self):
    '''
    delete an account
    '''
    Users.user_info.remove(self)

  
  @classmethod
  def find_by_username(cls,username):
    '''
    args:username to search for
    returns:user account that matches username
    '''
    for user in cls.user_info:
      if user.username == username:
        return user

  @classmethod
  def user_exists(cls,username):
    '''
    loop through list to check if username exists then return boolean
    '''  
    for user in cls.user_info:
      if user.username == username:
        return True
      
      return False

  @classmethod
  def display_users(cls):
    '''
    show all user accounts
    '''
    return cls.user_info
