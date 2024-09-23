import streamlit as st
import datetime
import aspose.words as aw
from io import BytesIO

def compare_pdf_files(file_1, file_2):
    try:
        pdf_1, pdf_2 = aw.Document(file_1), aw.Document(file_2)
        pdf_1.accept_all_revisions()
        pdf_2.accept_all_revisions()
        pdf_1.compare(pdf_2, 'Author', datetime.datetime.now())
        
        pdf_diff = BytesIO()
        pdf_1.save(pdf_diff, aw.SaveFormat.PDF)
        # Rewind the stream to the beginning for download
        pdf_diff.seek(0)  

        st.success('Karşılaştırma tamamlandı! Aşağıdaki sonucu indirin:')
        st.download_button(label="İndir", data=pdf_diff, file_name="pdf_ciktisi.pdf", mime="application/pdf")
    except Exception as e:
        st.error(f"Error occurred: {e}")

st.title("PDF Karşılaştırma Aracı")
st.write("İçeriklerini karşılaştırmak için iki PDF dosyası yükleyin.")

pdf_file_1 = st.file_uploader("İlk PDF'yi yükle", type=["pdf"])
pdf_file_2 = st.file_uploader("İkinci PDF'yi yükle", type=["pdf"])

if pdf_file_1 and pdf_file_2:
    if st.button("Karşılaştır"):
        compare_pdf_files(pdf_file_1, pdf_file_2)

st.markdown("---")
st.write("Bu web sayfası Egemen Eroğlu tarafından oluşturulmuştur.")