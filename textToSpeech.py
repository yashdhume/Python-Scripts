import gtts
import fbchat as fb
class AutoBot(fb.Client):
    def tts(self, message):
        tts = gtts.gTTS(text=message, lang='en')
        tts.save("temp.mp3")
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)
        if author_id != self.uid:
            self.tts(message_object.text)
            self.sendLocalFiles("temp.mp3", message=message_object.author, thread_id=thread_id, thread_type=thread_type)

client = AutoBot("Enter Facebook email here", "Enter Password here")
client.listen()