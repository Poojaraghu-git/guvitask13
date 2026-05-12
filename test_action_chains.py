from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def test_drag_white_rectangular_box_and_drop_yellow_rectangular_box_scenario(driver):
    #open url
    driver.get("https://jqueryui.com/droppable/")
    #switch to iframe
    iframe = driver.find_element(By.XPATH, "//iframe[@class ='demo-frame']")
    driver.switch_to.frame(iframe)
    #create drag and drop object
    drag_object = driver.find_element(By.XPATH,"//p[text() = 'Drag me to my target']")
    drop_object = driver.find_element(By.XPATH,"//div[@id ='droppable']")
    #Preform drag and drop action
    actions = ActionChains(driver)
    actions.drag_and_drop(drag_object, drop_object).perform()
    after_drop = driver.find_element(By.XPATH, "//div[@id='droppable']").text
    #validate whether the drop was success
    if after_drop == "Dropped!":
        print("Dropped successfully")
    else:
        print("Not dropped")

def test_drag_white_rectangular_box_and_drop_yellow_rectangular_box_scenario_without_drag_and_drop_function(driver):
    #open url
    driver.get("https://jqueryui.com/droppable/")
    #switch to iframe
    iframe = driver.find_element(By.XPATH, "//iframe[@class ='demo-frame']")
    driver.switch_to.frame(iframe)
    #create drag and drop object
    drag_object = driver.find_element(By.XPATH,"//p[text() = 'Drag me to my target']")
    drop_object = driver.find_element(By.XPATH,"//div[@id ='droppable']")
    #Preform drag and drop action without drag and drop functionality
    actions = ActionChains(driver)
    actions.click_and_hold(drag_object).perform()
    actions.move_to_element(drop_object).perform()

    actions.release().perform()

    after_drop = driver.find_element(By.XPATH, "//div[@id='droppable']").text
    #validate whether the drop was success
    if after_drop == "Dropped!":
        print("Dropped successfully")
    else:
        print("Not dropped")


