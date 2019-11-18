


"""==== Part 2 ==="""

from typing import Iterator


filepath = 'path/to/employees.txt'


class Employee:
    """Class to hold employee data fields."""
    def __init__(self, name: str, title: str, employee_id: int):
        self.name = name
        self.title = title
        self.employee_id = employee_id



def employees_from_file(filepath) -> Iterator[dict]:
    """Read data from text file in chunks and yield generator object."""
    with open(filepath, 'r') as source:
        keep_going = True
        while keep_going is True:
            line1 = source.readline().strip()  # Name
            line2 = source.readline().strip()  # Title
            line3 = source.readline().strip()  # ID Number
            line4 = source.readline().strip()  # Blank line
            if line1 == '' and line2 == '' and line3 == '':
                keep_going = False
                break

            yield {
                'name': line1,
                'title': line2,
                'employee_id': line3
            }


def get_employee_instances(filepath):
    """Create list of employee data fields."""
    employee_list = []
    for empl_dict in employees_from_file(filepath):
        employee = Employee(
            name=empl_dict['name'],
            title=empl_dict['title'],
            employee_id=empl_dict['employee_id'])
        employee_list.append(employee)
    return employee_list
    

employees = get_employee_instances(filepath)
assert(employees[0].name == 'Gilligan')
assert(employees[2].name == 'Howell, Thurston III')

