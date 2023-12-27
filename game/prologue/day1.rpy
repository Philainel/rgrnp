define submind = Character("...")
define gg = Character("Алексей")
define a = Character("Андрей")

image splashImage = im.Alpha("GUK.png", 0.5)
image white = "#fff"

label prologue_day_1:
    scene black 
    with Pause(1)

    show splashImage with dissolve
    show text "Пролог" at top 
    with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)
    
    submind """
    Нет ничего.

    Лишь теплая первобытная тьма.

    В ней бродит твое сознание; оно не тяжелее ячменного зернышка.

    Всё.

    Тебе не нужно больше ничего делать.

    Никогда.

    Совсем никогда.
    """

    "~ Вообще совсем никогда? ~"
    
    submind """
    Вообще совсем никогда.

    Проходит запредельное количество времени.
    
    Оно полностью лишено страданий.
    
    В нем нет никаких экзаменов.
    """
    "~ Шикарно! ~"

    submind "Более чем."

    "~ Хочу ещё, ещё подавай. ~"

    submind "Да на здоровье - ничто фаршированное ничем с приправой из ничего!"

    "~ Люблю ничто. А плесни-ка еще чуток сладкого забытья! ~"

    submind "Чуток сладкого забытия"

    scene window

    "Алексей проснулся в своей комнате"

    jump prologue_day_1_nvl
    