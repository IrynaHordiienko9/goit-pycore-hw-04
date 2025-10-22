def total_salary(path):
    try:
        with open(path, encoding='utf-8') as file:
            salaries = []
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    try:
                        salary = int(parts[1])
                        salaries.append(salary)
                    except ValueError:
                        continue  
            if not salaries:
                return (0, 0)
            total = sum(salaries)
            average = total // len(salaries)
            return (total, average)
    except FileNotFoundError:
        print("Файл не знайдено.")
        return (0, 0)
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return (0, 0) 
   
total, average = total_salary("C:\\Users\\Lenovo\\Documents\\path.txt.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")