# Builded with util/parse.py

define char_prologue_mother_0 = Character("Мама")
define char_prologue_mother_1 = Character("ГГ")

label prologue_mother:
    "~ Внезапно приходит осознание: штуки, сомкнувшиеся на моих глазах, полностью подконтрольны мне. ~"
    "~ Я пробую разомкнуть их… ~"
    scene window
    char_prologue_mother_0 "Алёша! Лёша! Алексей, это форменное безобразие! Снова ты спишь до обеда…"
    "~ Тот самый голос. ~"
    "~ Мама с недовольным видом ходит по комнате, распахивает шторы. Она останавливается у подоконников, чтобы опрыскать фикусы в глиняных горшках. ~"
    char_prologue_mother_0 "Ну скажи мне, в кого ты такой пожарник! Все при деле с самого утра - и только ты проводишь последние каникулы в постели. Скажи мне, ты снова сидел за компьютером до полуночи?..."
    "~ Я поднялся на руках и огляделся. Легкий ветерок колышет прозрачные тюли, на полу рисуют забавные узоры лучи мягкого летнего солнца. Непередаваемо уютно. ~"
    char_prologue_mother_1 "Каникулы ведь на то и каникулы - отдых по программе “всё включено”... – сонно пробубнил я"
    char_prologue_mother_0 "Отдыхать можно и с пользой… – мама добралась до последнего подоконника, хлама на котором было вдвое больше, чем на предыдущих - хотя бы для собственного здоровья…"
    "~ Потягиваюсь и, крякнув, хватаю вещи с прикроватной тумбочки. Не проходит и минуты - солдат одет и готов нести службу. ~"
    "~ Тем временем за грудой пыльных учебников мама обнаруживает считавшийся безвозвратно утерянным фикус. Он жалобно трепещет своими сморщившимися листьями, застенчиво прикрывает ими высохшую почву под собой. ~"
    "~ Мама, тяжело вздохнув, направляет на беднягу носик опрыскивателя и с особым усердием жмет на его ручку, вымещая накопившуюся злость ~"
    "~ Предвкушение взбучки заставило меня выскочить из комнаты. Пока мама была занята реанимацией растения, я мог спокойно умыться и поесть. ~"
    scene black
    "~ Быстро расправившись с омлетом и парой восхитительных блинов, я поспешил в свое убежище. ~"
    scene pc
    "~ Доведенными до автоматизма движениями включил компьютер, в пару действий заправил кровать и плюхнулся в кресло, тёплое мягкое кресло… ~"
    "~ Утренней бодрости как не бывало - сладкая истома тут же овладела мной. Я глубоко вдохнул и закрыл глаза ~"
    scene black
    "~ Совсем недавно я выпустился со школы. Сплошь и рядом встречаешь людей, готовых раз и навсегда забыть об её однообразии, глупых правилах, ответственности за успеваемость, брюках, юбках и рубашках. ~"
    "~ Школа для них стала испытанием, которое они _преодолели_ плечом к плечу с одноклассниками. Я же полюбил школу за то, что её рутина придавала моим действиям смысл ~"
    "~ Это во многом объясняет, почему каникулы для меня - без преувеличения, настоящая временная аномалия. ~"
    "~ Каждая неделя каникул - мимолетный призрак, проносящийся мимо в обескураживающей спешке, заставляющий смотреть на календарь и наблюдать, как испаряются дни ~"
    "~ Они похожи на страницы внезапно наскучившей книги, которую ты спешно пролистываешь, чтобы поскорее начать другую. ~"
    "~ Пора безграничных возможностей, когда спадают оковы школьных обязанностей, стремится стать одним из самых незапоминающихся эпизодов моей жизни ~"
    "~ Я тоскую по порядку, который навязывала мне школа, и с беспокойством отмечаю, что без него рискую увязнуть в болоте стагнации ~"
    scene pc
    jump prologue_nvl
