# ESP8266 Blink project with Micropython VSCode Pymaker extension

This is the tipical Hello World for ESP8266 framework.
Made to check that my developer setup is correctly configured.
This is a template project for future projects with with Micropython VSCode Pymaker extension for ESP8266 board.

## Project initialization guidelines

<https://unasguiasmas.wordpress.com/2021/05/08/visual-studio-code-micropython-esp/>

MicroPython Quick reference for the ESP8266

<http://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#deploying-the-firmware>

### ESP8266 Micropython instalation

Conect your board to USB computer port: (check COM port)

- Samsung Laptop [COM6]

1 . Erase 8266 flash memory:

```shell
esptool.exe --port COM6 erase_flash
```

2 . Install Micropython firmware:

```shell
esptool.exe --port COM3 --baud 460800 write_flash --flash_size=detect -fm dio 0 esp8266-20220618-v1.19.1.bin
```

### VScode pymaker extension

1. Install **_Node.js_** [https://nodejs.org/es/download/](https://nodejs.org/es/download/)
2. Install **_pymakr_** VScode extension

### My ESP8266 Board

<https://github.com/Freenove/Freenove_Basic_Starter_Kit_for_ESP8266>
