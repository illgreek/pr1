import spacy

# Завантаження моделі (залежно від мови, яку ви вибрали)
nlp = spacy.load("uk_core_news_sm")  # для української
# nlp = spacy.load("en_core_web_sm")  # для англійської

# Приклад речення для аналізу
sentence = "Електронний журнал дозволяє студентам переглядати свої оцінки онлайн."

# Аналіз речення
doc = nlp(sentence)

# Виведення синтаксичного аналізу
for token in doc:
    print(f"Слово: {token.text}, Частина мови: {token.pos_}, Граматичні відношення: {token.dep_}, Лема: {token.lemma_}")