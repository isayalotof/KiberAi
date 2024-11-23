import sqlite3

class DataBase:
    def __init__(self, table_name = 'user'):
        self.db = sqlite3.connect('data.db')
        self.cursor = self.db.cursor()
        self.table_name = table_name


class DataBaseUpdate(DataBase):
    def add_new_user(self, user_name: str, phone_number: str) -> bool:
        self.cursor.execute("")

    def remove_user(self, user_name: str) -> bool:
        pass

class DataBaseTools(DataBase):
    def update_user_text_req(self, user_name: str) -> bool:
        ...

    def update_user_img_req(self, user_name: str) -> bool:
        ...

    def update_user_total_text_score(self, user_name) -> bool:
        ...

    def update_user_total_img_score(self, user_name) -> bool:
        ...

    def reset_all_limit(self) -> bool:
        ...

    def check_text_limit(self, user_name: str) -> bool:
        ...

    def check_img_limit(self, user_name: str) -> bool:
        ...