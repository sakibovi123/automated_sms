from ray import SMSBot
import schedule
import time

with SMSBot() as sms:
    def execute():
        # sms.go_to_dashboard("https://sms.rayadvertising.com/login")
        sms.go_to_dashboard("https://sms.rayadvertising.com/login")
        sms.login_to_dashboard("root", "123456")
        sms.find_number_section()
        sms.clear_all_cookies()
    
# schedule.every(1).minutes.do(execute)

schedule.every().day.at("12:00").do(execute)
schedule.every().day.at("12:20").do(execute)
schedule.every().day.at("14:00").do(execute)
schedule.every().day.at("22:00").do(execute)


while True:
    schedule.run_pending()
    time.sleep(5)