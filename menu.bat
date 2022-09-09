@echo off

set hour=%time:~0,2%
if "%hour:~0,1%" == " " set hour=0%hour:~1,1%
set min=%time:~3,2%
if "%min:~0,1%" == " " set min=0%min:~1,1%
set secs=%time:~6,2%
if "%secs:~0,1%" == " " set secs=0%secs:~1,1%

:start
title BROWAR - MENU
cls
echo ---------------------------------------
echo               MENU BROWAR
echo ---------------------------------------

echo.
echo 1) Opis programu
echo 2) Uruchom algorytm i utworz raport
echo 3) Utworz backup
echo 4) Wyswietl raport
echo 5) Wyswietl dokumentacje
echo 6) Wyjscie
echo.
set /p opcja=wybor: 
if %opcja%==1 goto opcja1
if %opcja%==2 goto opcja2
if %opcja%==3 goto opcja3
if %opcja%==4 goto opcja4
if %opcja%==5 goto opcja5
if %opcja%==6 exit
goto zly_wybor

:opcja1
cls
echo Tytul projektu: "Gdzie zbudowac browar?" - VII OI
echo Autor: Antoni Zuber
echo - Program ma na celu obliczyc minimalny koszt dziennego transportu piwa pomiedzy miastami
echo oraz miasto, w ktorym powinien powstac browar, by ten koszt byl najmniejszy.
echo - Aby skorzysac z opcji backup, najpierw nalezy utworzyc nowy raport.
echo - W celu poprawnego dzialania programu, nalezy upewnic sie, ze istnije
echo co najmniej jeden plik wejsciowy broin*.txt.
echo.
echo Aby wrocic do menu - nacisnij ENTER
pause
goto start

:opcja2
cls
echo Plik python1.py odpowiedzialny za algorytm rozpoczyna prace...
"C:\Users\Antek\AppData\Local\Programs\Python\Python39\python.exe" "C:\Users\Antek\PycharmProjects\BROWAR\python1.py"
echo Plik python2.py tworzy raport...
"C:\Users\Antek\AppData\Local\Programs\Python\Python39\python.exe" "C:\Users\Antek\PycharmProjects\BROWAR\python2.py"
echo Aby wrocic do menu - nacisnij ENTER
pause
goto start

:opcja3
cls
echo Tworze backup...
IF EXIST raport.html copy raport.html BACKUP\%hour%-%min%-%secs%_%date%_raport.html
echo.
echo Aby wrocic do menu - nacisnij ENTER
pause
goto start

:opcja4
cls
echo Otwieram raport...
start raport.html
echo.
echo Aby wrocic do menu - nacisnij ENTER
pause
goto start

:opcja5
cls
echo Otwieram plik z dokumentacja...
start dokumentacja.pdf
echo.
echo Aby wrocic do menu - nacisnij ENTER
pause
goto start

:zly_wybor
echo Wybierz poprawny numer z menu!
echo.
echo Aby wrocic do menu - nacisnij ENTER
pause
goto start