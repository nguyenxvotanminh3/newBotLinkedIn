import csv
from datetime import time, datetime
import pandas as pd


def join_group(driver):
    df = pd.read_csv(f'edited_{keyword}_linkedin_groups_df.csv', usecols=['Name', 'Website'])
    websites = df['Website']
    i = 0
    status = check_status(driver)
    while status[0] < 100 and status[1] < 20 and i < len(websites):
        url = websites[i]
        driver.get(url)
        time.sleep(5)
        try:
            element = driver.find_element("xpath",
                                          '/html/body/div[5]/div[3]/div/div[3]/div/div/main/div/div[1]/section/div/button/span/span[2]')
            if (element.get_attribute('innerText') == 'Join'):
                driver.find_element("xpath",
                                    '/html/body/div[5]/div[3]/div/div[3]/div/div/main/div/div[1]/section/div/button/span/span[2]').click()
        except:
            try:
                element = driver.find_element("xpath",
                                              '/html/body/div[4]/div[3]/div/div[3]/div/div/main/div/div[1]/section/div/button/span')
                if (element.get_attribute('innerText') == 'Join'):
                    driver.find_element("xpath",
                                        '/html/body/div[4]/div[3]/div/div[3]/div/div/main/div/div[1]/section/div/button/span').click()
            except:
                print('Join ' + url + ' failed')
        time.sleep(3)
        status = check_status(driver)
        i += 1
    # check for current status
    if status[0] == 100:
        print('Maximum number of groups joined (100)')
    if status[1] == 20:
        print('Maximum number of requests reached (20)')


def check_status(driver):
    # go to groups page
    time.sleep(3)
    driver.get('https://www.linkedin.com/groups')
    time.sleep(5)
    status = []
    # check the joined page
    num_of_joined = len(
        driver.find_elements("xpath", "//a[contains(@class, 'ember-view link-without-visited-state t-black')]"))
    time.sleep(3)
    # check the num of requests
    driver.get('https://www.linkedin.com/groups/requests')
    time.sleep(5)
    num_of_requests = len(
        driver.find_elements("xpath", "//a[contains(@class, 'ember-view link-without-visited-state t-black')]"))
    status = [num_of_joined, num_of_requests]
    return status


def returnLink(join_requested):
    return join_requested.get_attribute('href')


# def get_result(driver):
#     allstatus = {'Name': [], 'LinkedIn group': [], 'Result': [], 'Date': []}
#     # go to groups page for joined
#     driver.get('https://www.linkedin.com/groups')
#     time.sleep(3)
#     join_groups = driver.find_elements("xpath",
#                                        "//a[contains(@class, 'ember-view link-without-visited-state t-black')]")
#     list_link_join_group = list(map(returnLink, join_groups))
#     for link in list_link_join_group:
#         driver.get(link)
#         time.sleep(5)
#         date_joined = driver.find_element("xpath", "//p[contains(@class, 't-12 t-black--light')]").text.replace(
#             'Joined group: ', '')
#         name = driver.find_element("xpath", '//*[@id="group-entity-page"]/div/div/main/div/div[1]/section/div/h1/span')
#         allstatus['Name'].append(name.text)
#         allstatus['LinkedIn group'].append(link)
#         allstatus['Result'].append('Joined')
#         date = datetime.strptime(date_joined, '%b %Y')
#         date1 = date.strftime('%m/%Y')
#         allstatus['Date'].append(date.strftime('%m/%Y'))
#         print(date1)
#
#     # go to groups page for requested
#     driver.get('https://www.linkedin.com/groups/requests')
#     time.sleep(3)
#     join_requested = driver.find_elements("xpath",
#                                           "//a[contains(@class, 'ember-view link-without-visited-state t-black')]")
#     list_link_join_requested = list(map(returnLink, join_requested))
#     for link in list_link_join_requested:
#         driver.get(link)
#         time.sleep(5)
#         name = driver.find_element("xpath", '//*[@id="group-entity-page"]/div/div/main/div/div[1]/section/div/h1/span')
#         date_joined = datetime.today().strftime('%m/%d/%Y')
#         allstatus['Name'].append(name.text)
#         allstatus['LinkedIn group'].append(link)
#         allstatus['Result'].append('Requested')
#         allstatus['Date'].append(date_joined)
#
#     # update status for the rest of the groups
#     with open('input/keywords.csv', 'r') as csvfile:
#         datareader = csv.reader(csvfile)
#         for row in datareader:
#             keyword = ''.join(row)
#             df = pd.read_csv(f'{keyword}_linkedin_groups.csv')
#             row_count = df.shape[0]
#             for i in range(1, row_count):
#                 if df['Name'][i] not in allstatus['Name']:
#                     allstatus['Name'].append(df['Name'][i])
#                     allstatus['LinkedIn group'].append(df['Website'][i])
#                     allstatus['Result'].append('Limit request to join')
#                     allstatus['Date'].append('')
#
#     allstatus = pd.DataFrame(allstatus)
#     allstatus.to_csv('results.csv')
