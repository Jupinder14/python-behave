from behave import given, then, when
import utils.urls as urls

@given('I am on carbohydrate calculator page')
def on_page(context):
    context.driver.get(urls.urls['carbohydrate_calculator'])

@when('I enter {age} in age')
def enter_age(context, age):
    context.calculator.input_age(context.driver, age)

@when('I select gender {gender}')
def select_gender(context, gender):
    context.calculator.select_gender(context.driver, gender)

@when('I enter {height} in height')
def enter_height(context, height):
    context.calculator.input_height(context.driver, height)

@when('I enter {weight} in weight')
def enter_weight(context, weight):
    context.calculator.input_weight(context.driver, weight)

@when('I select {activity_type} exercise')
def select_activity(context, activity_type):
    context.calculator.select_activity(context.driver, activity_type)

@when('I click calculate')
def click_calculate(context):
    context.calculator.click_calculate_button(context.driver)

@then('I see results')
def see_results(context):
    visible = context.calculator.check_results_visible(context.driver)
    assert visible == True

@then('I verify results are accurate')
def verify_results(context):
    expected_table_data = {
        'Weight Maintenance': ['2,879 Calories', '307 grams', '422 grams', '499 grams', '576 grams'],
        'Lose 0.5 kg/week': ['2,379 Calories', '254 grams', '349 grams', '412 grams', '476 grams'],
        'Lose 1 kg/week': ['1,879 Calories', '200 grams', '276 grams', '326 grams', '376 grams'],
        'Gain 0.5 kg/week': ['3,379 Calories', '360 grams', '496 grams', '586 grams', '676 grams'],
        'Gain 1 kg/week': ['3,879 Calories', '414 grams', '569 grams', '672 grams', '776 grams']
    }
    table_data = context.calculator.get_result(context.driver)

    assert expected_table_data == table_data
