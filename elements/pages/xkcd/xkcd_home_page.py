from selene.conditions import visible
from selene.support.jquery_style_selectors import s

from elements.utils import verify_objects_not_equal


class HomePage:

    def __init__(self):
        self.img_logo = s("img[alt='xkcd.com logo']")
        self.random_button = s(".comicNav li:nth-of-type(3)")
        self.picture = s("div#comic img")
        self.previous_button = s(".comicNav li a[rel='prev']")

    def check_logo(self):
        self.img_logo.assure(visible)

    def check_picture_is_changed(self, pict, new_pict):
        verify_objects_not_equal(pict, new_pict)
