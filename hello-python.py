class HelloJenkins:

   def __init__(self, msg: str) -> None:
      self.msg = msg

   def greet_jenkins(self) -> None:
      print(f"{self.msg}! Have a good time automating my builds :)")

if __name__ == "__main__":
   
   jenkins_obj = HelloJenkins("Hello Jenkins")
   jenkins_obj.greet_jenkins()