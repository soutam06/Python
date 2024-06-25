import time
from plyer import notification
for i in range(5):
    notification.notify(title ='Please drink water',app_name="Drinking water" ,message='Please drink water for your own safety',timeout=5 )
    time.sleep(60)