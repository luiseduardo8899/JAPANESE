from django import forms
from django_countries.fields import CountryField

JANUARY_ID = 0
FEBRUARY_ID = 1
MARCH_ID = 2
APRIL_ID = 3
MAY_ID = 4
JUNE_ID = 5
JULY_ID = 6
AUGUST_ID = 7
SEPTEMBER_ID = 8
OCTOBER_ID = 9
NOVEMBER_ID = 10
DECEMBER_ID = 11

MONTH_IDS = (
(JANUARY_ID , "January"),
(FEBRUARY_ID , "February"),
(MARCH_ID , "March"),
(APRIL_ID , "April"),
(MAY_ID , "May"),
(JUNE_ID , "June"),
(JULY_ID , "July"),
(AUGUST_ID , "August"),
(SEPTEMBER_ID , "September"),
(OCTOBER_ID , "October"),
(NOVEMBER_ID , "November"),
(DECEMBER_ID , "December"),
)

DAY_IDS = (
(1, "1"),
(2, "2"),
(3, "3"),
(4, "4"),
(5, "5"),
(6, "6"),
(7, "7"),
(8, "8"),
(9, "9"),
(10, "10"),
(11, "11"),
(12, "12"),
(13, "13"),
(14, "14"),
(15, "15"),
(16, "16"),
(17, "17"),
(18, "18"),
(19, "19"),
(20, "20"),
(21, "21"),
(22, "22"),
(23, "23"),
(24, "24"),
(25, "25"),
(26, "26"),
(27, "27"),
(28, "28"),
(29, "29"),
(30, "30"),
(31, "31"),
)

YEAR_IDS = (
(1920, "before 1920"),
(1921, "1921"),
(1922, "1922"),
(1923, "1923"),
(1924, "1924"),
(1925, "1925"),
(1926, "1926"),
(1927, "1927"),
(1928, "1928"),
(1929, "1929"),
(1930, "1930"),
(1931, "1931"),
(1932, "1932"),
(1933, "1933"),
(1934, "1934"),
(1935, "1935"),
(1936, "1936"),
(1937, "1937"),
(1938, "1938"),
(1939, "1939"),
(1940, "1940"),
(1941, "1941"),
(1942, "1942"),
(1943, "1943"),
(1944, "1944"),
(1945, "1945"),
(1946, "1946"),
(1947, "1947"),
(1948, "1948"),
(1949, "1949"),
(1950, "1950"),
(1951, "1951"),
(1952, "1952"),
(1953, "1953"),
(1954, "1954"),
(1955, "1955"),
(1956, "1956"),
(1957, "1957"),
(1958, "1958"),
(1959, "1959"),
(1960, "1960"),
(1961, "1961"),
(1962, "1962"),
(1963, "1963"),
(1964, "1964"),
(1965, "1965"),
(1966, "1966"),
(1967, "1967"),
(1968, "1968"),
(1969, "1969"),
(1970, "1970"),
(1971, "1971"),
(1972, "1972"),
(1973, "1973"),
(1974, "1974"),
(1975, "1975"),
(1976, "1976"),
(1977, "1977"),
(1978, "1978"),
(1979, "1979"),
(1980, "1980"),
(1981, "1981"),
(1982, "1982"),
(1983, "1983"),
(1984, "1984"),
(1985, "1985"),
(1986, "1986"),
(1987, "1987"),
(1988, "1988"),
(1989, "1989"),
(1990, "1990"),
(1991, "1991"),
(1992, "1992"),
(1993, "1993"),
(1994, "1994"),
(1995, "1995"),
(1996, "1996"),
(1997, "1997"),
(1998, "1998"),
(1999, "1999"),
(2000, "2000"),
(2001, "2001"),
(2002, "2002"),
(2003, "2003"),
(2004, "2004"),
(2005, "2005"),
(2006, "2006"),
(2007, "2007"),
(2008, "2008"),
(2009, "2009"),
(2010, "2010"),
(2011, "2011"),
(2012, "2012"),
(2013, "2013"),
(2014, "2014"),
(2015, "2015"),
(2016, "2016"),
(2017, "2017"),
(2018, "2018"),
(2019, "2019"),
)
#Gender Question IDS
FEMALE_ID = 0 
MALE_ID = 1 
LGBT_ID = 2 
OTHER_ID = 3
REFRAIN_ID = 4
GENDER_IDS  = (
(FEMALE_ID , "Female"),
(MALE_ID , "Male"),
(LGBT_ID , "LGBT"),
(OTHER_ID , "Other"),
(REFRAIN_ID , "Preffer not to say"),
)
AFRIKANNS_ID = 0
ALBANIAN_ID = 1
ARABIC_ID = 2
ARMENIAN_ID = 3
BASQUE_ID = 4
BENGALI_ID = 5
BULGARIAN_ID = 6
CATALAN_ID = 7
CAMBODIAN_ID = 8
CHINESE_ID = 9
CROATION_ID = 10
CZECH_ID = 11
DANISH_ID = 12
DUTCH_ID = 13
ENGLISH_ID = 14
ESTONIAN_ID = 15
FIJI_ID = 16
FINNISH_ID = 17
FRENCH_ID = 18
GEORGIAN_ID = 19
GERMAN_ID = 20
GREEK_ID = 21
GUJARATI_ID = 22
HEBREW_ID = 23
HINDI_ID = 24
HUNGARIAN_ID = 25
ICELANDIC_ID = 26
INDONESIAN_ID = 27
IRISH_ID = 28
ITALIAN_ID = 29
JAPANESE_ID = 30
JAVANESE_ID = 31
KOREAN_ID = 32
LATIN_ID = 33
LATVIAN_ID = 34
LITHUANIAN_ID = 35
MACEDONIAN_ID = 36
MALAY_ID = 37
MALAYALAM_ID = 38
MALTESE_ID = 39
MAORI_ID = 40
MARATHI_ID = 41
MONGOLIAN_ID = 42
NEPALI_ID = 43
NORWEGIAN_ID = 44
PERSIAN_ID = 45
POLISH_ID = 46
PORTUGUESE_ID = 47
PUNJABI_ID = 48
QUECHUA_ID = 49
ROMANIAN_ID = 50
RUSSIAN_ID = 51
SAMOAN_ID = 52
SERBIAN_ID = 53
SLOVAK_ID = 54
SLOVENIAN_ID = 55
SPANISH_ID = 56
SWAHILI_ID = 57
SWEDISH_ID  = 58
TAMIL_ID = 59
TATAR_ID = 60
TELUGU_ID = 61
THAI_ID = 62
TIBETAN_ID = 63
TONGA_ID = 64
TURKISH_ID = 65
UKRANIAN_ID = 66
URDU_ID = 67
UZBEK_ID = 68
VIETNAMESE_ID = 69
WELSH_ID = 70
XHOSA_ID = 71

LANGUAGE_IDS = (
(AFRIKANNS_ID, "Afrikanns"),
(ALBANIAN_ID, "Albanian"),
(ARABIC_ID, "Arabic"),
(ARMENIAN_ID, "Armenian"),
(BASQUE_ID, "Basque"),
(BENGALI_ID, "Bengali"),
(BULGARIAN_ID, "Bulgarian"),
(CATALAN_ID, "Catalan"),
(CAMBODIAN_ID, "Cambodian"),
(CHINESE_ID, "Chinese (Mandarin)"),
(CROATION_ID, "Croation"),
(CZECH_ID, "Czech"),
(DANISH_ID, "Danish"),
(DUTCH_ID, "Dutch"),
(ENGLISH_ID, "English"),
(ESTONIAN_ID, "Estonian"),
(FIJI_ID, "Fiji"),
(FINNISH_ID, "Finnish"),
(FRENCH_ID, "French"),
(GEORGIAN_ID, "Georgian"),
(GERMAN_ID, "German"),
(GREEK_ID, "Greek"),
(GUJARATI_ID, "Gujarati"),
(HEBREW_ID, "Hebrew"),
(HINDI_ID, "Hindi"),
(HUNGARIAN_ID, "Hungarian"),
(ICELANDIC_ID, "Icelandic"),
(INDONESIAN_ID, "Indonesian"),
(IRISH_ID, "Irish"),
(ITALIAN_ID, "Italian"),
(JAPANESE_ID, "Japanese"),
(JAVANESE_ID, "Javanese"),
(KOREAN_ID, "Korean"),
(LATIN_ID, "Latin"),
(LATVIAN_ID, "Latvian"),
(LITHUANIAN_ID, "Lithuanian"),
(MACEDONIAN_ID, "Macedonian"),
(MALAY_ID, "Malay"),
(MALAYALAM_ID, "Malayalam"),
(MALTESE_ID, "Maltese"),
(MAORI_ID, "Maori"),
(MARATHI_ID, "Marathi"),
(MONGOLIAN_ID, "Mongolian"),
(NEPALI_ID, "Nepali"),
(NORWEGIAN_ID, "Norwegian"),
(PERSIAN_ID, "Persian"),
(POLISH_ID, "Polish"),
(PORTUGUESE_ID, "Portuguese"),
(PUNJABI_ID, "Punjabi"),
(QUECHUA_ID, "Quechua"),
(ROMANIAN_ID, "Romanian"),
(RUSSIAN_ID, "Russian"),
(SAMOAN_ID, "Samoan"),
(SERBIAN_ID, "Serbian"),
(SLOVAK_ID, "Slovak"),
(SLOVENIAN_ID, "Slovenian"),
(SPANISH_ID, "Spanish"),
(SWAHILI_ID, "Swahili"),
(SWEDISH_ID, "Swedish "),
(TAMIL_ID, "Tamil"),
(TATAR_ID, "Tatar"),
(TELUGU_ID, "Telugu"),
(THAI_ID, "Thai"),
(TIBETAN_ID, "Tibetan"),
(TONGA_ID, "Tonga"),
(TURKISH_ID, "Turkish"),
(UKRANIAN_ID, "Ukranian"),
(URDU_ID, "Urdu"),
(UZBEK_ID, "Uzbek"),
(VIETNAMESE_ID, "Vietnamese"),
(WELSH_ID, "Welsh"),
(XHOSA_ID, "Xhosa"),
)
#COUNTRY TAG IDS
AFGHANISTAN_ID  =  0
ALBANIA_ID = 1
ALGERIA_ID = 2
ANDORRA_ID = 3
ANGOLA_ID = 4
ANTIGUA_AND_BARBUDA_ID = 5
ARGENTINA_ID = 6
ARMENIA_ID = 7
AUSTRALIA_ID = 8
AUSTRIA_ID = 9
AZERBAIJAN_ID = 10
BAHAMAS_ID = 11
BAHRAIN_ID = 12
BANGLADESH_ID = 13
BARBADOS_ID = 14
BELARUS_ID = 15
BELGIUM_ID = 16
BELIZE_ID = 17
BENIN_ID = 18
BHUTAN_ID = 19
BOLIVIA_ID = 20
BOSNIA_AND_HERZEGOVINA_ID = 21
BOTSWANA_ID = 22
BRAZIL_ID = 23
BRUNEI_ID = 24
BULGARIA_ID = 25
BURKINA_FASO_ID = 26
BURUNDI_ID = 27
CABO_VERDE_ID = 28
CAMBODIA_ID = 29
CAMEROON_ID = 30
CANADA_ID = 31
CENTRAL_AFRICAN_REPUBLIC_ID = 32
CHAD_ID = 33
CHILE_ID = 34
CHINA_ID = 35
COLOMBIA_ID = 36
COMOROS_ID = 37
CONGO_ID = 38
COSTA_RICA_ID = 39
CROATIA_ID = 40
CUBA_ID = 41
CYPRUS_ID = 42
CZECHIA_ID = 43
COTE_D_IVOIRE_ID = 44
DR_CONGO_ID = 45
DENMARK_ID = 46
DJIBOUTI_ID = 47
DOMINICA_ID = 48
DOMINICAN_REPUBLIC_ID = 49
ECUADOR_ID = 50
EGYPT_ID = 51
EL_SALVADOR_ID = 52
EQUATORIAL_GUINEA_ID = 53
ERITREA_ID = 54
ESTONIA_ID = 55
ETHIOPIA_ID = 56
FIJI_ID = 57
FINLAND_ID = 58
FRANCE_ID = 59
GABON_ID = 60
GAMBIA_ID = 61
GEORGIA_ID = 62
GERMANY_ID = 63
GHANA_ID = 64
GREECE_ID = 65
GRENADA_ID = 66
GUATEMALA_ID = 67
GUINEA_ID = 68
GUINEA_ID = 69
GUYANA_ID = 70
HAITI_ID = 71
HOLY_SEE_ID = 72
HONDURAS_ID = 73
HUNGARY_ID = 74
ICELAND_ID = 75
INDIA_ID = 76
INDONESIA_ID = 77
IRAN_ID = 78
IRAQ_ID = 79
IRELAND_ID = 80
ISRAEL_ID = 81
ITALY_ID = 82
JAMAICA_ID = 83
JAPAN_ID = 84
JORDAN_ID = 85
KAZAKHSTAN_ID = 86
KENYA_ID = 87
KIRIBATI_ID = 88
KUWAIT_ID = 89
KYRGYZSTAN_ID = 90
LAOS_ID = 91
LATVIA_ID = 92
LEBANON_ID = 93
LESOTHO_ID = 94
LIBERIA_ID = 95
LIBYA_ID = 96
LIECHTENSTEIN_ID = 97
LITHUANIA_ID = 98
LUXEMBOURG_ID = 99
MADAGASCAR_ID = 100
MALAWI_ID = 101
MALAYSIA_ID = 102
MALDIVES_ID = 103
MALI_ID = 104
MALTA_ID = 105
MARSHALL_ISLANDS_ID = 106
MAURITANIA_ID = 107
MAURITIUS_ID = 108
MEXICO_ID = 109
MICRONESIA_ID = 110
MOLDOVA_ID = 111
MONACO_ID = 112
MONGOLIA_ID = 113
MONTENEGRO_ID = 114
MOROCCO_ID = 115
MOZAMBIQUE_ID = 116
MYANMAR_ID = 117
NAMIBIA_ID = 118
NAURU_ID = 119
NEPAL_ID = 120
NETHERLANDS_ID = 121
NEW_ZEALAND_ID = 122
NICARAGUA_ID = 123
NIGER_ID = 124
NIGERIA_ID = 125
NORTH_KOREA_ID = 126
NORTH_MACEDONIA_ID = 127
NORWAY_ID = 128
OMAN_ID = 129
PAKISTAN_ID = 130
PALAU_ID = 131
PANAMA_ID = 132
PAPUA_NEW_GUINEA_ID = 133
PARAGUAY_ID = 134
PERU_ID = 135
PHILIPPINES_ID = 136
POLAND_ID = 137
PORTUGAL_ID = 138
QATAR_ID = 139
ROMANIA_ID = 140
RUSSIA_ID = 141
RWANDA_ID = 142
SAINT_KITTS_NEVIS_ID = 143
SAINT_LUCIA_ID = 144
SAMOA_ID = 145
SAN_MARINO_ID = 146
SAO_TOME_PRINCIPE_ID = 147
SAUDI_ARABIA_ID = 148
SENEGAL_ID = 149
SERBIA_ID = 150
SEYCHELLES_ID = 151
SIERRA_LEONE_ID = 152
SINGAPORE_ID = 153
SLOVAKIA_ID = 154
SLOVENIA_ID = 155
SOLOMON_ISLANDS_ID = 156
SOMALIA_ID = 157
SOUTH_AFRICA_ID = 158
SOUTH_KOREA_ID = 159
SOUTH_SUDAN_ID = 160
SPAIN_ID = 161
SRI_LANKA_ID = 162
ST_VINCENT_GRENADINES_ID = 163
STATE_OF_PALESTINE_ID = 164
SUDAN_ID = 165
SURINAME_ID = 166
SWAZILAND_ID = 167
SWEDEN_ID = 168
SWITZERLAND_ID = 169
SYRIA_ID = 170
TAIWAN_ID = 171
TAJIKISTAN_ID = 172
TANZANIA_ID = 173
THAILAND_ID = 174
TIMOR_ID = 175
TOGO_ID = 176
TONGA_ID = 177
TRINIDAD_AND_TOBAGO_ID = 178
TUNISIA_ID = 179
TURKEY_ID = 180
TURKMENISTAN_ID = 181
TUVALU_ID = 182
UGANDA_ID = 183
UKRAINE_ID = 184
UNITED_ARAB_EMIRATES_ID = 185
UNITED_KINGDOM_ID = 186
UNITED_STATES_ID = 187
URUGUAY_ID = 188
UZBEKISTAN_ID = 189
VANUATU_ID = 190
VENEZUELA_ID = 191
VIETNAM_ID = 192
YEMEN_ID = 193
ZAMBIA_ID = 194
ZIMBABWE_ID = 195

COUNTRY_IDS = (
(AFGHANISTAN_ID , "Afghanistan" ),
(ALBANIA_ID, "Albania"),
(ALGERIA_ID, "Algeria"),
(ANDORRA_ID, "Andorra"),
(ANGOLA_ID, "Angola"),
(ANTIGUA_AND_BARBUDA_ID, "Antigua and Barbuda"),
(ARGENTINA_ID, "Argentina"),
(ARMENIA_ID, "Armenia"),
(AUSTRALIA_ID, "Australia"),
(AUSTRIA_ID, "Austria"),
(AZERBAIJAN_ID, "Azerbaijan"),
(BAHAMAS_ID, "Bahamas"),
(BAHRAIN_ID, "Bahrain"),
(BANGLADESH_ID, "Bangladesh"),
(BARBADOS_ID, "Barbados"),
(BELARUS_ID, "Belarus"),
(BELGIUM_ID, "Belgium"),
(BELIZE_ID, "Belize"),
(BENIN_ID, "Benin"),
(BHUTAN_ID, "Bhutan"),
(BOLIVIA_ID, "Bolivia"),
(BOSNIA_AND_HERZEGOVINA_ID, "Bosnia and Herzegovina"),
(BOTSWANA_ID, "Botswana"),
(BRAZIL_ID, "Brazil"),
(BRUNEI_ID, "Brunei"),
(BULGARIA_ID, "Bulgaria"),
(BURKINA_FASO_ID, "Burkina Faso"),
(BURUNDI_ID, "Burundi"),
(CABO_VERDE_ID, "Cabo Verde"),
(CAMBODIA_ID, "Cambodia"),
(CAMEROON_ID, "Cameroon"),
(CANADA_ID, "Canada"),
(CENTRAL_AFRICAN_REPUBLIC_ID, "Central African Republic"),
(CHAD_ID, "Chad"),
(CHILE_ID, "Chile"),
(CHINA_ID, "China"),
(COLOMBIA_ID, "Colombia"),
(COMOROS_ID, "Comoros"),
(CONGO_ID, "Congo"),
(COSTA_RICA_ID, "Costa Rica"),
(CROATIA_ID, "Croatia"),
(CUBA_ID, "Cuba"),
(CYPRUS_ID, "Cyprus"),
(CZECHIA_ID, "Czechia"),
(COTE_D_IVOIRE_ID, "Côte d'Ivoire"),
(DR_CONGO_ID, "DR Congo"),
(DENMARK_ID, "Denmark"),
(DJIBOUTI_ID, "Djibouti"),
(DOMINICA_ID, "Dominica"),
(DOMINICAN_REPUBLIC_ID, "Dominican Republic"),
(ECUADOR_ID, "Ecuador"),
(EGYPT_ID, "Egypt"),
(EL_SALVADOR_ID, "El Salvador"),
(EQUATORIAL_GUINEA_ID, "Equatorial Guinea"),
(ERITREA_ID, "Eritrea"),
(ESTONIA_ID, "Estonia"),
(ETHIOPIA_ID, "Ethiopia"),
(FIJI_ID, "Fiji"),
(FINLAND_ID, "Finland"),
(FRANCE_ID, "France"),
(GABON_ID, "Gabon"),
(GAMBIA_ID, "Gambia"),
(GEORGIA_ID, "Georgia"),
(GERMANY_ID, "Germany"),
(GHANA_ID, "Ghana"),
(GREECE_ID, "Greece"),
(GRENADA_ID, "Grenada"),
(GUATEMALA_ID, "Guatemala"),
(GUINEA_ID, "Guinea"),
(GUINEA_ID, "Guinea"),
(GUYANA_ID, "Guyana"),
(HAITI_ID, "Haiti"),
(HOLY_SEE_ID, "Holy See"),
(HONDURAS_ID, "Honduras"),
(HUNGARY_ID, "Hungary"),
(ICELAND_ID, "Iceland"),
(INDIA_ID, "India"),
(INDONESIA_ID, "Indonesia"),
(IRAN_ID, "Iran"),
(IRAQ_ID, "Iraq"),
(IRELAND_ID, "Ireland"),
(ISRAEL_ID, "Israel"),
(ITALY_ID, "Italy"),
(JAMAICA_ID, "Jamaica"),
(JAPAN_ID, "Japan"),
(JORDAN_ID, "Jordan"),
(KAZAKHSTAN_ID, "Kazakhstan"),
(KENYA_ID, "Kenya"),
(KIRIBATI_ID, "Kiribati"),
(KUWAIT_ID, "Kuwait"),
(KYRGYZSTAN_ID, "Kyrgyzstan"),
(LAOS_ID, "Laos"),
(LATVIA_ID, "Latvia"),
(LEBANON_ID, "Lebanon"),
(LESOTHO_ID, "Lesotho"),
(LIBERIA_ID, "Liberia"),
(LIBYA_ID, "Libya"),
(LIECHTENSTEIN_ID, "Liechtenstein"),
(LITHUANIA_ID, "Lithuania"),
(LUXEMBOURG_ID, "Luxembourg"),
(MADAGASCAR_ID, "Madagascar"),
(MALAWI_ID, "Malawi"),
(MALAYSIA_ID, "Malaysia"),
(MALDIVES_ID, "Maldives"),
(MALI_ID, "Mali"),
(MALTA_ID, "Malta"),
(MARSHALL_ISLANDS_ID, "Marshall Islands"),
(MAURITANIA_ID, "Mauritania"),
(MAURITIUS_ID, "Mauritius"),
(MEXICO_ID, "Mexico"),
(MICRONESIA_ID, "Micronesia"),
(MOLDOVA_ID, "Moldova"),
(MONACO_ID, "Monaco"),
(MONGOLIA_ID, "Mongolia"),
(MONTENEGRO_ID, "Montenegro"),
(MOROCCO_ID, "Morocco"),
(MOZAMBIQUE_ID, "Mozambique"),
(MYANMAR_ID, "Myanmar"),
(NAMIBIA_ID, "Namibia"),
(NAURU_ID, "Nauru"),
(NEPAL_ID, "Nepal"),
(NETHERLANDS_ID, "Netherlands"),
(NEW_ZEALAND_ID, "New Zealand"),
(NICARAGUA_ID, "Nicaragua"),
(NIGER_ID, "Niger"),
(NIGERIA_ID, "Nigeria"),
(NORTH_KOREA_ID, "North Korea"),
(NORTH_MACEDONIA_ID, "North Macedonia"),
(NORWAY_ID, "Norway"),
(OMAN_ID, "Oman"),
(PAKISTAN_ID, "Pakistan"),
(PALAU_ID, "Palau"),
(PANAMA_ID, "Panama"),
(PAPUA_NEW_GUINEA_ID, "Papua New Guinea"),
(PARAGUAY_ID, "Paraguay"),
(PERU_ID, "Peru"),
(PHILIPPINES_ID, "Philippines"),
(POLAND_ID, "Poland"),
(PORTUGAL_ID, "Portugal"),
(QATAR_ID, "Qatar"),
(ROMANIA_ID, "Romania"),
(RUSSIA_ID, "Russia"),
(RWANDA_ID, "Rwanda"),
(SAINT_KITTS_NEVIS_ID, "Saint Kitts & Nevis"),
(SAINT_LUCIA_ID, "Saint Lucia"),
(SAMOA_ID, "Samoa"),
(SAN_MARINO_ID, "San Marino"),
(SAO_TOME_PRINCIPE_ID, "Sao Tome & Principe"),
(SAUDI_ARABIA_ID, "Saudi Arabia"),
(SENEGAL_ID, "Senegal"),
(SERBIA_ID, "Serbia"),
(SEYCHELLES_ID, "Seychelles"),
(SIERRA_LEONE_ID, "Sierra Leone"),
(SINGAPORE_ID, "Singapore"),
(SLOVAKIA_ID, "Slovakia"),
(SLOVENIA_ID, "Slovenia"),
(SOLOMON_ISLANDS_ID, "Solomon Islands"),
(SOMALIA_ID, "Somalia"),
(SOUTH_AFRICA_ID, "South Africa"),
(SOUTH_KOREA_ID, "South Korea"),
(SOUTH_SUDAN_ID, "South Sudan"),
(SPAIN_ID, "Spain"),
(SRI_LANKA_ID, "Sri Lanka"),
(ST_VINCENT_GRENADINES_ID, "St. Vincent & Grenadines"),
(STATE_OF_PALESTINE_ID, "State of Palestine"),
(SUDAN_ID, "Sudan"),
(SURINAME_ID, "Suriname"),
(SWAZILAND_ID, "Swaziland"),
(SWEDEN_ID, "Sweden"),
(SWITZERLAND_ID, "Switzerland"),
(SYRIA_ID, "Syria"),
(TAIWAN_ID, "Taiwan"),
(TAJIKISTAN_ID, "Tajikistan"),
(TANZANIA_ID, "Tanzania"),
(THAILAND_ID, "Thailand"),
(TIMOR_ID, "Timor"),
(TOGO_ID, "Togo"),
(TONGA_ID, "Tonga"),
(TRINIDAD_AND_TOBAGO_ID, "Trinidad and Tobago"),
(TUNISIA_ID, "Tunisia"),
(TURKEY_ID, "Turkey"),
(TURKMENISTAN_ID, "Turkmenistan"),
(TUVALU_ID, "Tuvalu"),
(UGANDA_ID, "Uganda"),
(UKRAINE_ID, "Ukraine"),
(UNITED_ARAB_EMIRATES_ID, "United Arab Emirates"),
(UNITED_KINGDOM_ID, "United Kingdom"),
(UNITED_STATES_ID, "United States"),
(URUGUAY_ID, "Uruguay"),
(UZBEKISTAN_ID, "Uzbekistan"),
(VANUATU_ID, "Vanuatu"),
(VENEZUELA_ID, "Venezuela"),
(VIETNAM_ID, "Vietnam"),
(YEMEN_ID, "Yemen"),
(ZAMBIA_ID, "Zambia"),
(ZIMBABWE_ID, "Zimbabwe"),
)
class ProfileForm(forms.Form):
    gender = forms.ChoiceField(label="Gender", choices=GENDER_IDS)
    gender_other = forms.CharField(label="Other", max_length=50, required=False)
    year_ob = forms.ChoiceField(label="Year", choices=YEAR_IDS)
    month_ob = forms.ChoiceField(label="Month", choices=MONTH_IDS)
    day_ob = forms.ChoiceField(label="Day", choices=DAY_IDS)
    country = forms.ChoiceField(label="Where are you from originally?", choices=COUNTRY_IDS)
    location = forms.ChoiceField(label="Where do you live now?", choices=COUNTRY_IDS)
    language = forms.ChoiceField(label="What is your mother tongue or main language ?", choices=LANGUAGE_IDS)
    intro = forms.CharField(label="Write a short intro about yourself", widget=forms.Textarea, max_length=800, required=False)
