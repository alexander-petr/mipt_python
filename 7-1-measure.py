import RPi.GPIO as rp
import time
from matplotlib import pyplot as plt

rp.setmode(rp.BCM)

leds = [2, 3, 4, 17, 27, 22, 10, 9]
rp.setup(leds, rp.OUT)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
rp.setup(dac, rp.OUT)

comp = 14
rp.setup(comp, rp.IN)

troyka = 13

#перевод в двоичную ситсему исчесления
def binary(value):
    return[int(element) for element in bin(value)[2:].zfill(8)]
#измерение значений на тройке-модуле
def adc():
    value = 0
    for i in range (7, -1, -1):
        value += 2**i
        rp.output(dac, binary(value))
        time.sleep (0.005)
        if rp.input(comp) == 1:
            value -= 2**i
    return value

try:
    adc_value = 0
    new_values = []
    start_time = time.time()
    number = 0

    rp.setup(troyka, rp.OUT, initial = rp.HIGH)
    #зарядка конденсатора
    print('Зарядка конденсатора')
    while adc_value < 207 * 0.97:
        adc_value = adc()
        new_values.append(adc_value)
        time.sleep(0)
        number += 1
        rp.output(leds, binary(adc_value))
        print(adc_value)
    
    rp.output(troyka, 0)
    
    #разрядка конденсатора
    print('Разрядка конденсатора')
    while adc_value > 192:
        adc_value = adc()
        new_values.append(adc_value)
        time.sleep(0)
        number += 1
        rp.output(leds, binary(adc_value))
        print(adc_value)
    #записываем время эксперимента
    finish_time = time.time()
    experiment_time = finish_time - start_time
    #записываем данные в файлы
    with open('data.txt', 'w') as f:
        for i in new_values:
            f.write(str(i) + '\n')
    with open('settings.txt', 'w') as f:
        f.write(str(1/(experiment_time/number)) + '\n')
    
    print('Общая продолжительность эксперимента:', "{:.2f}".format(experiment_time), 'c', ' Период одного измерения:', "{:.2f}".format(experiment_time/number), 'c', ' Средняя частота дискретизации проведенных измерений:', "{:.2f}".format(number/experiment_time), 'Шаг квантования: 0,013')
    #строим график зависимости времени от напряжения
    y = [i/256*3.3 for i in new_values]
    x = [i*experiment_time/number for i in range(len(new_values))]
    plt.plot(x, y)
    plt.xlabel('Время, с')
    plt.ylabel('Напряжение, В')
    plt.show()

finally:
    #подаем ноль на все выходы и сбрасываем настройки
    rp.output(leds, 0)
    rp.output(dac, 0)
    rp.cleanup()






