## 28C16 EEPROM Burner Client

This is a simple program to be used in conjunction with [this](https://github.com/jasonalexander-ja/PicoEEPROMBurner)
program for the Raspberry Pi Pico to burn the 28C16 - 28C256 and compatilble EEPROMs with binary format files specified over 
the command line. 

To use simple run; 

`python main.py [com port Pico is on] [path to binary file]`

### Dev/Debug

Setup with useful VSC, Git configuration and libraries. 

To start:
```
    ProjectRoot>python -m venv .
    ProjectRoot>.\Scipts\activate
    ProjectRoot>pip install -r requirements.txt
```

To test:
```
    ProjectRoot>pytest
```

To generate coverage documentation:
```
    ProjectRoot>coverage run -m pytest
```

To view coverage report as a HTML document:
```
    ProjectRoot>coverage html
```

Remember when revisiting after the IDE or terminal has been restarted, restart the env;

<sub>On Linux/Mac this will be `./bin/activate`, on M1 Mac use `source ./bin/activate.csh` from a csh terminal</sub>
```
    ProjectRoot>.\Scipts\activate
```
When the env is active you should see the project name before the directory in ther terminal;
```
    (ProjectName) ProjectName>
```

To update the dependancy list, use;
```
    ProjectName>pip install -r requirements.txt 
```
To install dependancies, use;
```
    ProjectRoot>pip install -r requirements.txt
```
