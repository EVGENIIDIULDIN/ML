��� ������� �� ��������� ������ Windows
#���������� ����������� ���������
C:\env\env32\Scripts\activate.bat
#������� � ������� � �����������
cd C:\wp\PYTHON\DETECTOR
# ����������� ����� �� ���������
pyuic5 design\HelpWindow3.ui -o HelpWindow.py
# ����������� exe-����
pyinstaller --onefile main.py
pyinstaller --onefile C:\wp\PYTHON\DETECTOR\main.py
pyinstaller --onefile C:\TMP\DETECT\main.py
P.S.
pip3 install pyinstaller

�������� ����� � ������� ��������
python -m venv env32
C:\env32\Scripts\activate.bat
��������� ����������� ����������
pip install opencv-python
pip install opencv-contrib-python
pip install Pillow
pip install PyQt5
pip install pyinstaller

pip install PyQt5Designer
pip3 install pyinstaller




pip install pyinstaller ERROR - solve:

#���������� �������� ������ pip �� 18.1:
python -m pip install pip==18.1
#����� ���������� pyinstaller:
pip install pyinstaller
#����� �������� pip �� ��������� ������:
python -m pip install --upgrade pip