# Builded with util/parse.py

define char_chapter1_day1_rita_bridge_0 = Character("ГГ")
define char_chapter1_day1_rita_bridge_1 = Character("Волонтер")
define char_chapter1_day1_rita_bridge_2 = Character("Саша")

label chapter1_day1_rita_bridge:
    if persistent.search_locaton == "caffeteria":
        # (Радиоточка)
        "~ Радиоточка была небольшим помещением, где было сложно спрятать рюкзак даже целенаправленно, не говоря уж о случайной утере. Нам хватило двух минут поисков, чтобы стал очевидным факт - рюкзака тут нет. ~"
        char_chapter1_day1_rita_bridge_0 "Мы правда не можем поискать его в других местах? Это вопрос пятнадцати минут…"
        "~ Саша устало рухнула на скамейку. На ней не было лица. Неужели так сильно расстроилась из-за пропажи? Если да, то как это, черт возьми, соотносится с ее требованием прекратить поиски? ~"
        "~ Пока я ходил из стороны в сторону, пытаясь найти объяснение всему произошедшему, Саша заказывала такси. ~"
        "~ Почему мы не можем вернуться обратно ~"
        "~ Почему у нее такой разбитый вид? Почему я выбрал “радиоточку”?.. ~"
        "~ Чувствовал же, что искать нужно в другом месте ~"
        "~ Выглядело всё это крайне нелепо ~"
        # (Переход к общей части)
    else:
        # (Последняя аудитория со стендом)
        char_chapter1_day1_rita_bridge_0 "Прошу прощения, вы не видели тут никаких утерянных вещей? Может, обращали внимание на бесхозные рюкзаки, например…"
        char_chapter1_day1_rita_bridge_1 "Неа, не обращали. А если б обратили, то уже давно бы отыскали владельца. Но вы походите и проверьте еще раз, на всякий случай. - Он обвел рукой аудиторию. - Только не устраивайте дебошей, нам же потом за ваши раскопки держать ответ…"
        char_chapter1_day1_rita_bridge_0 "Мы правда не можем поискать его в других местах? Это вопрос пятнадцати минут…"
        "~ Саша устало рухнула на стул у стенда. На ней не было лица. Неужели так сильно расстроилась из-за пропажи? Если да, то как это, черт возьми, соотносится с ее требованием прекратить поиски? ~"
        "~ Пока я ходил из стороны в сторону, пытаясь найти объяснение всему произошедшему, Саша заказывала такси. ~"
        "~ Почему мы не можем вернуться обратно ~"
        "~ Почему у нее такой разбитый вид? Почему я выбрал эту аудиторию?.. ~"
        "~ Чувствовал же, что искать нужно в другом месте ~"
        "~ Выглядело всё это крайне нелепо ~"
        # (Переход к общей части)
    char_chapter1_day1_rita_bridge_0 "Поедешь домой?"
    char_chapter1_day1_rita_bridge_2 "У меня нет выбора."
    char_chapter1_day1_rita_bridge_0 "Прости, если сую нос не в свое дело, но мне всё ещё не ясна причина твоего решения отступить."
    char_chapter1_day1_rita_bridge_0 "Осталось ведь всего ничего - проверить несколько комнат, в одной из которых обязательно найдется твое тканевое сокровище. Мне он уже практически мерещится…"
    char_chapter1_day1_rita_bridge_2 "А если _не_ найдется? Однажды в похожей ситуации я пошла на риск - и сильно об этом пожалела."
    char_chapter1_day1_rita_bridge_2 "Теперь я руководствуюсь строгой логикой, исключающей все варианты с сомнительными шансами на успех. – отрезала Саша."
    "~ Пора уже запомнить, что Саша моментально вспыхивает, когда её выбор подвергают сомнению. Запомнить, чтобы завтра забыть. ~"
    "~ Внезапная вспышка волнения отпустила так же быстро, как и появилась - пораженческие настроения Саши вынудили сдаться и меня. Теперь, когда надежда покинула последнего оптимиста в нашем тандеме, можно было смело переходить к стадии принятия. С чего я вообще взял, что её осторожность в сложившейся ситуации была излишней? Что я знал о её мотивах? Она же явно поступает так неспроста. Чувствую себя идиотом. ~"
    "~ Телефон в ее руках зазвонил. ~"
    char_chapter1_day1_rita_bridge_0 "Карета подана."
    char_chapter1_day1_rita_bridge_2 "Мне пора. Слушай, Лёша…"
    "~ Я вопросительно промычал. ~"
    char_chapter1_day1_rita_bridge_2 "Прости за это нелепое путешествие… и спасибо за помощь."
    char_chapter1_day1_rita_bridge_0 "Не извиняйся. Я сам выразил желание помочь."
    if persistent.quiz:
        # (Викторина)
        "~ Она внезапно ткнула телефоном мне в лицо. ~"
        char_chapter1_day1_rita_bridge_2 "Ты есть в этой соцсети?"
        char_chapter1_day1_rita_bridge_0 "Допустим."
        char_chapter1_day1_rita_bridge_2 "Найди себя."
        "~ Сует его в руки. Здрасьте, приехали. А вдруг я не хочу? ~"
        "~ Я нашел свой профиль и передал телефон обратно ~"
        char_chapter1_day1_rita_bridge_2 "Я напишу чуть позже, хорошо?"
        char_chapter1_day1_rita_bridge_0 "В любое удобное время."
        "~ Саша вздохнула и встала на ноги. ~"
        char_chapter1_day1_rita_bridge_0 "Пока."
        "~ Она помахала рукой. ~"
        char_chapter1_day1_rita_bridge_2 "Еще спишемся."
        # (Переход к общей части)
    else:
        # (Аналог)
        "~ Саша вздохнула и встала на ноги. ~"
        char_chapter1_day1_rita_bridge_0 "Пока."
        "~ Она помахала рукой. ~"
        char_chapter1_day1_rita_bridge_2 "До встречи."
        "~ Ага, как же. ~"
        # (Переход к общей части)
    "~ Ушла. Куда теперь податься? ~"
    "~ Быть может, в коворкинге еще остались люди ~"
    "~ Я побрел обратно к чаю и уюту. ~"
    jump final_message
