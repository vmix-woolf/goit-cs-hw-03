from connect import collection
from create import create_cat, add_feature_to_cat
from read import read_all_cats, read_cat_by_name
from update import update_cat_age
from delete import delete_all_cats, delete_cat_by_name


if __name__ == "__main__":
    # Створюємо кілька котів
    create_cat("Barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    create_cat("Murchik", 5, ["любить рибу", "лінивий", "чорний"])
    create_cat("Marsik", 2, ["любить сухий корм", "кумедний", "білий"])
    create_cat("Snezhok", 5, ["полюбляє безкінечно мурликати", "зухвалий", "чорний"])
    create_cat("Zefir", 3, ["любить рибу", "лінивий", "черепаховий"])

    # Читання всіх котів
    print("\nВсі коти:")
    read_all_cats()

    # Читання кота за ім'ям
    print("\nІнформація про кота Barsik:")
    read_cat_by_name("Barsik")

    # Оновлення віку кота
    update_cat_age("Barsik", 4)

    # Додавання характеристики коту
    add_feature_to_cat("Barsik", "любить грати з ниткою")

    # Видалення кота за ім'ям
    delete_cat_by_name("Zefir")

    # Видалення всіх котів
    delete_all_cats()
