# etudes

## Important vocabulary

### Compiler / Compilated language
Compilers are algoritms that "translate" high-level code to low-level code. They are used in compilated languages.

### GCC (GNU Compiler Collection)
GCC is an front-end to compile in many different languages, as you're going to see on this document. That means, when you call `gcc myfile.language` on terminal, GCC is going to analyze the file extension (`.language`) and call a proper compiler to that language. You can assure it uses the right compiler by flagging its library. You are able to name its output executable using flag `-o output_name`, but thats optional.
#### Examples
##### Fortran
`gcc -lgfortran myfile.f -o myfile.exe`
can replace 
`gfortran myfile.f -o myfile.exe`

### Interpreter / Interpretated language

### Level (high/low)

### Library

### Modules
Library?

## Languages

### C
#### Compilation
```
gcc main.c -o main
```
### C++
#### Compilation
Many people compile directly on g++, like:
```
g++ main.cpp -o main
```
But I prefer use gcc, which serves as a front-end, its gonna call `g++` anyway on backstage:
```
gcc main.cpp -o main
```
### Dart

#### Flutter
```
flutter run lib/dart.main
```
To run in a specific device, get its ID and then use run with `-d` parameter.
Listing devices
```
flutter devices
```
Then run specifying device
```
flutter run -d <DEVICE>
```

### Fortran
#### Compilation
Be careful, Fortran varies a lot on its versions.
Most people and tutorials recommend to compile Fortran stuff this way:
```
gfortran main.f -o main
```
But I do like this:
``` 
gcc -lgfortran main.f -o main
```


### GTK
#### Compilation:
I compile GTK on C using gcc as 
```
gcc `pkg-config --cflags gtk4` `pkg-config --cflags gtk4` main.c -o main
```
### Reference
I let you a great book recomendation for GTK programming:
- https://developer-old.gnome.org/gtkmm-tutorial/stable/index.html


### Python3
#### Running
No need to compile. One advantage of py3 is that you dont need to compile anything. It works something similar to shell script, interpretated in real time.
The basic .py execution on Linux and similars may be like this:
```
python3 myscript.py
```
#### Missing a module
It it tells you it could not import a module, you can easily install that with pip3:
```
pip3 install my_missing_module
```
