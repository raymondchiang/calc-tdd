@echo off
coverage run --source calc -m py.test
echo.
coverage report -m
