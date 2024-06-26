from utils import tz

TEXT_AGREE = " Это сервис для напоминаний о дедлайнах и других важных датах. Хотите получать уведомления?"
TEXT_UNSUBSCRIBE = "Хотите отписаться?"

MAIN_MENU_ADMIN = "Выберите действие:"

INVITATION_INPUT_ID = "Введите telegram id человека (он может узнать его, написав нашему боту /id)"

SUCCESS_ADD_NEW_ADMIN = "Успешно добавлен новый администратор"

SUCCESS_ADD_NEW_DEADLINE = "Успешно добавлен новый дедлайн"

VALIDATE_ID = "Id состоит только из цифр, попробуйте ввести еще раз"

INVITATION_INPUT_DATE = f"Введите дату и время события({tz}) в формате: дд.мм.ггггг чч.мм\nК примеру 01.01.2025 15.30"

VALIDATE_DATE = "Дата должна быть в формате: дд.мм.ггггг чч.мм\n" + \
                "К примеру 01.01.2025 15.30\n" \
                "Попробуйте ввести еще раз"

VALIDATE_DATE_TOO_LATE = "Мы не можем уведомить подписчиков о просроченном дедлайне...\n" + \
                         "Попробуйте ввести еще раз, дату позже текущей"

INVITATION_INPUT_NAME = "Введите имя события дедлайна\n" + \
                        "(должно начинаться с буквы, может содержать цифры, символы: , . _ : - space)"

VALIDATE_NAME = "Попробуйте еще раз ввести имя события дедлайна,\n" + \
                "которое должно начинаться с буквы, может содержать цифры, символы: , . _ : - space"

INVITATION_INPUT_COMMENT = "Введите описание дедлайна\n" + \
                           "(должно начинаться с буквы, может содержать цифры, символы: , . _ : - space)"

VALIDATE_COMMENT = "Попробуйте еще раз ввести комментарий к дедлайну,\n" + \
                   "который должно начинаться с буквы, может содержать цифры, символы: , . _ : - space"

DELETE_DEADLINE = "Введите id дедлайна для удаления"

DOUBTFUL_BUT_OK = "Если вы ввели существующий id, дедлайн удален"
