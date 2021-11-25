from selene.bys import by_xpath
from selene.conditions import visible
from selene.support.jquery_style_selectors import s


class KicherchekoiHomePage:

    def __init__(self):
        self.main_search_button = s("[id*=btn-home-main-search]")
        self.search_field = s("[id*=search_q]")
        self.category_selector = s("[id*=category-select]")
        self.category = s(by_xpath("//*[@id='second-navbar']/div[2]/div/div[1]/ul[1]/li[2]"))
        self.title_only_checkbox = s("[id*=titleonly]")
        self.location_input_field = s(".input-group search-location, input[name='location']")
        self.search_button = s("[id*='search-form'] button[type='submit']")
        self.result = s("[id*=jeux-et-accessoires-pour-console-wii")
        self.no_result = s("[class*='search-no-result-message box']")

    def is_result_message_visible(self):
        self.result.assure(visible)

    def is_no_result_message_visible(self):
        self.no_result.assure(visible)
