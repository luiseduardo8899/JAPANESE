import re
import xml.etree.ElementTree as metree
import random

pos_switch = {
"Godan verb with `bu' ending": {"VERB_5_BU"},
"Godan verb with `gu' ending": {"VERB_5_GU"},
"Godan verb with `ku' ending": {"VERB_5_KU"},
"Godan verb with `mu' ending": {"VERB_5_MU"},
"Godan verb with `ru' ending": {"VERB_5_RU"},
"Godan verb with `ru' ending (irregular verb)": {"VERB_5_RU", "VERB_IRREGULAR"},
"Godan verb with `su' ending": {"VERB_5_SU"} ,
"Godan verb with `tsu' ending": {"VERB_5_TSU"} ,
"Godan verb with `u' ending":  {"VERB5_U"},
"Godan verb with `u' ending (special class)": {"VERB_5_U", "VERB_SPECIAL"} ,
"Ichidan verb": {"VERB_1"} ,
"Ichidan verb - zuru verb (alternative form of -jiru verbs)": {"VERB_1_ZURU"} ,
"Nidan verb (lower class) with `ru' ending (archaic)": {"VERB_2_RU"} ,
"Yodan verb with `ku' ending (archaic)":  {"VERB_4_KU", "VERB_ARCHAIC"},
"Yodan verb with `ru' ending (archaic)":  {"VERB_4_RU", "VERB_ARCHAIC"},
"`taru' adjective": {"ADJECTIVE_TARU"},
"adjectival nouns or quasi-adjectives (keiyodoshi)": {"ADJECTIVAL_NOUN"},
"adjective (keiyoushi)": {"ADJECTIVE"},
"adverb (fukushi)":  {"ADVERB"},
"adverb taking the `to' particle":  {"ADVERB", "TAKES_TO"},
"adverbial noun (fukushitekimeishi)": {"ADVERBIAL_NOUN"} ,
"archaic/formal form of na-adjective":  {"FORMAL_NA_ADJECTIVE"},
"auxiliary verb": {"VERB_AUXILIARY"} ,
"conjunction": {"CONJUNCTION"},
"counter":  {"COUNTER"},
"expressions (phrases, clauses, etc.)": {"EXPRESSION"},
"interjection (kandoushi)":  {"INTERJECTION"},
"intransitive verb":  {"VERB_INTRANSITIVE"},
"irregular ru verb, plain form ends with -ri": {"VERB_RU", "VERB_IRREGULAR"},
"noun (common) (futsuumeishi)":  {"NOUN"},
"noun (temporal) (jisoumeishi)": {"NOUN", "TEMPORAl"},
"noun or participle which takes the aux. verb suru":  {"NOUN", "TAKES_SURU"},
"noun or verb acting prenominally":  {"NOUN_VERB_ACTING_PRENOMINALLY"},
"noun, used as a prefix":  {"NOUN", "USED_AS_PREFIX"},
"noun, used as a suffix": {"NOUN", "USED_AS_SUFFIX"} ,
"nouns which may take the genitive case particle `no'":  {"NOUN", "TAKES_NO"},
"pre-noun adjectival (rentaishi)":  {"PRE_NOUN_ADJECTIVAL"},
"prefix": {"PREFIX"},
"pronoun": {"PRONOUN"},
"suffix":  {"SUFFIX"},
"suru verb - special class":  {"VERB_SURU", "SPECIAL"},
"transitive verb": {"VERB_TRANSITIVE"}}

misc_switch = {
"abbreviation": {"ABBREVIATION"},
"archaism": {"ARCHAISM"},
"colloquialism": {"COLLOQUIALISM"},
"familiar language": {"FAMILIAR_LANGUAGE"},
"female term or language": {"FEMALE_TERM"},
"honorific or respectful (sonkeigo) language": {"HONORIFIC_TERM"},
"humble (kenjougo) language": {"HUMBLE_TERM"},
"male term or language": {"MALE_TERM"},
"obscure term": {"OBSCURE_TERM"},
"obsolete term": {"OBSOLETE_TERM"},
"polite (teineigo) language": {"POLITE_TERM"},
"sensitive": {"SENSITIVE"},
"slang": {"SLANG"},
"vulgar expression or word": {"VULGAR"},
"word usually written using kana alone": {"KANA_ALONE"},
"yojijukugo": {"YOJIJUKUGO"} }

def load_vocabulary():
    vocab_filename = "./GKvocab_n2.xml"
    dict_filename = "./JMdict_e"
    new_filename = "updated_vocab_entries.xml"
    
    vocab_array = []
    number = 0
    counter = 0
    level_counter = 1
    
    xml_file_h = open(new_filename,"w") #File where we will dump the updated XML entries

    print('Processing GKVocab XML File - ')
    #Main execution code
    #load the entire GKVocab and JMdict_e XML File 
    print('Processing GKVocab XML File: %s - ' % vocab_filename)
    tree = metree.parse(vocab_filename)
    dict_tree = metree.parse(dict_filename)

    #get root of the XML File
    root = tree.getroot()
    dict_root = dict_tree.getroot()

    #get all entries in the Dictionary file
    dict_entries_x = dict_root.findall('entry')
    
    #get all entries in the Vocab file
    entries_x = root.findall('vocab_entry')
    
    for entry_x in entries_x:
        no_match = 1
        match_reb = 0 # default to match Kanji element
        number += 1
    
        xml_file_h.write("<vocab_entry>\n")
        #Get kanji and furigana element, kanji element may be empty
        ent_seq_set_x = entry_x.findall('ent_seq')
        xml_file_h.write("<ent_seq>%s</ent_seq>\n" % ent_seq_set_x[0].text)

        jlpt_set = entry_x.findall('jlpt') # Reading Element ( furigana )
        xml_file_h.write("<jlpt>%s</jlpt>\n" % jlpt_set[0].text)
        level_set = entry_x.findall('level') # Reading Element ( furigana )
        if len(level_set) > 0 and level_set[0].text != None :
            xml_file_h.write("<level>%s</level>\n" % level_set[0].text)
        else:
            xml_file_h.write("<level></level>\n")

        kanji_set = entry_x.findall('kanji') # Kanji Element
        if len(kanji_set) > 0:
            if kanji_set[0].text == None or  kanji_set[0].text == "" :
                xml_file_h.write("<kanji></kanji>\n")
                match_reb = 1
            else:
                xml_file_h.write("<kanji>%s</kanji>\n" % kanji_set[0].text)
        else:
            match_reb = 1
        furigana_set = entry_x.findall('furigana') # Reading Element ( furigana )
        if len(furigana_set) > 0:
            if furigana_set[0].text == None or furigana_set[0].text == "" :
                xml_file_h.write("<furigana></furigana>\n")
            else:
                print("FURIGANA: %s \n" % furigana_set[0].text)
                xml_file_h.write("<furigana>%s</furigana>\n" % furigana_set[0].text)
        definition_set = entry_x.findall('definition') # Reading Element ( furigana )
        for definition_x in definition_set:
            xml_file_h.write("<definition>%s</definition>\n" % definition_x.text)

        pos_array = []
        sinf_array = []
        misc_array = []
        field_array = []
        kanji_score = 0
        furigana_score = 0
        if len(kanji_set) > 0 and len(furigana_set) > 0:
            vocab_list = [number, ent_seq_set_x[0].text, kanji_set[0].text, furigana_set[0].text, kanji_score, furigana_score]
            print("GKEntry: %s \n" % vocab_list)
        vocab_array.append(vocab_list)


        #Find MATCH in FULL DICTIONARY 
        for dict_entry_x in dict_entries_x:
            k_ele_set = dict_entry_x.findall('k_ele') # Kanji Element
            r_ele_set = dict_entry_x.findall('r_ele') # Kanji Element

            if no_match == 1:
                if match_reb == 0: #match only Kanji default
                    for k_ele_x in k_ele_set:
                        keb_set = k_ele_x.findall('keb')
                        reb_set = r_ele_x.findall('reb')
                        for keb_x in keb_set:
                            if keb_x.text == kanji_set[0].text:
                                match_entry = dict_entry_x
                                no_match = 0
                else : # Match furigana since no Kanji provided 
                    for r_ele_x in r_ele_set:
                        reb_set = r_ele_x.findall('reb')
                        for reb_x in reb_set:
                            if reb_x.text == furigana_set[0].text:
                                match_entry = dict_entry_x
                                no_match = 0

        if no_match == 0:
            #Get kanji and furigana element, kanji element may be empty
            dict_seq_set_x = match_entry.findall('ent_seq')
            sense_set = match_entry.findall('sense')
            k_ele_set = match_entry.findall('k_ele') # Kanji Element
            r_ele_set = match_entry.findall('r_ele') # Kanji Element
            #Check if match N2 Vocab entry
            xml_file_h.write("<dict_seq>%s</dict_seq>\n" % dict_seq_set_x[0].text)
            for sense_x in sense_set:
                pos_set = sense_x.findall('pos')
                s_inf_set = sense_x.findall('s_inf')
                misc_set = sense_x.findall('misc')
                field_set = sense_x.findall('field')

                #if so dump POS tags
                for pos_x in pos_set:
                    s =  pos_switch.get(pos_x.text, {"INVALID_POS: %s" % pos_x.text})
                    for i in s :
                        if i in pos_array:
                            print("REPEAT POS: %s \n" % i)
                        else:
                            pos_array.append(i)
                            xml_file_h.write("<pos>%s</pos>\n" % i)
                            print("POS: %s \n" % i)
                    
                #if so dump SINF tags
                for s_inf_x in s_inf_set:
                    if s_inf_x.text in sinf_array:
                        print("REPEAT SINF: %s \n" % s_inf_x.text )
                    else:
                        sinf_array.append(s_inf_x.text)
                        xml_file_h.write("<s_inf>%s</s_inf>\n" % s_inf_x.text)
                        print("SINF: %s \n" % s_inf_x.text )

                #if so dump SINF tags
                for misc_x in misc_set:
                    s =  misc_switch.get(misc_x.text, {"INVALID_MISC: %s" % misc_x.text})
                    for i in s :
                        if i in misc_array:
                            print("REPEAT MISC: %s \n" % i)
                        else:
                            misc_array.append(i)
                            xml_file_h.write("<misc>%s</misc>\n" % i )
                            print("MISC: %s \n" % i)

                #if so dump SINF tags
                for field_x in field_set:
                    if field_x.text in field_array:
                        print("REPEAT MISC: %s \n" % field_x.text )
                    else:
                        field_array.append(field_x.text)
                        xml_file_h.write("<field>%s</field>\n" % field_x.text )
                        print("FIELD: %s \n" % field_x.text )

                #TODO;: check the definition entries if they match or if new ones are found

        if no_match == 1:
             xml_file_h.write("<nomatch>NO MATCH IN DICTIONARY<no_match>\n")

        xml_file_h.write("</vocab_entry>\n\n")


    return vocab_array

print("STARTING")
vocab_A = load_vocabulary()
print("DONE")
