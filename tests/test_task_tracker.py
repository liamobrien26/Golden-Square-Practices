from lib.task_tracker import *

def test_add_to_list():
    gettingClass = MyTask()
    gettingClass.add_to_do("Clean bedroom")
    assert gettingClass.tasks == ["Clean bedroom"]

def test_add_multi_tasks_to_list():
    gettingClass = MyTask()
    gettingClass.add_to_do("Clean bedroom")
    gettingClass.add_to_do("Walk dog")
    assert gettingClass.see_list_of_tasks() == ["Clean bedroom", "Walk dog"]

def test_complete_task_and_remove():
    gettingClass = MyTask()
    gettingClass.add_to_do("Clean bedroom")
    gettingClass.add_to_do("Walk dog")
    gettingClass.complete_task("Walk dog")
    assert gettingClass.see_list_of_tasks() == ["Clean bedroom"]

