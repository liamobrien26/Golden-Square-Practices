# {{PROBLEM}} Class Design Recipe

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class MyTask():

    def __init__(self):
    # Parameters: 
    #task: list
        self.task = []
        pass

    def add_to_do(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        pass

    def see_list_of_tasks(self,task):
        pass

    def complete_task(self,task):
        #Remove task from list

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a task
#add task to lsit
"""
gettingClass = Mytask()
gettingClass.add_to_do("Clean bedroom")
reminder.remind() # => "Clean bedroom"

"""
Given tasks
#Display lists of tasks
"""
gettingClass = Mytask()
gettingClass.add_to_do("Clean bedroom")
gettingClass.add_to_do("Walk dog")
gettingClass.add_to_do("Cook dinner")
gettingClass.see_list_of_tasks() # => "Clean bedroom","Walk dog", "Cook dinner"


"""
Given task and task completed
#Removes task from list 
"""
gettingClass = Mytask()
gettingClass.add_to_do("Clean bedroom")
gettingClass.add_to_do("Walk dog")
gettingClass.complete_task("Walk dog") #=> "Clean bedroom"


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
