import PyPDF2

# Oluşturulacak yeni PDF adı
yeni_pdf_adı = "OUTPUTPDFNAME.pdf"

# Kullanıcıdan seçilen sayfa aralıklarını al
sayfa_araliklari = [(35, 86), (90, 157), (161, 276), (299, 359), (435, 682), (713, 821)]  # Örneğin, 1-3 ve 5-7 aralıklarını alacak şekilde belirtildi

# Birleştirilecek PDF dosyasının adı
birlesim_pdf_adı = "destinationfortargetpdf"

# Seçilen sayfaları birleştir
def sayfaları_birlestir(pdf_adı, sayfa_araliklari):
    birlesim = PyPDF2.PdfFileReader(open(pdf_adı, "rb"))
    yeni_pdf = PyPDF2.PdfFileWriter()

    for aralik in sayfa_araliklari:
        basla, bitir = aralik
        for sayfa_numarasi in range(basla-1, bitir):
            sayfa = birlesim.getPage(sayfa_numarasi)
            yeni_pdf.addPage(sayfa)

    with open(yeni_pdf_adı, "wb") as yeni_pdf_dosyasi:
        yeni_pdf.write(yeni_pdf_dosyasi)

# Sayfaları birleştir
sayfaları_birlestir(birlesim_pdf_adı, sayfa_araliklari)

