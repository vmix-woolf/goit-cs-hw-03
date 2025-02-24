from connect import collection


# Функція для виведення всіх котів з колекції
def read_all_cats():
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except Exception as e:
        print(f"Помилка при читанні котів: {e}")


# Функція для виведення кота за ім'ям
def read_cat_by_name(name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"Кіт з ім'ям {name} не знайдений.")
    except Exception as e:
        print(f"Помилка при пошуку кота: {e}")
