

class ListToBool:

    def __init__(self):
        self.hit_list = list

    def list_checker(self, hit_list: list) -> bool:
        """
            Check if the list has elements
        @args:
            hit_list [list] - the list to be checked
        @return:
            True [bool] - if the list has elements
            False [bool] - if the list has no element
        """
        self.hit_list = hit_list
        if len(self.hit_list) > 0:
            return True
        else:
            return False
