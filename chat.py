from collections import deque

class Chat():
    """docstring for Chat"""
    def __init__(self):
        self.latestMessages = deque(maxlen=20)

    def addMessage(self, msg):
        if len(self.latestMessages) >= self.latestMessages.maxlen:
            self.latestMessages.popleft()

        self.latestMessages.append(msg)

    def runNN(self):
        return "Len: " + str(len(self.latestMessages)) + " Text: " + str(self.latestMessages[0].text)
