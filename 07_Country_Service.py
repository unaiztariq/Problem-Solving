class CountryService:
    def __init__(self,data):
        self.data = data

    def get_capital(self,name):
        for i in self.data:
            if name==i["name"]["common"]:
                return i["capital"][0]
    def get_region(self,name):
        for i in self.data:
            if name==i["name"]["common"]:
                return i["region"]
    def get_population(self,name):
        for i in self.data:
            name = i["name"]["common"] if i.get("name") else None
            try:
                if name==i["name"]["common"]:
                    return i["population"]          
            except:
                for j in i:
                    if j == "name":
                        if name==i[j]["common"]:
                            return i["population"]
                        else:
                            print("name not find")
            




data =[{"tld":[".pk"],"cca2":"PK","ccn3":"586","cca3":"PAK","cioc":"PAK","independent":True,"status":"officially-assigned","unMember":True,"idd":{"root":"+9","suffixes":["2"]},"capital":["Islamabad"],"altSpellings":["PK","Pākistān","Islamic Republic of Pakistan","Islāmī Jumhūriya'eh Pākistān"],"region":"Asia","subregion":"Southern Asia","landlocked":False,"borders":["AFG","CHN","IND","IRN"],"area":796095.0,"maps":{"googleMaps":"https://goo.gl/maps/5LYujdfR5yLUXoERA","openStreetMaps":"https://www.openstreetmap.org/relation/307573"},"population":241499431,"fifa":"PAK","car":{"signs":["PK"],"side":"left"},"timezones":["UTC+05:00"],"continents":["Asia"],"flag":"\uD83C\uDDF5\uD83C\uDDF0","name":{"common":"Pakistan","official":"Islamic Republic of Pakistan","nativeName":{"eng":{"official":"Islamic Republic of Pakistan","common":"Pakistan"},"urd":{"official":"اسلامی جمہوریۂ پاكستان","common":"پاكستان"}}},"currencies":{"PKR":{"symbol":"₨","name":"Pakistani rupee"}},"languages":{"eng":"English","urd":"Urdu"},"latlng":[30.0,70.0],"demonyms":{"eng":{"f":"Pakistani","m":"Pakistani"},"fra":{"f":"Pakistanaise","m":"Pakistanais"}},"translations":{"ara":{"official":"جمهورية باكستان الإسلامية","common":"باكستان"},"bre":{"official":"Republik islamek Pakistan","common":"Pakistan"},"ces":{"official":"Pákistánská islámská republika","common":"Pákistán"},"cym":{"official":"Islamic Republic of Pakistan","common":"Pakistan"},"deu":{"official":"Islamische Republik Pakistan","common":"Pakistan"},"est":{"official":"Pakistani Islamivabariik","common":"Pakistan"},"fin":{"official":"Pakistanin islamilainen tasavalta","common":"Pakistan"},"fra":{"official":"République islamique du Pakistan","common":"Pakistan"},"hrv":{"official":"Islamska Republika Pakistan","common":"Pakistan"},"hun":{"official":"Pakisztán","common":"Pakisztán"},"ind":{"official":"Republik Islam Pakistan","common":"Pakistan"},"ita":{"official":"Repubblica islamica del Pakistan","common":"Pakistan"},"jpn":{"official":"パキスタンIslamic共和国","common":"パキスタン"},"kor":{"official":"파키스탄 이슬람 공화국","common":"파키스탄"},"nld":{"official":"Islamitische Republiek Pakistan","common":"Pakistan"},"per":{"official":"جمهوری اسلامی پاکستان","common":"پاکستان"},"pol":{"official":"Islamska Republika Pakistanu","common":"Pakistan"},"por":{"official":"República Islâmica do Paquistão","common":"Paquistão"},"rus":{"official":"Исламская Республика Пакистан","common":"Пакистан"},"slk":{"official":"Islamská republika Pakistan","common":"Pakistan"},"spa":{"official":"República Islámica de Pakistán","common":"Pakistán"},"swe":{"official":"Islamiska republiken Pakistan","common":"Pakistan"},"tur":{"official":"Pakistan İslam Cumhuriyeti","common":"Pakistan"},"urd":{"official":"اسلامی جمہوریۂ پاکستان","common":"پاکستان"},"zho":{"official":"巴基斯坦伊斯兰共和国","common":"巴基斯坦"}},"cioc":"PAK","independent":True}]


service = CountryService(data)
print(service.get_capital("Pakistan"))
print(service.get_population("Pakistan"))
print(service.get_region("Pakistan"))
