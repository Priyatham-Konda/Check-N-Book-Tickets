from datetime import datetime
import qrgenerator
def savefiles(pht):
    st = pht+str(datetime.now())+"\n"
    qrgenerator.qrgen(st[:len(st)])
    with open("busseats_log_file.txt","a") as bsf:
        bsf.writelines(st)