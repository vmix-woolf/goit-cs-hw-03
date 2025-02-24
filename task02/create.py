from connect import collection

# Функція для створення нового кота
def create_cat(name, age, features):
    cat = {
        "name": name,
        "age": age,
        "features": features
    }
    try:
        result = collection.insert_one(cat)
        print(f"Кіт {name} був успішно доданий!")
    except Exception as e:
        print(f"Помилка при додаванні кота: {e}")

# Функція для додавання нової характеристики коту
def add_feature_to_cat(name, new_feature):
    try:
        result = collection.update_one(
            {"name": name},
            {"$push": {"features": new_feature}}
        )
        if result.modified_count > 0:
            print(f"Характеристика '{new_feature}' була успішно додана коту {name}.")
        else:
            print(f"Не знайдено кота з ім'ям {name}.")
    except Exception as e:
        print(f"Помилка при додаванні характеристики: {e}")
