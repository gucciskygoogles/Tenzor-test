# Tenzor-test
Тесты созданы для браузера Chrome. Для работы с тестами необходимо скачать файл **chromedriver.exe**, который должен быть помещен в переменную **Path**.
Для переноса репозитория на свой локальный компьютер используется команда ```git clone https://github.com/gucciskygoogles```
**Инструкция для Windows**

Перед установкой зависимостей стоит создать виртуальное окружение, после чего устанавливаем зависимости с помощью следующей команды:
```
pip install -r requriements.txt
```
Для создания отчетности был использован **Allure**, который требуется установить.
В **Power Shell** Используем следующую команду ```iwr -useb get.scoop.sh | iex```, если возникнет ошибка, то необходимо ввести это 
```
Set-ExecutionPolicy RemoteSigned -scope CurrentUser
```
И снова вводим ```iwr -useb get.scoop.sh | iex```
Следующая команда - ```scoop install allure```

Запускаем тесты и создаем папку для отчетов командой: ```python -m pytest --alluredir=reports/ test_cases.py```
И формируем отчет: ```allure serve reports```
