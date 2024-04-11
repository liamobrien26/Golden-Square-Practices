class MyTask():
    def __init__(self):
        self.tasks = []

    def add_to_do(self,task):
        self.tasks.append(task)
    
    def see_list_of_tasks(self):
        return self.tasks
    
    def complete_task(self,task):
        self.tasks.remove(task)
