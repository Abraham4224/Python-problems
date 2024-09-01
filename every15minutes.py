def every15minutes():
    horario=['am','pm']
    horas=['12','1','2','3','4','5','6','7','8','9','10','11']
    minutos=['00','15','30','45']
    for a in horario:
        for b in horas:
            for c in minutos:
                print(b,':',c,' ',a)
                
                
every15minutes()  
