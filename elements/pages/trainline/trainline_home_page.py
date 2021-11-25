from selene.bys import by_xpath
from selene.support.jquery_style_selectors import s


class TrainlineHomePage:

    def __init__(self):
        self.depart_field = s("input[id*='from.search']")
        self.arrive_field = s("input[id*='to.search']")
        self.calendar = s("input[name='page.journeySearchForm.outbound.title']")
        self.data_calendar = s("[data-test='2021-12-24'")
        self.submit_button = s("._1kmf9x23")
        self.accept_cookie_button = s("[id*='onetrust-accept-btn-handler']")
        self.cancel_button = s("._1mw23jrNaN")
        self.time_picker = s(by_xpath(
            "//div[2]/div/div[2]/main/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/section/form/div[3]/fieldset[1]/div[4]/div[1]/select"))
        self.time = s("option[value='16']")


class TrainlineSearchResultPage:

    def __init__(self):
        self.train_details_container = s("[class*='_1x7766d']")
        self.train_data = s("[data-test='eu-journey-row-0-first-class-ticket-container']")
