import json

f = open("122722.json")
data = json.load(f)
# print(data

for i in data:
    print(i["customer_phone"])


    def find_campaign_id(self):
        wait = WebDriverWait(self, 25)
        select_camp = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "tbody tr:nth-child(23) td:nth-child(1)"
        )))

        select_camp.click()