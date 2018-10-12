class User():
    def __init__(self, settingsFile):
        self.settingsFile = settingsFile
        self.settings = self.readSettings()

    def readSettings(self):
        settings = {}
        with open(self.settingsFile, "r") as file:
            individualSettings = file.read().split('\n')
        for setting in individualSettings:
            setting = setting.split(" = ")
            settings[setting[0]] = setting[1]
        return settings

    def getSettings(self):
        return self.settings
