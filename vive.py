from ast import Global
import os



def console_vive(dannie_t, vid, nach_spiska, kon_spiska):
    os.system('cls' if os.name == 'nt' else 'clear')

    stolbN=""
    gorizontLine=""
    strokaDannix=""
    otstupID=0
    otstupF=0
    otstupI=0
    otstupOT=0
    otstupNT=0
    maxSimvol=0

    if(vid==0):

        for i in range(nach_spiska, kon_spiska):
            n = i
            if(otstupID<len(f"{i}")):
                    otstupID=len(f"{i}")
            if(i<len(dannie_t)):
                if(otstupF<len(f"{dannie_t[n]['Заголовок']}")):
                    otstupF=len(f"{dannie_t[n]['Заголовок']}")
                if(otstupI<len(f"{dannie_t[n]['Описание']}")):
                    otstupI=len(f"{dannie_t[n]['Описание']}")
                if(otstupOT<len(f"{dannie_t[n]['Дата создания']}")):
                    otstupOT=len(f"{dannie_t[n]['Дата создания']}")
                if(otstupNT<len(f"{dannie_t[n]['Дата изменения']}")):
                    otstupNT=len(f"{dannie_t[n]['Дата изменения']}")
                n+=1

        for i in range(nach_spiska, kon_spiska):
            strokaDannix=''
            n = i
            if(i<len(dannie_t)):
                strokaDannix= f"|{i}|{dannie_t[n]['Заголовок']}|{dannie_t[n]['Описание']}|{dannie_t[n]['Дата создания']}|{dannie_t[n]['Дата изменения']}|"
                if(maxSimvol<=len(strokaDannix)):
                    maxSimvol=len(strokaDannix)
                n+=1


        strokaDannix= '|','ID','|','Заголовок', ' '*(otstupF-len("Заголовок")),'|','Описание', ' '*(otstupI-len("Описание")),'|','Дата создания', ' '*(otstupOT-len("Дата создания")),'|','Дата изменения', ' '*(otstupNT-len("Дата изменения")),'|'
        
        maxSimvol=maxSimvol+17

        gorizontLine='-'*maxSimvol
        print(gorizontLine)
        print(*strokaDannix)
        print(gorizontLine)
        for i in range(nach_spiska, kon_spiska):
            n = i
            if(i<len(dannie_t)):
                strokaDannix= '|', i, ' '*(otstupID-len(f"{i}")), '|', dannie_t[n]['Заголовок'], ' '*(otstupF-len(f"{dannie_t[n]['Заголовок']}")), '|', dannie_t[n]['Описание'], ' '*(otstupI-len(f"{dannie_t[n]['Описание']}")), '|', dannie_t[n]['Дата создания'], ' '*(otstupOT-len(f"{dannie_t[n]['Дата создания']}")), '|', dannie_t[n]['Дата изменения'], ' '*(otstupNT-len(f"{dannie_t[n]['Дата изменения']}")), '|'
                print(*strokaDannix)
                print(gorizontLine)
                n+=1
            elif(i>=len(dannie_t)):
                print ('|', i, ' '*(otstupID-len(f"{i}")), '|', ' '*(otstupF+1), '|', ' '*(otstupI+1),'|',' '*(otstupOT+1),'|',' '*(otstupNT+1),'|')
                print(gorizontLine)
    elif(vid==1):

        for i in range(nach_spiska, kon_spiska):
            strokaDannix=''
            n = i
            if(i<len(dannie_t)):
                strokaDannix= f"| Запись №  {i} | Заголовок записи -- {dannie_t[n]['Заголовок']} |"
                if(maxSimvol<=len(strokaDannix)):
                    maxSimvol=len(strokaDannix)
                strokaDannix= f"| {dannie_t[n]['Описание']} |"
                if(maxSimvol<=len(strokaDannix)):
                    maxSimvol=len(strokaDannix)
                strokaDannix= f"| Дата создания - {dannie_t[n]['Дата создания']} | Дата изменения - {dannie_t[n]['Дата изменения']} |"
                if(maxSimvol<=len(strokaDannix)):
                    maxSimvol=len(strokaDannix)
                n+=1

        maxSimvol=maxSimvol+6

        gorizontLine='-'*maxSimvol

        for i in range(nach_spiska, kon_spiska):
            n = i
            if(i<len(dannie_t)):
                strokaDannix= '|', ' '*(int(maxSimvol/4)-len(f"Запись №  {i}")), 'Запись №  ', i, ' '*(int(maxSimvol/4)-len(f"Заголовок записи -- {dannie_t[n]['Заголовок']}")), '|', ' '*(int(maxSimvol/4)-len(f"Запись №  {i}")), 'Заголовок записи -- ', dannie_t[n]['Заголовок'],' '*(int(maxSimvol/4)-len(f"Заголовок записи -- {dannie_t[n]['Заголовок']}")), '|' 
                print(gorizontLine)
                print(*strokaDannix)
                print(gorizontLine)
                strokaDannix= '|', ' '*(int(maxSimvol/2)-len(f"{dannie_t[n]['Описание']}")+1), dannie_t[n]['Описание'], ' '*(int(maxSimvol/2)-len(f"{dannie_t[n]['Описание']}")+1), '|'
                print(*strokaDannix)
                print(gorizontLine)
                strokaDannix= '|', ' '*(int(maxSimvol/4)-len(f"Дата создания - {dannie_t[n]['Дата создания']}")), 'Дата создания - ', dannie_t[n]['Дата создания'], ' '*(int(maxSimvol/4)-len(f"Дата создания - {dannie_t[n]['Дата создания']}")), '|', ' '*(int(maxSimvol/4)-len(f"Дата изменения - {dannie_t[n]['Дата изменения']}")), 'Дата изменения - ', dannie_t[n]['Дата изменения'], ' '*(int(maxSimvol/4)-len(f"Дата изменения - {dannie_t[n]['Дата изменения']}")), '|'
                print(*strokaDannix)
                print(gorizontLine)
                n+=1
            elif(i>=len(dannie_t)):
                print ('|'+' '*2, i, ' '*3+'|'+' '*15, ' ', ' '*15+'|'+' '*13, ' ', ' '*13+'|')
                print('-'*70)

def consol_comand_user():
    consol_comanda = input('введите команду - ')
    return consol_comanda

def dobav_zapis_book():
    dobav_zapis = int(input('введите номер ID для создания записи - '))
    return dobav_zapis

def zapis_tel_book():
    zapis_tel = input('введите "заголовок" / "описание" через знак"/" - ')
    return zapis_tel

def izmenit_zagolovok_zapisi(dannie_t, n):
    izmenit_zagolovok = input(f"заголовок-|-{dannie_t[n]['Заголовок']}-|-изменить на :")
    return izmenit_zagolovok

def izmenit_opisanie_zapisi(dannie_t, n):
    izmenit_opisanie = input(f"описание записи-|-{dannie_t[n]['Описание']}-|-изменить на :")
    return izmenit_opisanie