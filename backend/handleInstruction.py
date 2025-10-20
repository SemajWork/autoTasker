#This file will allow users to input a certain task, and have AI automate the process for them
from playwright.sync_api import sync_playwright, TimeoutError
from aiInterpreter import interpret_instruction 
#will handle task handling
class Task:
    #class constructor
    def __init__(self):
        self.browser = None
        self.page = None
        self.playwright = None
        try:
            self.playwright = sync_playwright().start()
            self.browser = self.playwright.chromium.launch(headless=False, slow_mo=1000)
            self.page = self.browser.new_page()
        except(Exception, TimeoutError) as e:
            print("An error occurred", e)
                
    def go_page(self, url):
        try:
            if self.page:
                self.page.goto(url, timeout = 12000, wait_until="networkidle")
                return True
            raise Exception("Page not initiated")
        except (Exception, TimeoutError) as e:
            print("An error occurred", e)
            return False
            
    def fill_form(self, formType, formName, inputData):
        try:
            if self.page:
                self.page.get_by_role(formType,name=formName).fill(inputData)
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
    def get_value(self, typeName):
        try:
            if self.page:
                price = self.page.get_by_role("text",name=typeName).text_content()
                return price
            raise Exception(f"{typeName} not found!")
        except (Exception, TimeoutError) as e:
            print("An error occurred", e)
            return False
    def handle_instruction(self, instruction):
        try:
            if instruction["type"] == "go_page":
                self.go_page(instruction["url"])
            elif instruction["type"] == "fill_form":
                self.fill_form(instruction["formType"], instruction["formName"], instruction["inputData"])
            elif instruction["type"] == "click_button":
                self.click_button(instruction["buttonName"])
            else:
                raise("Invalid instruction type")
        except(Exception,TimeoutError) as e:
            print("An error occurred", e)
           
    @property
    def is_ready(self):
        return self.playwright and self.browser and self.page
    
    def close(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()

def execute_instructions(instructions):
    try:
        task = Task()
        if task.is_ready:
            for instruction in instructions:
                task.handle_instruction(instruction)    
        task.close()
        return {"success": True, "result": "Instructions done"}
    except(Exception,TimeoutError) as e:
        print("An error occurred", e)

def main():
    instruction = "help me login into wellsfargo workday account, my email is jamesma765@gmail.com, and password is Dugong05!"
    instructions = interpret_instruction(instruction)
    execute_instructions(instructions)

if __name__ == "__main__":
    main()

