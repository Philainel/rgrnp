define gg = Character("Алексей", kind=nvl) #TODO: Check source to restore sound
define a = Character("Андрей", kind=nvl)

define menu = nvl_menu

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)
define background_pc = "#1E1E1E"

label prologue_day_1_nvl:
    scene background_pc
    show pc
    window hide

    gg "Сообщение 1"
    # gg "Сообщение 2"
    # a "Ответ 1"
    menu (nvl=True):
        "Чел ты":
            nvl_narrator "Чел ты"
            gg "Чел ты"
            pass
        "Когда":
            nvl_narrator "Когда"
            gg "Когда"
            pass
        "Сделаешь":
            nvl_narrator "Сделаешь"
            gg "Сделаешь"
            pass
        "Новеллу":
            nvl_narrator "Новеллу"
            gg "Новеллу"
            pass
    nvl_narrator "Вот это текст нарратора"
    
    "Developer" "А это классический текст"
    "Developer" "Вот тут рофл случился"
    # nvl hide
    "Developer" "Эта часть прорабатывается, здесь будет диалог с другом ГГ, над переходом я работаю"
    # nvl clear
    # nvl show

    scene black with Dissolve(2)
    with Pause(1)

    jump prologue_day_2 
