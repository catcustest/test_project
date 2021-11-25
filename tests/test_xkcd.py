def test_check_homepage_displayed(xkcd_home_page):
    xkcd_home_page.check_logo()


def test_check_random_picture_displayed(xkcd_home_page):
    pict_id = xkcd_home_page.picture.id
    xkcd_home_page.random_button.click()
    new_pict_id = xkcd_home_page.picture.id
    xkcd_home_page.check_picture_is_changed(pict_id, new_pict_id)


def test_check_favuirite_picture_displayed(xkcd_home_page):
    pict_id = xkcd_home_page.picture.id
    xkcd_home_page.previous_button.click()
    favourite_picture = xkcd_home_page.picture.id
    xkcd_home_page.check_picture_is_changed(pict_id, favourite_picture)
