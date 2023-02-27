import json
import vive
from datetime import datetime


consol_comanda = ''
dannue_tel_book = ''
id_zapisi = 0
slovar_zapisi = {}
vid_otobragen = 0
n_nach_cpiska = 0
n_konc_spiska = 0
iz_zag_zaps=0
iz_osn_zaps=0
id_iz_zaps=0
data_sozdaniu=""
data_izmen=""
time=""

def init(comanda):
    global consol_comanda
    global dannue_tel_book
    global id_zapisi
    global slovar_zapisi
    global vid_otobragen
    global n_nach_cpiska
    global n_konc_spiska
    global iz_zag_zaps
    global id_iz_zaps
    global iz_osn_zaps
    global data_sozdaniu
    global data_izmen
    global time
    consol_comanda = comanda
    
    if(consol_comanda=="пуск"):
        dannue_tel_book = read_fail()
        n_konc_spiska = len(dannue_tel_book)
        consol_comanda = ''
    elif(consol_comanda.split()[0] =="строк"):
        n_nach_cpiska=0
        n_konc_spiska = int(consol_comanda.split()[1])
        consol_comanda = ''
        
    elif(consol_comanda=="обновить"):
        dannue_tel_book = read_fail()
        consol_comanda = ''
    elif(consol_comanda=="сохранить"):
        wread_fail()
        consol_comanda = ''
    elif(consol_comanda=="назад"):
        vid_otobragen = 0
        n_nach_cpiska=0
        n_konc_spiska = len(dannue_tel_book)
        iz_zag_zaps=0
        iz_osn_zaps=0
        consol_comanda = ''
        
    elif((consol_comanda.split()[0]+' '+consol_comanda.split()[1])=="показать запись"):
        n_nach_cpiska=(int(consol_comanda.split()[2]))
        n_konc_spiska=(int(consol_comanda.split()[2]))+1
        id_iz_zaps=n_nach_cpiska
        vid_otobragen = 1
        iz_zag_zaps=1
        iz_osn_zaps=2
        consol_comanda = ''

    elif((consol_comanda.split()[0]+' '+consol_comanda.split()[1])=="показать записи"):
        n_nach_cpiska=(int(consol_comanda.split()[2]))
        n_konc_spiska=(int(consol_comanda.split()[3]))+1
        consol_comanda = ''
    elif(consol_comanda=="показать все записи"):
        n_nach_cpiska=0
        n_konc_spiska=len(dannue_tel_book)
        consol_comanda = ''
    elif(consol_comanda=="добавить запись"):
        
        data_sozdaniu=rid_time()
        id_zapisi = vive.dobav_zapis_book()
        vvedenna_zapis=vive.zapis_tel_book()
        if(0<=id_zapisi<=len(dannue_tel_book)):
            slovar_zapisi = {'Заголовок': vvedenna_zapis.split("/")[0] , 
                            'Описание': vvedenna_zapis.split("/")[1], 
                            'Дата создания': data_sozdaniu, 
                            'Дата изменения': data_sozdaniu}
            dannue_tel_book.insert(id_zapisi, slovar_zapisi)
        if(id_zapisi>len(dannue_tel_book)):
            slovar_zapisi = {'Заголовок': vvedenna_zapis.split("/")[0] , 
                            'Описание': vvedenna_zapis.split("/")[1], 
                            'Дата создания': data_sozdaniu, 
                            'Дата изменения': data_sozdaniu}
            dannue_tel_book.append(slovar_zapisi)
        consol_comanda = ''
    elif((consol_comanda.split()[0]+' '+consol_comanda.split()[1])=="удалить запись"):
        del_index = int(consol_comanda.split()[2])
        if(del_index<=len(dannue_tel_book)):
            dannue_tel_book.pop(del_index)
        consol_comanda = ''
    
    elif(consol_comanda=="изменить заголовок"):
        data_izmen=rid_time()
        if(iz_zag_zaps==1):

            vvedenna_zapis=vive.izmenit_zagolovok_zapisi(dannue_tel_book,id_iz_zaps)
            slovar_zapisi = {'Заголовок': vvedenna_zapis, 
                                'Описание': dannue_tel_book[id_iz_zaps]['Описание'], 
                                'Дата создания': dannue_tel_book[id_iz_zaps]['Дата создания'], 
                                'Дата изменения': data_izmen}
            del_index=id_iz_zaps
            if(del_index<=len(dannue_tel_book)):
                dannue_tel_book.pop(del_index)
            dannue_tel_book.insert(id_iz_zaps, slovar_zapisi)

    elif(consol_comanda=="редактировать описание"):
        data_izmen=rid_time()
        if(iz_osn_zaps==2):
            vvedenna_zapis=vive.izmenit_opisanie_zapisi(dannue_tel_book,id_iz_zaps)
            slovar_zapisi = {'Заголовок': dannue_tel_book[id_iz_zaps]['Заголовок'], 
                                'Описание': vvedenna_zapis, 
                                'Дата создания': dannue_tel_book[id_iz_zaps]['Дата создания'], 
                                'Дата изменения': data_izmen}
            del_index=id_iz_zaps
            if(del_index<=len(dannue_tel_book)):
                dannue_tel_book.pop(del_index)
            dannue_tel_book.insert(id_iz_zaps, slovar_zapisi)

def read_fail():
    baza_dannix = ''
    with open("data.json", "r") as read_file: 
        baza_dannix = json.load(read_file)
    return baza_dannix

def wread_fail():
    baza_dannix = ''
    with open("data.json", "w") as write_file:
        json.dump(dannue_tel_book, write_file)
    return baza_dannix

def rid_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S %D")
    time=f"{current_time}"
    return time
