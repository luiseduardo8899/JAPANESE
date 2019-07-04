import scrapy
import re
import xml.etree.ElementTree as metree

class BlogSpider(scrapy.Spider):
    rate = 1
    pagenum = 1
    enable_images = 0
    filename = "sentence_db.txt"
    im_filename = "images_db.txt"
    vocab_score_filename = "vocab_score_db.txt"

    file_h = None
    im_file_h = None
    vocab_file_h = None 
    name = 'wikipedia'
    allowed_domains = ['ja.wikipedia.org']
    start_urls = ['https://ja.wikipedia.org']
    MAX_PAGES = 25

    SENTENCE_MIN = 14
    SENTENCE_MAX = 35

    vocab_x = []

    MIN_SENTENCE_RANK = 3 #If sentence has 2 N2 Vocab entries in it
    kanji_rank = 0
    furigana_rank = 0
    #TAG_RE = re.compile(r'<[^>]+>')

    def load_vocabulary(txt):
        vocab_filename = "./GKvocab_n2.xml"
        vocab_array = []
        number = 0
        counter = 0
        level_counter = 1

        print('Processing GKVocab XML File - ')
        #Main execution code
        #load the entire JMdict_e XML File 
        print('Processing GKVocab XML File: %s - ' % vocab_filename)
        tree = metree.parse(vocab_filename)

        #get root of the XML File
        root = tree.getroot()

        #get all entries in the file
        entries_x = root.findall('vocab_entry')

        for entry_x in entries_x:
            number += 1

            #Get kanji and furigana element, kanji element may be empty
            ent_seq_set_x = entry_x.findall('ent_seq')
            kanji_set = entry_x.findall('kanji') # Kanji Element
            furigana_set = entry_x.findall('furigana') # Reading Element ( furigana )
            kanji_score = 0
            furigana_score = 0
            vocab_list = [number, ent_seq_set_x[0].text, kanji_set[0].text, furigana_set[0].text, kanji_score, furigana_score]
            vocab_array.append(vocab_list)
            print(vocab_list)

        print(vocab_array)
        return vocab_array

    def __init__(self):
        self.download_delay = 1/float(self.rate)
        self.file_h = open(self.filename,"w") #always append to file
        self.im_file_h = open(self.im_filename,"w") #always append to file
        self.vocab_x = self.load_vocabulary()

    def clean_html(paragraph):
        re_tag = re.compile('<.*?>')
        cleantext = re.sub(re_tag, '', paragraph)
        return cleantext

    def parse(self, response):
        self.pagenum = self.pagenum + 1
        re_tag = re.compile('<.*?>')

        #for header1 in response.css('h1'):
        #    yield {'h1': header1.css('h1::text').get()}

        #for header2 in response.css('h2'):
        #    yield {'h2': header2.css('h2::text').get()}

        #for header3 in response.css('h3'):
        #    yield {'h3': header3.css('h3::text').get()}

        if self.enable_images > 0 :
            images = response.css('img').xpath('@src').getall()
            print("IMAGES: %s" % images)
            for im in images:
                im_txt = im + "\n"
                self.im_file_h.write(im_txt)

        for paragraph in response.css('p'):
            #yield {'p': paragraph.css('p::text').get()}
            p = paragraph.css('p').get()

            #DEBUG print("Page%s PARAGRAPH: %s" % (self.pagenum, p) )
            #1.clean out href from paragraph, <p> </p>
            clean_p = re.sub(re_tag, '', p)
            sentences = clean_p.split("。")

            #clean_p = self.clean_html(p)
            #2. Grab a sentence 
            for sentence in sentences:
                sentence_score = 0
                num_char = len(sentence)
                kanjis = []
                furiganas = []
                if (num_char < self.SENTENCE_MAX) and (num_char > self.SENTENCE_MIN) :
                    for k, entry in enumerate(self.vocab_x, start=0):
                        kanji_count = 0
                        furigana_count = 0

                        num, seq, kanji, furigana, kanji_score, furigana_score = entry

                        if kanji != None:
                            kanji_count = sentence.count(kanji)
                            if kanji_count > 0 :
                                kanji_score = kanji_score + kanji_count
                                kanjis.append(kanji)

                        if kanji == None and furigana != None:
                            furigana_count = sentence.count(furigana)
                            if furigana_count > 0 :
                                furigana_score = furigana_score + furigana_count
                                furiganas.append(furigana)

                        if (kanji_count + furigana_count) > 0:
                            sentence_score = sentence_score + kanji_count + furigana_count
                            #update vocab entry score
                            self.vocab_x[k] =  [num, seq, kanji, furigana, kanji_score, furigana_score]
                        
                         
                    if sentence_score >= self.MIN_SENTENCE_RANK : 
                        self.file_h.write(str(num_char))
                        self.file_h.write(": Score: ")
                        self.file_h.write(str(sentence_score))
                        self.file_h.write(": ")
                        self.file_h.write(sentence)
                        self.file_h.write(" || K: ")
                        self.file_h.write("".join(kanjis))
                        #self.file_h.write(" F: ")
                        #self.file_h.write("".join(furiganas))
                        self.file_h.write(" ||\n")

            #For each word in dictionary search how many times it appears in the text 


            #TODO: 3. Rank sentence based on how many JLP N2 words it hits.  ( Later use N5/N4/N3/N2/N1 vocabulary )
            ##LUIS: 4. Everytime a vocabulary word is hit in the <p> increase its points in the database ( text hits). 
            ##LUIS:    kanji_rank = kanji_rank + 1 
            ##LUIS:    furigana_rank = furigana_rank + 1

            #TODO" 5. Dump out sentences that hit 2 or 3 N2 vocabulary words.
            #TODO: 6. group words based on number of hits

            #7.  #dump to text file after every 10 pages?
            if self.pagenum % 5 == 0 : 
                score_file_h = open(self.vocab_score_filename, "w") #always append to file
                #Dump out only the entries that have hits!
                for k, entry in enumerate(self.vocab_x, start=0):
                    num, seq, kanji, furigana, kanji_score, furigana_score = entry
                    if kanji_score > 0 :
                        score_file_h.write("".join(entry))
                    

        # Follow a mximum of 50 pages
        if self.pagenum < self.MAX_PAGES :
            for next_page in response.css('a.mw-redirect'):
                yield response.follow(next_page, self.parse)


