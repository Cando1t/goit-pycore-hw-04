def total_salary(path):
    total_salary_sum = 0
    total_developers = 0
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                
                salary = int(salary)
                
                total_salary_sum += salary
                
                total_developers += 1
          
        average_salary = total_salary_sum / total_developers
        
        return total_salary_sum, average_salary
        
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None, None
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return None, None

total, average = total_salary("path/to/salary_file.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")