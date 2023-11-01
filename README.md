# trashAI
Нейроная сеть созданная коллективом уеников 10 класса Гимназии №17 города Перми для решения проблемы автоматического подсчета типов ТБО

# Установка
## Linux
```
git clone https://github.com/sobakaruzhaya/trashAI/
cd trashAI
sudo apt-get install python3-venv
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
## Windows
```
git clone https://github.com/sobakaruzhaya/trashAI/
cd trashAI
python -m venv env
./env/Scripts/Activate 
pip install -r requirements.txt
```

# Как пользоваться
1. Создайте каталог images и перенесите в него картики всех фреймов
2. Запустите main.py командой: python3 main.py

# Как работает
1. Из набора фреймов, которых пользователь вставил в images/, создаётся файл 1.mp4 с частотой обновления 25 кадров в секунду
2. Для каждого фрейма в каталог frames_output/ сохраняется .txt файл в котором записано количество объектов каждого класса
3. Создаётся mp4 файл на котором видны результаты обнаружений всех классов 
4. Нейросеть на основе модели определяет количество объектов каждого класса 
