import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename
import fire

class Reader(object):
        
    def AudioStart(self, page_number):

        book = askopenfilename()
        pdfreader = PyPDF2.PdfFileReader(book)
        pages = pdfreader.numPages
        player = pyttsx3.init()
        
        last_page = 0
        player.say(f"You have decided to start reading from page {page_number}")
        for num in range(page_number, pages):
            player.say(f"Now reading page {num}")
            page = pdfreader.getPage(num)
            text = page.extractText()
            player.say(text)
            player.runAndWait()
            
        player.say(f"Your last page read was {last_page}")

if __name__ == "__main__":
    fire.Fire()