import django
django.setup()

from core.models import Owner

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.keys import Keys
import time
import subprocess
from subprocess import STDOUT, check_call
import traceback
import os


class Test:
    url = 'http://127.0.0.1:8000'
    webdriver_path = 'tests/chromedriver.exe'
    driver = ''
    process = ''

    def start_django_app(self):
        try:
            self.driver = webdriver.Chrome(self.webdriver_path)
            self.process = subprocess.Popen(['python', r'manage.py', 'runserver', '--insecure'])
            print('STARTING DJANGO                                  INITIALIZED')
            time.sleep(8)
        except Exception as e:
            print('START DJANGO                                     FAILED')
            print('DETAILS: ' + str(traceback.format_exc()))

    def page_authentication(self):
        self.driver.get(self.url)
        assert 'Login' in self.driver.title
        title = self.driver.find_element_by_id('title').text
        if 'CONDOMÍNIO TITÂNIA' == title:
            print('PAGE                                            AUTHENTICATED')

    def wait_for_ajax(self):
        wait = WebDriverWait(self.driver, 15)
        try:
            wait.until(lambda driver: self.driver.execute_script('return jQuery.active') == 0)
            wait.until(lambda driver: self.driver.execute_script('return document.readyState') == 'complete')
        except Exception as e:
            pass

    def login(self):
        try:
            self.driver.find_element_by_id('login').click()
            self.wait_for_ajax()
            assert 'Titânia' in self.driver.title
            print('LOGIN                                            AUTHENTCATED')
        except Exception as e:
            print('LOGIN                                      FAILED')
            print('DETAILS: ' + str(traceback.format_exc()))

    def get_owners_list(self):
        try:
            self.driver.get(self.url + '/list/residents/')
            self.wait_for_ajax()
            tbody = self.driver.find_element_by_tag_name('tbody')
            if tbody.find_elements_by_tag_name('tr'):
                print('LIST OWNERS                                           PASSED')
            else:
                print('LIST OWNERS                                        FAILED')
            #time.sleep(5)
        except Exception as e:
            print('LIST OWNERS                                      FAILED')
            print('DETAILS: ' + str(traceback.format_exc()))

    def filter_owners(self):
        try:
            Select(self.driver.find_element_by_id('tower')).select_by_visible_text('1')
            self.wait_for_ajax()
            tbody = self.driver.find_element_by_tag_name('tbody')
            trs = tbody.find_elements_by_tag_name('tr')
            selected = Select(self.driver.find_element_by_id('tower')).first_selected_option.text
            failed = False
            for tr in trs:
                td = tr.find_elements_by_tag_name('td')
                towers_registers = Owner.objects.filter(tower__number=int(selected))
                if towers_registers:
                    if td[0].text != selected:
                        failed = True
                        break
                else:
                    print(td[0].text)
                    if td[0].text != 'Não foram encontrados registros':
                        failed = True
            if not failed:
                print('FILTER OWNERS                                      PASSED')
            else:
                print('FILTER OWNERS                                      FAILED')
        except Exception as e:
            print('FILTER OWNERS                                      FAILED')
            print('DETAILS: ' + str(traceback.format_exc()))

    def finish_tests(self):
        time.sleep(5)
        self.driver.close()
        os.system('taskkill /F /T /PID '+str(str(self.process.pid)))


test = Test()
test.start_django_app()
test.page_authentication()
test.login()
test.get_owners_list()
test.filter_owners()
test.finish_tests()
