adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
task13_adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(task13_adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""

task13_adwentures_of_tom_sawer = task13_adwentures_of_tom_sawer.replace("....", " ")
print(task13_adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
task13_adwentures_of_tom_sawer = task13_adwentures_of_tom_sawer.replace("  ", "")
print(task13_adwentures_of_tom_sawer)


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_h = task13_adwentures_of_tom_sawer.count("h")
print("Літера h:", count_h)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
all_words = task13_adwentures_of_tom_sawer.split()
upper_words = 0
for word in all_words:
    if word == word.capitalize():
        upper_words += 1
print("Слів з Великої літери:", upper_words)


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
find_tom = task13_adwentures_of_tom_sawer.find("Tom", 1)
print("Позиція другого слова Tom:", find_tom)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.replace("....", " ").replace("  ", "").split(".")[:-1]

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("4й рядок у нижньому регістрі:", adwentures_of_tom_sawer_sentences[3].lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

by_the_time = adwentures_of_tom_sawer.find("By the time")
if by_the_time != -1:
    print("Перевірте чи починається якесь речення з \"By the time\": Так, починається")
else:
    print(("Перевірте чи починається якесь речення з \"By the time\":Ні, не починається"))

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence_words = adwentures_of_tom_sawer_sentences[len(adwentures_of_tom_sawer_sentences)-1].split()
print("Кількість слів останнього речення:", len(last_sentence_words))