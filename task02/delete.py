from connect import collection



# Функція для видалення кота за ім'ям
def delete_cat_by_name(name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Кіт з ім'ям {name} був успішно видалений.")
        else:
            print(f"Не знайдено кота з ім'ям {name}.")
    except Exception as e:
        print(f"Помилка при видаленні кота: {e}")


# Функція для видалення всіх котів з колекції
def delete_all_cats():
    try:
        result = collection.delete_many({})
        print(f"{result.deleted_count} котів було успішно видалено.")
    except Exception as e:
        print(f"Помилка при видаленні всіх котів: {e}")

