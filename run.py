from ray import SMSBot

with SMSBot() as sms:
    sms.go_to_dashboard("https://sms.rayadvertising.com/login")
    sms.login_to_dashboard("ray@admin", "ray@2022")
    sms.find_campaign_section()
    

