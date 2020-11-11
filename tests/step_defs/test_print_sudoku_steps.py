from pytest_bdd import scenario, given, when, then
from pytest_bdd.parsers import cfparse




@given(cfparse('the {basket} has {2} cucumbers'))
def step_function(, basket, 2):
    # Add Your Code Here
    pass