class Content:
    def __init__(self, url, title, body):
        self.url = url;
        self.title = title;
        self.body = body;

    def get_data(self):
        print(f"The URL Of Page Is: {self.url}");
        print(f"The Title Of The Page Is: {self.title}");
        print(f"The Body Of The Page Is: {self.body}");

