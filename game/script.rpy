# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
# define e = Character('Эйлин', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    "Developer" "Привет" 
    "Developer" "Это альфа версия новеллы" 
    "Developer" "Работа над многими частями находится в активной фазе, поэтому в игре нет, например, детальных диалогов" 
    "Developer" "Надеюсь на помнимание" 
    
    #TODO: RESTORE THIS TO prologue_day_1 TO BEGIN FROM THE START
    jump prologue_day_1_nvl

    return
