from elements.utils import convert_str_to_lst, verify_objects_are_equal

PARIS = "Paris"
ANGERS = "Angers"
DEPARTURE_TIME = "16:35"
DEPARTURE_STATION = "Paris Montparnasse"
ARRIVAL_STATION = "Angers St-Laud"
ARRIVAL_TIME = "18:11"


def test_check_train_displayed_in_search_result(trainline_home_page, trainline_train_details_page, browser):
    trainline_home_page.accept_cookie_button.click()
    trainline_home_page.cancel_button.click()
    trainline_home_page.depart_field.set(PARIS)
    trainline_home_page.arrive_field.set(ANGERS)
    browser.execute_script("arguments[0].click();", trainline_home_page.calendar.get_actual_webelement())
    trainline_home_page.data_calendar.click()
    browser.execute_script("arguments[0].click();", trainline_home_page.time_picker.get_actual_webelement())
    trainline_home_page.time.click()
    trainline_home_page.submit_button.click()
    trainline_train_details_page.train_data.click()
    train_details = trainline_train_details_page.train_details_container.text
    lst_train_data = convert_str_to_lst(train_details)
    verify_objects_are_equal(lst_train_data[0], DEPARTURE_TIME)
    verify_objects_are_equal(lst_train_data[1], DEPARTURE_STATION)
    verify_objects_are_equal(lst_train_data[4], ARRIVAL_TIME)
    verify_objects_are_equal(lst_train_data[5], ARRIVAL_STATION)
