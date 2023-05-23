#3
import random
import logging
def rand_file(file_path, num):
    try:
        with open(file_path, 'w') as file:
            for i in range(num):
                data = random.randint(1, 100)
                file.write(str(data) + '\n')
                logging.info(f'Згенероване число: {data}')
    except Exception as e:
        logging.error(str(e))
rand_file('input_randm.txt', int(input('Кількість згенерованих чисел:')))