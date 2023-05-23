#2
import logging
def write_file(fill_path, data):
    try:
        with open(fill_path, 'w') as file:
            file.write(data)
        logging.info(f'Запис у файл {fill_path} пройшов успішно.')
    except Exception as e:
        logging.error(f'В цьому файлі {fill_path} трапилась помилка: {e}')

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
write_file('output.txt', input('Введіть що треба вписати в файл: '))