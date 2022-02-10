class User:
  def __init__(self, name, user_name, email):
    self.name = name
    self.user_name = user_name
    self.email = email
  def get_name(self):
    return self.name
  def get_email(self):
    return self.email
  def get_info(self, age):
    print(f"Ismim: {self.name}\UserName: {self.user_name}\
    Yoshim: {age}")
user1 = User('Sevinch', 'Sevgilim', 'sevgi')
(user1.get_info(16))
