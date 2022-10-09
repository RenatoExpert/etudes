# Etudes
A repository with many study exercises and examples in many languages

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

### C ncurses
#### Compilation
```
gcc -lncurses main.c -o main
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

### Dart Flutter

#### Compile
Flutter let you compile for many different devices. From mobile to web or desktop.
An example of building apk (for android).
```
flutter build apk
```
#### Running
You may run and debug directly into your target.
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
Fortran has a lot on its versions, you can find a lot of documentation on F77 and F95. I recommend you to prefer to compile in the newest syntax (2018), since the newer versions have a lot of improvements. Books on F95 are still useful anyway.
#### Compilation
``` 
gcc -lgfortran main.f95 -o main
```
#### Reference
- Its wikipedia article is just perfect: 
https://en.wikipedia.org/wiki/Fortran#Evolution
- It has also its own wiki:
https://fortranwiki.org/
- I found some good books on this link:
https://www.fortranplus.co.uk/fortranplus-books/

### GTK
#### Compilation:
I compile GTK on C using gcc as 
```
gcc `pkg-config --cflags gtk4` `pkg-config --cflags gtk4` main.c -o main
```
### Reference
I let you a great book recomendation for GTK programming:
- https://developer-old.gnome.org/gtkmm-tutorial/stable/index.html

### Java
#### Compilation:
```
javac myfile.java
```
Its going to generate *.class* java binary files.
#### Running:
After compiled, run *.class* files without its extension.
For example, if you have *myapp.class*, you may run it with:
```
java myapp
```

### Javascript
#### Running:
```
node myapp.js
```

### PKG
Generate *.zst* packages, handable by pacman on Arch-based distros.
#### Build
Make sure you have a PKGBUILD file in your current directory
```
makepkg
```
Build __and__ autoinstall with `-i` flag:
```
makepkg -i
```


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

### Rust
#### Compiling
```
rustc myscript.rs
```

### Rust Cargo
#### Compiling
```
cargo run myapp
```

