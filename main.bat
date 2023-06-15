@echo off
title Github bot profile viewer by otema
echo Elija un navegador:
echo 1. Chrome
echo 2. Firefox
echo.

:bucle
color a
set /p opcion=Seleccione una opcion: 

if "%opcion%"=="1" (
    cls
    python chrome.py
) else if "%opcion%"=="2" (
    cls
    python firefox.py
) else (
    echo Opcion no valida!!
    echo.
    goto bucle
)


