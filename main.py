from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://gradesresults.griet.in/results.php?result=GR18:2019-20:A:110:REGULAR:JANUARY')

File = open('ID.txt', 'r')
Lines = File.read().splitlines()
Output = open('CGPA.txt', 'w')

for line in Lines:
    driver.find_element_by_xpath('//*[@id="content"]/table[2]/tbody/tr[1]/td[3]/input').clear()
    driver.find_element_by_xpath('//*[@id="content"]/table[2]/tbody/tr[1]/td[3]/input').send_keys(line, Keys.ENTER)
    driver.switch_to.window(driver.window_handles[1])
    NAME = driver.find_element_by_xpath('/html/body/table[3]/tbody/tr[1]/td[3]')
    GPA = driver.find_element_by_xpath("/html/body/table[6]/tbody/tr/td[4]")
    string = (line + ' ' + NAME.text + ' ' + GPA.text + '\n')
    # print(line, ' ', NAME.text, ' ', GPA.text)
    Output.write(string)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
# driver.close()
