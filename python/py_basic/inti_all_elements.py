# The __post_init__ method is a special method in dataclasses that is automatically called after the instance is initialized. 
# In this case, it is used to initialize any elements in the instance that are set to None with a default value. 
# It calls a function init_all_elements(self) to accomplish this.

# In this example, the init_all_elements function loops through the attributes of an object and checks if any of them are None. 
# If an attribute is None, it sets the attribute's value to a default value (in this case, "Default").

# When the Compiler instance is created, the __post_init__ method is automatically called, 
# which in turn calls the init_all_elements function to initialize any attributes that are None with the default value.


from dataclasses import dataclass
from typing import Dict

def init_all_elements(obj):
    """Initialize all elements with default value"""
    for attr_name, attr_value in obj.__dict__.items():
        if attr_value is None:
            setattr(obj, attr_name, "Default")

@dataclass
class Compiler:
    """Contains configuration about the replaced compiler"""

    name: str
    configure_command: str
    file_to_copy: str
    env_vars: Dict

    def __post_init__(self):
        """Init all elements which are NONE with default value"""
        init_all_elements(self)


# Create an instance of the Compiler class
compiler = Compiler(name="GCC", configure_command=None, file_to_copy="gcc.exe", env_vars={"OPTIMIZE": "True"})
# here the configure_command value is None , it will take default value from init_all_elements

# Print the instance
print(compiler)
