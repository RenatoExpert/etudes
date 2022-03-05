# etudes

## C
### Compilation
```
gcc main.c -o main
```
## C++
### Compilation
Many people compile like this
```
g++ main.cpp -o main
```
But I do like this:
```
gcc main.cpp -o main
```

## Fortran
### Compilation
Be careful, Fortran varies a lot on its versions.
Most people and tutorials recommend to compile Fortran stuff this way:
```
gfortran main.f -o main
```
But I do like this:
``` 
gcc -lgfortran main.f -o main
```


## GTK
### Compilation:
I compile GTK on C using gcc as 
```
gcc `pkg-config --cflags gtk4` `pkg-config --cflags gtk4` main.c -o main
```
### Reference
I let you a great book recomendation for GTK programming:
- https://developer-old.gnome.org/gtkmm-tutorial/stable/index.html
