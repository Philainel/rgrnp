
define d = Character("Разработчик")

label final_message:
    scene black
    show dev
    d "Приветствую. Благодарю за уделённое новелле время. На текущий момент это конец демо-версии."
    d "Можете попытаться перепройти, выйдя на другую ветку."
    hide dev
    show qrcode at top
    d "Если вам интересна судьба проекта (а я хочу его продолжить), то прошу подписаться на следующий репозиторий на гитхабе (ссылка далее или по QR)"
    d "https://github.com/Philainel/gigachads-radik-novel-project"
