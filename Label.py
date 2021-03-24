

from PySide2.QtCore import *
from PySide2.QtGui import * 
from PySide2.QtPrintSupport import QPrintDialog, QPrinter
from PySide2.QtWidgets import QDialog
from qrcode.constants import ERROR_CORRECT_H
from LaelDialog import Ui_LabelWindow
import zpl
import io
from data.connection import *
from datetime import date
import qrcode
from PIL import Image
from PySide2.QtWidgets import QWidget
class Label(QDialog, Ui_LabelWindow):
    def __init__(self, listInfo, results, isMedia,  parent= None):
        self.listInfo = listInfo
        self.results = results
        self.isMedia = isMedia
        super(Label, self).__init__(parent)
        self.setupUi(self)
        self.image = QImage()
        self.dirty = False
        self.filename = None
        self.connection = sqlite3con()
        self.isFlam = False 
        self.isHHM = False
        self.isTox = False 
        self.isHaz = False
        self.isResp =False 
        self.isCorr = False
        self.isEnv  = False
        self.corr.clear()
        self.flam.clear()
        self.hhmIcon.clear()
        self.tox.clear()
        self.resp.clear()
        self.non.clear()
        self.env.clear()
        self.haz.clear()
        self.corrImg = QImage("corrosive.png")
        self.corrPix = QPixmap(self.corrImg)
        self.flamImg = QImage("flammable.png")
        self.flamPix = QPixmap(self.flamImg)
        self.respImg = QImage("respiratory.png")
        self.respPix = QPixmap(self.respImg)
        self.envImg = QImage("environment.png")
        self.envPix = QPixmap(self.envImg)
        self.nonImg = QImage("Non haz.png")
        self.nonPix = QPixmap(self.nonImg)
        self.toxImg = QImage("toxic.png")
        self.toxPix = QPixmap(self.toxImg)
        self.hhmImg = QImage("HHM.png")
        self.hhmPix = QPixmap(self.hhmImg)
        self.hazImg = QImage("warning.png")
        self.hazPix = QPixmap(self.hazImg)
        self.dateLabel.setText(str(date.today()))
        self.batch_title.setText(listInfo[0])
        self.emailLabel.setText("Email: " + listInfo[1])
        self.lotLabel.setText("Lot: "+ listInfo[2])
        self.lot2.setText("Lot: "+ listInfo[2])
        self.deliveryLabel.setText("Drop Zone: " + listInfo [3])
        self.expLabel.setText("Exp: "+listInfo[4])
        self.dialog = None
        if self.isMedia:
            self.conLabel.setText("pCO2: " + listInfo[7]+ "mmHg/ Osmolality: "+ listInfo[8] + "mOsm/kg" )
        else:
            self.conLabel.setText("Conductivity: " + listInfo[7]+"mS/cm @ " + listInfo[8]+ "C")
        self.pHLabel.setText("pH: " + listInfo[5]+" @ "+listInfo[6] + "C")
       
       
        self.printer = None
        self.buttonBox.accepted.connect(self.print_preview_dialog)
        img = self.createBarcode( listInfo[1], listInfo[0],listInfo[2])
        self.qrLabel.setPixmap(self.pil2pixmap(img))
        self.qrLabel.setScaledContents(True)
        self.checkShit(listInfo[0], listInfo[5])
        self.doTheChemicals(self.results)
    def doTheChemicals(self, results):
        """changeDict ={"NaOH": "Sodium Hydroxide", "NaCl":"Sodium Chloride", "PS20": "Polysorbate 20", "PS80": "Polysorbate 80", "CHAPS":"3-((3-cholamidopropyl) dimethylammonio)-1-propanesulfonate(CHAPS)", "IGF-1": "Insulin Growth Factor - 1", "DTPA":"Diethylenetriamine Pentaacetate(DTPA)", "SDS": "Sodium Dodecyl Sulfate", "HFIP":"Hexafluoroisopropanol(HFIP)", "HPMC": "Hydroxymethylcellulose", "HPBCD": "2-Hydroxypropyl-beta-cyclodextrin", " PEG": " Polyethylene Glycol(PEG)","EDTA": "Ethylenediaminetetraacetic acid(EDTA)", "EGTA": "ethylene glycol-bis('-aminoethyl ether)-N,N,N',N'-tetraacetic acid(EGTA)", "Tris":"tris(hydroxymethyl)aminomethane(Tris)", "MES": "2-(N-morpholino)ethanesulfonic acid(MES)", "MOPS":"3-morpholinopropane-1-sulfonic acid(MOPS)", "HEPES": "2-[4-(2-hydroxyethyl)piperazin-1-yl]ethanesulfonic acid(HEPES)", "HCl": "Hydrochloric Acid", "H2O": "Dihydrogen Monoxide(H2O)"}
        reslist = results.split(",")
        reslist = [changeDict.get(item, item) for item in reslist]
        self.results = ", ".join(reslist)"""
        giffy = checkIfResult(self.connection, results)
        self.resuls.setText(giffy)
    def createBarcode(self, batch, email, lot):
        codeStr = batch + "*" + email + "*" + lot
        qrCode = qrcode.QRCode(
            error_correction=ERROR_CORRECT_H,
        )
        qrCode.add_data(codeStr)
        qrCode.make()
        img = qrCode.make_image()
        return img
    def pil2pixmap(self, image):
        bytes_img = io.BytesIO()
        image.save(bytes_img, format='JPEG')

        qimg = QImage()
        qimg.loadFromData(bytes_img.getvalue())

        return QPixmap.fromImage(qimg)
    def print_preview_dialog(self):
        sshot = QWidget.grab(self.frame)
        sshot2 = QWidget.grab(self.frame2)
        sshot.save('sshot.png')
        sshot2.save('sshot2.png')
        

        #Instantiate print image object
        sshot = sshot.toImage()
        sshot.allGray()
        sshot.setDotsPerMeterX(7992)
        sshot.setDotsPerMeterY(7992)
        sshot.save('2sshot.png')
        sshot2 = sshot2.toImage()
        sshot2.setDotsPerMeterX(7992)
        sshot2.setDotsPerMeterY(7992)
        screenshots = [sshot, sshot2]
        printer=QPrinter(QPrinter.HighResolution)
        paperSize = QPageSize(QSizeF(4.05, 2.05), QPageSize.Inch)
        printer.setPageSize(paperSize)
        #Print window pops up
        
        printDialog=QPrintDialog(printer,self)
        
        if printDialog.exec_():
            for shot in screenshots: 

                painter=QPainter(printer)
                painter.begin(printer)
            #Instantiated view window
                rect=painter.viewport()
            #Get the size of the picture
                size=shot.size()

                size.scale(rect.size(),Qt.KeepAspectRatio)
            #Set the properties of the view window
                painter.setViewport(rect.x(),rect.y(),size.width(),size.height())

            #Set the size of the window to the size of the picture, and draw the picture in the window
                painter.setWindow(shot.rect())
                painter.drawImage(0,0,shot)
                painter.end()
                painter
              
       
    def zebraPrint(self):
        l = zpl.Label(53.30, 104.10, 12)
        height = 0
        width= 104.10
        l.origin(0, 53.3)
        l.write_graphic(Image.open('sshot.png'), width)
        l.endorigin()
        print(l.dumpZPL())
        l.preview()

    def printImage(image, printer, scaleToFillPage=False): 
        dialog = QPrintDialog(printer) 
        if dialog.exec_():
            painter = QPainter(printer) 
            painter.setRenderHint(QPainter.Antialiasing) 
            rect = painter.viewport() 
            size = image.size()
            size.scale(rect.size(), Qt.KeepAspectRatio) 
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
        if scaleToFillPage:
            painter.setWindow(image.rect())
        if isinstance(image, QPixmap):
            painter.drawPixmap(0, 0, image) 
        else:
            painter.drawImage(0, 0, image)
    def checkShit(self, batch, pH):
        try:
            fpH = float(pH)
            if fpH <= 5.5 or fpH >= 10.5:
                self.isCorr = True
                img = QImage("corrosive.png")
                corrpix = QPixmap(img)
                self.corr.setPixmap(corrpix)
        except:
            self.pHLabel.setVisible(False)

        corrosive_list = createCorrosiveList(self.connection)
        flam_list = createFlammableList(self.connection) 
        """['Acetonitrile', 'Acetone', 'Methanol', 'Formic Acid', 'Sodium Dodecyl Sulfate', 'SDS', 'Ethanol', 'Sodium Cyanoborohydride', 'Sodium Perchlorate']"""
        tox_list = createToxicList(self.connection)
        """['Methanol', 'Formic Acid', 'Ethylmaleidmide', 'Azide', 'Sodium Cyanoborohydride']"""
        env_list = createEnvironmentList(self.connection)
        """['Azide', 'Sodium Cyanoborohydride']"""
        haz_list = createHazardousList(self.connection)
        """['Benzyl Alcohol', 'EDTA', 'Ammonium Acetate', 'Ammonium Hydroxide', 'Acetone', 'DMSO', 'Guanidine', 'Methanol', 'Ammonium Formate', 'Ethylmaleidmide', 'Sodium Sulfate', 'Sodium Dodecyl Sulfate', 'Urea', 'Tris', 'Sodium Perchlorate']"""
        resp_list = createRespiratoryList(self.connection)
   
        hhm_list = ['Azide', 'Sodium Cyanoborohydride', 'Sodium Perchlorate']
        createHHMList(self.connection) 
      
        if any(ele in batch for ele in corrosive_list):
            self.isCorr = True
            self.corr.setPixmap(self.corrPix)

        if any(ele in batch for ele in flam_list):
            self.isFlam = True
            self.flam.setPixmap(self.flamPix)
        if any(ele in batch for ele in tox_list):
            self.isTox = True
            self.tox.setPixmap(self.toxPix)
        if any(ele in batch for ele in resp_list):
            self.isResp = True
            self.resp.setPixmap(self.respPix)
        if any(ele in batch for ele in env_list):
            self.isEnv = True
            self.env.setPixmap(self.envPix)
        if any(ele in batch for ele in hhm_list):
            self.isHHM = True
            self.hhmIcon.setPixmap(self.hhmPix)
        if any(ele in batch for ele in haz_list):
            self.isHaz = True
            self.haz.setPixmap(self.hazPix)
        if self.isFlam is False  and self.isHHM is False  and self.isTox is False and self.isHaz is False and self.isResp is False and self.isCorr is False and self.isEnv is False:
            self.non.setPixmap(self.nonPix)

            
 
 
 
 




