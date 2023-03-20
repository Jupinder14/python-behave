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
        'Weight Maintenance': ['2,482 Calories', '265 grams', '364 grams', '430 grams', '496 grams'],
        'Lose 0.5 kg/week': ['1,982 Calories', '211 grams', '291 grams', '344 grams', '396 grams'],
        'Lose 1 kg/week': ['1,482 Calories', '158 grams', '217 grams', '257 grams', '296 grams'],
        'Gain 0.5 kg/week': ['2,982 Calories', '318 grams', '437 grams', '517 grams', '596 grams'],
        'Gain 1 kg/week': ['3,482 Calories', '371 grams', '511 grams', '604 grams', '696 grams']
    }
    table_data = context.calculator.get_result(context.driver)

    assert expected_table_data == table_data
