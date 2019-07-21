import re
import xml.etree.ElementTree as metree
import random

def load_videos():
    vocab_filename = "./GKvocab_n2.xml"
    video_filename = "./GKvideos_n2.xml" 
    dict_filename = "./JMdict_e"
    new_filename = "updated_video_entries.xml"
    
    vocab_array = []
    number = 0
    counter = 0
    level_counter = 1
    
    xml_file_h = open(new_filename,"w") #File where we will dump the updated XML entries

    #Main execution code
    #load the entire GKVocab and JMdict_e XML File 
    print('Processing GKVocab XML File: %s - ' % vocab_filename)
    tree = metree.parse(vocab_filename)
    dict_tree = metree.parse(dict_filename)
    video_tree = metree.parse(video_filename)

    #get root of the XML File
    root = tree.getroot()
    dict_root = dict_tree.getroot()
    video_root = video_tree.getroot()

    #get all entries in the Dictionary file
    dict_entry_set = dict_root.findall('entry')
    
    #get all entries in the Vocab file
    entry_set = root.findall('vocab_entry')
    video_entries = video_root.findall('video_entry')

    for video_entry_x in video_entries:
        no_gk_match = 1
        no_dict_match = 1
        title_set = video_entry_x.findall('title')
        url_set = video_entry_x.findall('url')
        ent_seq_set = video_entry_x.findall('ent_seq')
        ventry_set = video_entry_x.findall('ventry')
        fentry_set = video_entry_x.findall('fentry')

        for ventry_x in ventry_set:
            no_gk_match = 1
            no_dict_match = 1
            print("VOCAB ENTRY: %s" % ventry_x.text)
            for entry_x in entry_set:
                kanji_set = entry_x.findall('kanji') # Kanji Element
                furigana_set = entry_x.findall('furigana') # Kanji Element
                seq_num_set = entry_x.findall('ent_seq') # Kanji Element
                if len(kanji_set) > 0:
                    if kanji_set[0].text == None or  kanji_set[0].text == "" :
                        match_reb = 1
                        if ventry_x.text == furigana_set[0].text:
                            print("MATCH_ENTRY: %s to GK entry  : %s" % (ventry_x.text, seq_num_set[0].text ))
                            no_gk_match = 0
                    else:
                        if ventry_x.text == kanji_set[0].text:
                            print("MATCH_ENTRY: %s to GK entry  : %s" % (ventry_x.text, seq_num_set[0].text ))
                            no_gk_match = 0
            #If could not match in current GK_n2 database, seac hfull ditionary
            if no_gk_match == 1:
                for dict_entry_x in dict_entry_set:
                    dict_seq_set_x = dict_entry_x.findall('ent_seq')
                    sense_set = dict_entry_x.findall('sense')
                    k_ele_set = dict_entry_x.findall('k_ele') # Kanji Element
                    r_ele_set = dict_entry_x.findall('r_ele') # Kanji Element
                    for k_ele_x in k_ele_set:
                        keb_set = k_ele_x.findall('keb')
                        #reb_set = r_ele_x.findall('reb')
                        for keb_x in keb_set:
                            if ventry_x.text == keb_x.text:
                                print("MATCH_ENTRY: %s to DICT entry  : %s" % (ventry_x.text, dict_seq_set_x[0].text ))
                                no_dict_match = 0

            if no_dict_match == 1 and no_gk_match == 1:
                print("NOMATCH_ENTRY: %s to DICT entry  : %s" % ventry_x.text )

        for fentry_x in fentry_set:
            no_gk_match = 1
            print("VOCAB FENTRY: %s" % fentry_x.text)
            for entry_x in entry_set:
                kanji_set = entry_x.findall('kanji') # Kanji Element
                furigana_set = entry_x.findall('furigana') # Kanji Element
                seq_num_set = entry_x.findall('ent_seq') # Kanji Element
                if fentry_x.text == furigana_set[0].text:
                    print("MATCH_FENTRY: %s to GK entry  : %s" % (ventry_x.text, seq_num_set[0].text ))
                    no_gk_match = 0
            #If could not match in current GK_n2 database, seac hfull ditionary
            if no_gk_match == 1:
                no_dict_match = 1
                for dict_entry_x in dict_entry_set:
                    dict_seq_set_x = dict_entry_x.findall('ent_seq')
                    sense_set = dict_entry_x.findall('sense')
                    k_ele_set = dict_entry_x.findall('k_ele') # Kanji Element
                    r_ele_set = dict_entry_x.findall('r_ele') # Kanji Element
                    for r_ele_x in r_ele_set:
                        reb_set = r_ele_x.findall('reb')
                        #reb_set = r_ele_x.findall('reb')
                        for reb_x in reb_set:
                            if fentry_x.text == reb_x.text:
                                print("MATCH_FENTRY: %s to DICT entry  : %s" % (fentry_x.text, dict_seq_set_x[0].text ))
                                no_dict_match = 0

    

print("STARTING")
vocab_A = load_videos()
print("DONE")
