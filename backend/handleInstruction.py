#This file will allow users to input a certain task, and have AI automate the process for them
from playwright.sync_api import sync_playwright, TimeoutError
import json,os
import re
#will handle task handling
class Task:
    #class constructor
    def __init__(self):
        self.browser = None
        self.page = None
        self.playwright = None
        self.url = None
        try:
            self.playwright = sync_playwright().start()
            self.browser = self.playwright.chromium.launch(headless=False, slow_mo=5000)
            self.page = self.browser.new_page()
        except(Exception, TimeoutError) as e:
            print("An error occurred", e)
                
    def go_page(self, url):
        try:
            if self.page:
                self.page.goto(url, timeout = 12000, wait_until="networkidle")
                self.page.reload()
                return True
            raise Exception("Page not initiated")
        except (Exception, TimeoutError) as e:
            print("An error occurred", e)
            return False
            
    def fill_form(self, formName, inputData):
        try:
            if self.page:
                self.page.get_by_role('textbox',name=formName).fill(inputData)
                return True
            raise Exception("Page not initiated")
        except (Exception,TimeoutError) as e:
            print("An error occurred",e)
            return False
    def click_button(self, buttonName):
        try:
            if self.page:
                self.page.get_by_role("button",name=buttonName).click()
                return True
            raise Exception("Page not initiated")
        except (Exception, TimeoutError) as e:
            print("An error occurred", e)
            
            return False
    def page_locate_price(self):
        try:
            if self.page:
                self.url = self.page.url
                price = self.page.content()
                price = re.search(r'\$[0-9]+\.[0-9]+', price)
                print(price.group())
                return price.group()
            raise Exception("Page not initiated")
        except (Exception, TimeoutError) as e:
            print("An error occurred", e)
            return "Error finding price"

    def select_form(self,formName,selectValue):
        try:
            if self.page:
                self.page.get_by_role("combobox",name=formName).select_option(selectValue)
                return True
            raise Exception("Page not initiated")
        except (Exception, TimeoutError) as e:
            print("An error occurred", e)
            return False

    def handle_instruction(self, instruction,formName):
        try:
            if instruction["type"] == "go_page":
                val =self.go_page(instruction["url"])
            elif instruction["type"] == "fill_form":
                val = self.fill_form( formName, instruction["inputData"])
            elif instruction["type"] == "click_button":
                val = self.click_button(formName)
            else:
                raise Exception("Invalid instruction type")

            if val == False:
                raise Exception(f"Instruction failed: {instruction}")
        except(Exception,TimeoutError) as e:
            print("An error occurred", e)
    def refresh(self) -> None:
        self.page.reload()
    @property
    def is_ready(self):
        return self.playwright and self.browser and self.page
    @property
    def click_first(self):
        self.page.locator("h2 a, a.a-link-normal.s-no-outline, a[href*='/dp/']").first.click()

    def close(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()

def execute_instructions(search_type):
    try:
        task = Task()
        task.go_page(f"http://amazon.com/s?k={search_type}")
        task.select_form("Sort By", "Price: Low to High")
        task.click_first
        price = task.page_locate_price()
        url = task.url
        task.close()
        return {"success": True, "result": "Form filled successfully","price": price,"url": task.url}
    except(Exception,TimeoutError) as e:
        print("An error occurred", e)

def main():
    execute_instructions("blue_shirt")

if __name__ == "__main__":
    main()

