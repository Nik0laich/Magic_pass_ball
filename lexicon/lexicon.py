answer: dict[str, list[str]] = {'positive': ['Бесспорно', 'Предрешено',
                                             'Никаких сомнений',
                                             'Определённо да',
                                             'Можешь быть уверен в этом'],
                                'not_positive': ['Мне кажется - да',
                                                 'Вероятнее всего',
                                                 'Хорошие перспективы',
                                                 'Знаки говорят - да', 'Да'],
                                'neutral': ['Пока неясно, попробуй снова',
                                            'Спроси позже',
                                            'Лучше не рассказывать',
                                            'Сейчас нельзя предсказать',
                                            'Сконцентрируйся и спроси опять'],
                                'negative': ['Даже не думай',
                                             'Мой ответ - нет',
                                             'По моим данным - нет',
                                             'Перспективы не очень хорошие',
                                             'Весьма сомнительно']}

type_answer: list[str] = [c for c in answer.keys()]

chars_s: str = '''0123456789abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&*+-=?@^_'''
not_used_chars: str = 'il1Lo0O'

gener_chars: dict[str, str] = {
    'digits': '0123456789',
    'lowercase_letters': 'abcdefghijklmnopqrstuvwxyz',
    'uppercase_letters': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'punctuation': '!#$%&*+-=?@^_',
    'not_used': '^_+-=@o0l1'
}
