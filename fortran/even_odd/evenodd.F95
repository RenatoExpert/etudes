program evenodd
        integer numero
        integer teste
        character prop*4
        print *,'Tell me a number'
        read *,numero
        teste = numero - ((numero/2)*2)
        if (teste == 0) then
                prop = 'even'
        else if (teste == 1) then
                prop = 'odd'
        else
                prop = 'erro'
        end if
        print *,'Hmmm...',numero,'? That is '//prop//'!'
        end
