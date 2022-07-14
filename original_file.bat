cls
C:\"Program Files"\STMicroelectronics\STM32Cube\STM32CubeProgrammer\bin\STM32_Programmer_CLI.exe -c port=SWD -sn 003600144741500520383733 freq=4000 -e all
echo ghgjhg

rem C:\"Program Files"\STMicroelectronics\STM32Cube\STM32CubeProgrammer\binSTM32_Programmer_CLI.exe -c port=SWD freq=4000 -e all
rem STM32_Programmer_CLI.exe -c port=SWD freq=4000 -e all
TIMEOUT 3
rem C:\"Program Files"\STMicroelectronics\STM32Cube\STM32CubeProgrammer\binSTM32_Programmer_CLI.exe -c port=SWD freq=4000 -e all

C:\"Program Files"\STMicroelectronics\STM32Cube\STM32CubeProgrammer\bin\STM32_Programmer_CLI.exe -c port=SWD -sn 003600144741500520383733 freq=4000 -w X:\Software\Eureka\Version 2.1.0.3\Slaves\twine-winder-g743-master\Debug\twine-winder-g743-master.bin 0x08000000 -rst
pause
echo "Done!"