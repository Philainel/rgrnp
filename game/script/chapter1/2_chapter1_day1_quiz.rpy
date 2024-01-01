define persistent.quiz = False

label chapter1_day1_quiz:
    # 407 util/start.md
    menu quiz:
        d "Викторина разрабатывается. Для создания развилок выберете исход."
        "Пройдена":
            $ persistent.quiz = True
        "Завалена":
            $ persistent.quiz = False
    jump chapter1_day1_searching
