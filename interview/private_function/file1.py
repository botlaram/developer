# file1.py

class one():

    def this_can_be_imported():
        print("this is from file1.py")

    def _this_should_not_be_imported():
        """This function is intended to be private by convention."""
        print("This should not be imported directly.")

obj1=one

if __name__ == "__main__":
    obj1.this_can_be_imported()
    obj1._this_should_not_be_imported()
