from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.log import LOG
from mycroft.api import DeviceApi
import time

#creating an object for the hour of the d
t = time.localtime()
current_time = int(time.strftime("%H", t))

device_name = data={"name": device["name"]}

class FinishedBooting(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.add_event("mycroft.skills.initialized", self.handle_booting_finished)
        LOG.debug("add event handle boot finished")

    @intent_file_handler('booting.finished.intent')
    def handle_booting_finished(self, message):
        if current_time >=12 and current_time < 18:
            self.speak_dialog('afternoon.finished', 'booting.finished', data={"name": device_name["name"]})
            LOG.debug('finished booting')

        elif current_time >= 18:
            self.speak_dialog('evening.finished', 'booting.finished', data={"name": device_name["name"]}) 
            LOG.debug('finished booting')

        else:
            self.speak_dialog('morning.finished', 'booting.finished', data={"name": device_name["name"]})
            LOG.debug('finished booting')

def create_skill():
    return FinishedBooting()

