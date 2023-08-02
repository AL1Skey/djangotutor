@echo off

set /p login= " user:"

workon %login%

if errorlevel 1 (
    mkvirtualenv %login%
)

pause