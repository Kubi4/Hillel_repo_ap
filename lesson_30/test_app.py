import allure

@allure.feature("Математичні операції")
def test_addition():

    @allure.step("Перевіряємо додавання 2 + 2")
    def step():
        return 2 + 2

    result = step()
    assert result == 4


@allure.feature("Математичні операції")
def test_subtraction():

    @allure.step("Перевіряємо віднімання 1 - 1")
    def step():
        return 1 - 1

    result = step()
    assert result == 0


@allure.feature("Математичні операції")
def test_multiplication():

    @allure.step("Перевіряємо множення 2 * 4")
    def step():
        return 2 * 4

    result = step()
    assert result == 8


@allure.feature("Математичні операції")
def test_negative_result():

    @allure.step("Перевіряємо від’ємний результат 5 - 7")
    def step():
        return 5 - 7

    result = step()
    assert result == -2

@allure.feature("Математичні операції")
def test_wrong_addition():

    @allure.step("Спеціально неправильна перевірка 5 + 5")
    def step():
        return 5 + 5

    result = step()
    assert result == 11


@allure.feature("Математичні операції")
def test_wrong_multiplication():

    @allure.step("Спеціально неправильна перевірка 3 * 3")
    def step():
        return 3 * 3

    result = step()
    assert result == 10