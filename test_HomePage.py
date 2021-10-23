import pytest
import inspect
import logging

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    loggername = inspect.stack()[1][3]
    logger = logging.getLogger(loggername)
    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  # Filehandler object

    logger.setLevel(logging.INFO)
    log = logger

    def test_formSubmission(self, getData):
        homepage = HomePage(self.driver)
        self.log.info("First name is: " + getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        self.log.info("Email is: " + getData["email"])
        homepage.getEmail().send_keys(getData["email"])
        homepage.getCheckBox().click()
        self.log.info("Gender selected is: " + getData["gender"])
        self.selectOptionByText(homepage.getGender(), getData["gender"])
        homepage.getSubmit().click()
        print("Changes made here part 4")

        alertText = homepage.getSuccessMessage().text
        self.log.info("Message displayed is: " + alertText)
        assert "Success" in alertText

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData())
    def getData(self, request):
        return request.param


