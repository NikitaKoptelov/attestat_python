import zapis_book
import vive

def pusk_prog():
    comanda_cs = vive.consol_comand_user()
    zapis_book.init(comanda_cs)
    vive.console_vive(zapis_book.dannue_tel_book, zapis_book.vid_otobragen, zapis_book.n_nach_cpiska, zapis_book.n_konc_spiska)
    
        

