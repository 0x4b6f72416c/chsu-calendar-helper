@echo  off
set /p  var=< requirements.txt
pip install %var%
