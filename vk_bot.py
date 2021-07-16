import bs4 as bs4

import answers

class VkBot:

    def __init__(self, user_id):
        self.USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)
        self.my_str = ""
        self._COMMANDS = ["привет", "пока", "как дела"]

        self._inputMes = {"для чего нужен бот?": answers.about_us1,
                          "что он умеет?": answers.about_us2}

    
    def _get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id" + str(user_id))

        bs = bs4.BeautifulSoup(request.text, "html.parser")

        user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])

        return user_name.split()[0]

    def new_message(self, message):
        if message.lower() == self._COMMANDS[0]:
            return f"Привет, {self._USERNAME}!"

        elif message.lower() == self._COMMANDS[1]:
            return f"До скорой встречи, {self._USERNAME}!"

        elif message.lower() == self._COMMANDS[2]:
            return "У меня всё хорошо 😊"

        else:
            for key, value in self._inputMes.items():
                if message.lower() == key:
                    return value
            return "Не понимаю тебя 🤷‍♂️"

    


    @staticmethod
    def _clean_all_tag_from_str(string_line):

        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True

        return result
