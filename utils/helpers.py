from selenium.webdriver import ActionChains, Keys


def scroll_to_element(driver, element, speed=50):
    """
    Scroll the page to the given element with a certain speed.

    :param driver: The WebDriver instance to use.
    :param element: The WebElement to scroll to.
    :param speed: The speed of the scrolling action. Default is 50.
    """
    action = ActionChains(driver)
    action.move_to_element(element)

    # Calculate the number of scrolls based on the distance between the current position and the element.
    current_pos = driver.execute_script("return window.pageYOffset;")
    target_pos = element.location['y'] - 200  # Adjust for header/footer
    distance = target_pos - current_pos
    num_scrolls = abs(int(distance / speed))

    # Scroll to the element.
    for i in range(num_scrolls):
        action.send_keys(Keys.PAGE_DOWN)
        action.perform()


def hover_to_element(driver, element):
    hover = ActionChains(driver).move_to_element(element)
    hover.perform()
    driver.implicity_wait(5)
