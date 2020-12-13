from pytest_bdd import scenario, given, when, then


@given('the basket has "2" cucumbers')
def step_impl():
    raise NotImplementedError(u'STEP: Given the basket has "2" cucumbers')


@when('"4" cucumbers are added to the basket')
def step_impl():
    raise NotImplementedError(u'STEP: When "4" cucumbers are added to the basket')


@then('the basket contains "6" cucumbers')
def step_impl():
    raise NotImplementedError(u'STEP: Then the basket contains "6" cucumbers')


@when('"3" cucumbers are removed from the basket')
def step_impl():
    raise NotImplementedError(u'STEP: When "3" cucumbers are removed from the basket')