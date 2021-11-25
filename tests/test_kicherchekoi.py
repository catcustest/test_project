FIRST_DATA_SEARCH = "mario kart"
SECOND_DATA_SEARCH = "mariokart64"
LOCATION_DATA = "75018"


def test_check_positive_search_result(kicherchekoi_home_page):
    kicherchekoi_home_page.main_search_button.click()
    kicherchekoi_home_page.search_field.set(FIRST_DATA_SEARCH)
    kicherchekoi_home_page.search_button.click()
    assert kicherchekoi_home_page.is_result_message_visible()


def test_check_negative_search_result(kicherchekoi_home_page):
    kicherchekoi_home_page.main_search_button.click()
    kicherchekoi_home_page.search_field.set(SECOND_DATA_SEARCH)
    kicherchekoi_home_page.category_selector.click()
    kicherchekoi_home_page.category.click()
    kicherchekoi_home_page.title_only_checkbox.click()
    kicherchekoi_home_page.location_input_field.set(LOCATION_DATA)
    kicherchekoi_home_page.search_button.click()
    assert kicherchekoi_home_page.is_no_result_message_visible()
