program inout
        character name*20
        print *,' Type in your name, up to 20 characters'
        read *,name
        print *,' Be welcome Mr(s)',name
        integer age
        print *,' How old are you, Mr(s)'//name//'?'
        read *,age
        print *,'Oh! You are so young!'
end

