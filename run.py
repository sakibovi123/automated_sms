from ray import SMSBot
import schedule

with SMSBot() as sms:
    def execute():
        sms.go_to_dashboard("https://sms.rayadvertising.com/login")
        sms.login_to_dashboard("ray@admin", "ray@2022")
        sms.find_number_section()
    
schedule.every(1).minute.do(execute())
schedule.every(20).minute.do(execute())
schedule.every(2).hour.do(execute())
schedule.every(12).hour.do(execute())
schedule.every(24).hour.do(execute())
schedule.every(26).hour.do(execute())
    


