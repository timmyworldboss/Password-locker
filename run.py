#!/usr/bin/env python3.8
from users import Users
from cridentials import Cridentials


def create_acc(fname,sname,username,password):
  users = Users(fname,sname,username,password)
  return users


def new_acc(users):
  users.new_acc()

def del_acc(users):
  users.del_acc()

def find_acc(username):
  return Users.find_by_username(username)

def exist_acc(username):
  return Users.user_exists(username)

def display_users(username):
  return Users.display_users()

def create_site(site,password):
  passwords = Cridentials(site,password)
  return passwords

def save_site(passwords):
  passwords.save_site()

def find_site(page):
  return Cridentials.find_by_site(page)

def site_exists(page):
  return Cridentials.site_exists(page)

def delete_site(self,passwords):
  passwords.delete_site(self)

def display_site():
  return Cridentials.diplay_site()
 
def main():
  print('WELCOME TO PASSWORD_LOCKER. What is your name?')
  user_name = input()
  print(f"Hello {user_name}. What would you like to do?")
  print('\n')

  while True:
    
    print("1.LOGIN \n 2.SIGNUP \n 3.About Password_Locker \n 4.Display User Accounts \n 5.Sign Out")

    pick = int(input())
    if pick == 1:
        print('Enter username')
        username = input()
        print('Enter password')
        password = input()
        users = find_acc(username)
        if users.username == username and users.password == password:

          print("you're in")
          while True:

            print(f"Welcome {username},what's next")
            print('a.Save a password \n b.Delete password \n c.Display saved passwords \n d.LogOut')

            choice = str(input())
            if choice == 'a':
              print('New save')
              print('*'*100)

              print('Site Name')
              site = input()

              print('password')
              password = input()

            #new site password created
              save_site(create_site(site,password))

            elif choice == 'b':
              print('Name of site to delete password')

              site = input()
              if site_exists(site):
                remove_site = (site)
                delete_site(remove_site)

              else:
                print(f'{site} not found')

            elif choice == 'c':
              if display_site():
                for sit in display_site():
                  print(f'{sit.site} : {sit.password}') 

              else:
                print('No passwords saved yet')
                print('\n')

            elif choice == 'd':
              print('Logged Out')
              break
        else:
          print('wrong cridentials')   

    if pick == 2:
      print('New User')
      print('*'*100)

      print('First Name')
      fname = input()

      print('Last Name')
      sname = input()

      print('Username')
      username = input()

      print('Password')
      password = input()

      new_acc(create_acc(fname,sname,username,password))  
      #create and save new user account
      print('Account created')
      while True:

        print(f"Welcome {username},next step ?")
        print('a.Save a password \n b.Delete password \n c.Display saved passwords \n d.LogOut')

        choice = str(input())
        if choice == 'a':
          print('New save')
          print('*'*100)

          print('Site name')
          site = input()

          print('password')
          password = input()

          #create and save site
          save_site(create_site(site, password))

        elif choice == 'b':
          print('Name of site to delete password')

          page = input()
          if site_exists(page):
            return delete_site(page)
            # page.delete_site(page)
            # page = (site)
            # # breakpoint()
            # delete_site(self,page)
          else:
            print(f'{page} not found')

        elif choice == 'c':
          if display_site():
            for sit in display_site():
              print(f'{sit.site} : {sit.password}')
          else:
            print('No passwords saved yet')

        elif choice == 'd':
          break
    elif pick == 3:
      print('About PASSWORD_LOCKER')
      print(
        '''
          No need to stress yourself trying to remember passwords to every website you sign up for a site, 
          Password Locker has got you covered. All you need is to create a locker account and save all your cridentials inside.
        ''' )

    elif pick == 4:
      if display_users(username):
        for acc in display_users(username):
          print(f'{acc.username}')
      else:
        print('No accounts yet')

    elif pick == 5:
      print('come back again soon')
      break

if __name__ == '__main__':
  main()