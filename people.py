"""
We'll try to understand classes in python. 
Check the resources on google classroom to ensure you have gone through everything expected.

"""
###### THESE LISTS HAVE ALREADY BEEN DEFINED FOR YOU ###############
engineer_roster = [] # A list of all instantiated engineer objects
sales_roster = [] # List of all instantiated sales objects
branchmap = {  # A dictionary of dictionaries -> Maps branchcodes to cities and branch names
    0:  { "city": "NYC", "name": "Hudson Yards"},
    1:  { "city": "NYC" , "name": "Silicon Alley"},
    2:  { "city": "Mumbai", "name": "BKC"},
    3:  { "city": "Tokyo", "name": "Shibuya"},
    4:  { "city": "Mumbai", "name": "Goregaon"},
    5:  { "city": "Mumbai", "name": "Fort"}
}
####################################################################

class Employee:
    name : str 
    age : int
    ID : int
    city : str # was int before
    branches : list[int] # This is a list of branches (as branch codes) to which the employee may report
    salary : int 

    def __init__(self, name, age, ID, city,\
                 branchcodes, salary = None):
        self.name = name
        self.age = age 
        self.ID = ID
        self.city = city
        self.branches = branchcodes
        if salary is not None: self.salary = salary
        else: self.salary = 10_000 
    
    def change_city(self, new_city:str) -> bool:
            if(new_city==self.city):
                return False
            else:
                self.city=new_city
                return True
       
        # Change the city 
        # Return true if city change, successful, return false if city same as old city
        

    def migrate_branch(self, new_code:int) -> bool:
        if(len(self.branches)>1):
            return False
        if(new_code==branchmap[self.branches[0]]['city']):
            branches=[new_code]
            return True
        # Should work only on those employees who have a single 
        # branch to report to. Fail for others.
        # Change old branch to new if it is in the same city, else return false.
        

    def increment(self, increment_amt: int) -> None:
        self.salary += increment_amt
        # Increment salary by amount specified.
        





class Engineer(Employee):
    position : str # Position in organization Hierarchy
    pos=["Junior", "Senior", "Team Lead", "Director" ]

    def __init__(self, name, age, ID, city,\
                 branchcodes, position= "Junior", salary = None):
        # Call the parent's constructor
        super().__init__(name, age, ID, city, branchcodes, salary)
        if position in self.pos:
                        self.position=position
        # Check if position is one of  "Junior", "Senior", "Team Lead", or "Director" 
        # Only then set the position. 

    
    def increment(self, amt:int) -> None:
        Employee.increment(int(1.1*amt))
        # While other functions are the same for and engineer,
        # and increment to an engineer's salary should add a 10% bonus on to "amt"
        
    def promote(self, position:str) -> bool:
        if ( self.pos.index(position) <= self.pos.index(self.position) ):
             return False
        else:
             self.position=position
             self.increment(int(0.3*self.salary))
        # Return false for a demotion or an invalid promotion
        # Promotion can only be to a higher position and
        # it should call the increment function with 30% of the present salary
        # as "amt". Thereafter return True.
        



class Salesman(Employee):
    """ 
    This class is to be entirely designed by you.

    Add increment (this time only a 5% bonus) and a promotion function
    This time the positions are: Rep -> Manager -> Head.

    Add an argument in init which tracks who is the superior
    that the employee reports to. This argument should be the ID of the superior
    It should be None for a "Head" and so, the argument should be optional in init.
    """

    pos=['Rep' , 'Manager' , 'Head']
    
    # An extra member variable!
    superior : int # EMPLOYEE ID of the superior this guy reports to
    position : str # was not given ... made by me
 
    def __init__(self,name, age, ID, city, branchcodes, salary,position="Rep" ,superior=-1): # Complete all this! Add arguments
        
        super().__init__(name, age, ID, city, branchcodes, salary)
        self.superior=superior
        if position in self.pos:
             self.position=position
        
    
    # def promote 
    def promote(self,position):
        #  c=0
        #  t=0
        #  while(t!=-1):
        #       t=-1
        #       Id=self.superior                    # code for finding position if position not given
        #       for s in sales_roster:
        #            if(s.ID==Id):
        #                 c+=1
        #                 t=s.ID
        #  self.position=self.pos[c]
        if ( self.pos.index(position) <= self.pos.index(self.position) ):
             return False
        else:
             self.position=position
             self.increment(int(0.05*self.salary))
            

    # def increment 
    def increment(self, increment_amt: int) -> None:
         return super().increment(increment_amt)

    def find_superior(self) -> tuple[int, str]:
        for s in sales_roster:
             if( s.ID == self.superior ):
                  return (s.ID,s.name)
        return (None,None)
        # Return the employee ID and name of the superior
        # Report a tuple of None, None if no superior.
        

    def add_superior(self,sup_id=-1) -> bool:
        for s in sales_roster:
             if (self.superior!=-1):
                  self.superior=sup_id
                  return True
        return False
        # Add superior of immediately higher rank.
        # If superior doesn't exist return false,
        


    def migrate_branch(self, new_code: int) -> bool:
        if(new_code<6):
             self.branches.append(new_code)
             return True
        return False

        # This should simply add a branch to the list; even different cities are fine
        
    





    
    
