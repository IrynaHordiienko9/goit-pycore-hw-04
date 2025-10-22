def get_cats_info(path):
    cats = []
    try:
        with open(path, encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat_id, name, age = parts
                    cats.append({"id": cat_id, "name": name, "age": age})
    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
    except Exception as e:
        print(f"Сталася помилка при читанні файлу: {e}")
    return cats

cats_info = get_cats_info("C:\\Users\\Lenovo\\Documents\\path2.txt.txt")
print(cats_info)