from connect import collection


# Функція для оновлення віку кота
def update_cat_age(name, new_age):
    try:
        result = collection.update_one(
            {"name": name},
            {"$set": {"age": new_age}}
        )
        if result.modified_count > 0:
            print(f"Вік кота {name} був успішно оновлений на {new_age}.")
        else:
            print(f"Не знайдено кота з ім'ям {name}, або його вік вже такий.")
    except Exception as e:
        print(f"Помилка при оновленні віку кота: {e}")
