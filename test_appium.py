import logging
import allure
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestAppium:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["noReset"] = "true"
        caps['skipDeviceInitialization'] = "true"
        caps["settings[waitForIdleTimeout]"] = 0
        caps['unicodeKeyBoard'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)
        logging.info('连接客户端，创建隐式等待')

    def teardomn(self):
        self.drive.quit()

    def test_appuim(self):
        with allure.step("进入通讯录列表"):
            self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        logging.info('进入通讯录列表')
        # 滚动查找
        with allure.step("滚动查找添加成员按钮"):
            logging.info("开始添加成员")
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                     'new UiScrollable(new UiSelector().scrollable(true).\
                                     instance(0)).scrollIntoView(new UiSelector().\
                                     text("添加成员").instance(0));').click()
        with allure.step("进入添加成员页面"):
            self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        with allure.step("输入姓名、手机号"):
            self.driver.find_element_by_xpath(
                '//*[@text="姓名　"]/../*[@resource-id="com.tencent.wework:id/b09"]').send_keys('小小')
            self.driver.find_element_by_xpath(
                '//*[@text="手机　"]/..//*[@resource-id="com.tencent.wework:id/f7y"]').send_keys('18733501234')
        with allure.step("点击保存按钮"):
            self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()
        with allure.step("获取添加成功提示语并截图"):
            text1 = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"添加成功")]').text
            self.driver.save_screenshot('a.png')
            allure.attach.file("a.png", attachment_type=allure.attachment_type.PNG, name="添加成功截图")
        with allure.step("断言"):
            assert text1 == "保存成功"
            logging.info("添加联系人成功")
