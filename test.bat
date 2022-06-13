cls
C:\"Program Files"\STMicroelectronics\STM32Cube\STM32CubeProgrammer\bin\STM32_Programmer_CLI.exe -c port=SWD freq=4000 -e all
echo ghgjhg

rem C:\"Program Files"\STMicroelectronics\STM32Cube\STM32CubeProgrammer\binSTM32_Programmer_CLI.exe -c port=SWD freq=4000 -e all
rem STM32_Programmer_CLI.exe -c port=SWD freq=4000 -e all
TIMEOUT 3
rem C:\"Program Files"\STMicroelectronics\STM32Cube\STM32CubeProgrammer\binSTM32_Programmer_CLI.exe -c port=SWD freq=4000 -e all

C:\"Program Files"\STMicroelectronics\STM32Cube\STM32CubeProgrammer\bin\STM32_Programmer_CLI.exe -c port=SWD freq=4000 -w filepath 0x08000000 paus
pause
C:\"Program Files"\STMicroelectronics\STM32Cube\STM32CubeProgrammer\bin\STM32_Programmer_CLI.exe -c port=SWD freq=4000 -rst