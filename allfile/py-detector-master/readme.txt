ВСЕ КОМАНДЫ ИЗ КОМАНДНОЙ СТРОКИ Windows
#активируем виртуальное окружение
C:\env\env32\Scripts\activate.bat
#заходим в каталог с исходниками
cd C:\wp\PYTHON\DETECTOR
# компилируем форму из дизайнера
pyuic5 design\HelpWindow3.ui -o HelpWindow.py
# компилируем exe-файл
pyinstaller --onefile main.py
pyinstaller --onefile C:\wp\PYTHON\DETECTOR\main.py
pyinstaller --onefile C:\TMP\DETECT\main.py
P.S.
pip3 install pyinstaller

создание среды в текущем каталоге
python -m venv env32
C:\env32\Scripts\activate.bat
добавляем необходимые расширения
pip install opencv-python
pip install opencv-contrib-python
pip install Pillow
pip install PyQt5
pip install pyinstaller

pip install PyQt5Designer
pip3 install pyinstaller




pip install pyinstaller ERROR - solve:

#Попробуйте откатить версию pip до 18.1:
python -m pip install pip==18.1
#потом установить pyinstaller:
pip install pyinstaller
#потом обновить pip до последней версии:
python -m pip install --upgrade pip