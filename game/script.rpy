# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
# define e = Character('Эйлин', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    #TODO: RESTORE THIS TO prologue_monologue TO BEGIN FROM THE START
    # jump prologue_monologue
    jump chapter1_day1_start
    return
