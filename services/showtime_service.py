import json

from models.showtime import Showtime


class ShowtimeService:
    def __init__(self):
        self.showtime_list = []
        self.load_data()

    def add_showtime(self, showtime):
        self.showtime_list.append(showtime)

    def display_showtimes(self):
        if len(self.showtime_list) == 0:
            print("Showtime list is empty")
            return

        for showtime in self.showtime_list:
            print(showtime)

    def find_showtime_by_id(self, showtime_id):
        for showtime in self.showtime_list:
            if showtime.showtime_id == showtime_id:
                return showtime

        return None

    def delete_showtime(self, showtime_id):
        showtime = self.find_showtime_by_id(showtime_id)

        if showtime is not None:
            self.showtime_list.remove(showtime)
            return True

        return False

    def save_data(self):
        data = []

        for showtime in self.showtime_list:
            data.append(showtime.to_dict())

        with open("data/showtimes.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        try:
            with open("data/showtimes.json", "r", encoding="utf-8") as file:
                data = json.load(file)

                for item in data:
                    showtime = Showtime(
                        item["showtime_id"],
                        item["movie_title"],
                        item["date"],
                        item["time"],
                        item["room"]
                    )

                    self.showtime_list.append(showtime)

        except:
            pass