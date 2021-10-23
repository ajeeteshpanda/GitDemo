from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        phoneName = "Samsung Note 8"

        log = self.getLogger()

        homePage = HomePage(self.driver)

        checkOutPage = homePage.shopItems()

        num = len(checkOutPage.getCardTitles())
        log.info(f'Total number of mobiles displayed is {num}')

        for i in range(num):
            mobileName = checkOutPage.getCardTitles().__getitem__(i).text
            log.info(mobileName)

            if mobileName == phoneName:
                checkOutPage.getCardFooters().__getitem__(i).click()
                break

        checkOutPage.gotoCheckOut().click()

        confirmPage = checkOutPage.CheckOut()

        confirmPage.countryname().send_keys("ind")

        self.verifyLinkPresence("India")

        # wait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "suggestions")))

        self.driver.find_element_by_xpath("//div[@class='suggestions']/ul/li/a[contains(text(), 'India')]").click()

        confirmPage.checkbox().click()

        confirmPage.buy().click()

        msg = self.driver.find_element_by_css_selector("div.alert-success").text
        log.info("Final message in confirm page: " + msg)

        assert "Success" in msg
