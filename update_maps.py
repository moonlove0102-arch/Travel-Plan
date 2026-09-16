import csv

csv_path = r"c:\Code\Antigravity\Travel-Plan\google_maps_trip_import.csv"
kml_path = r"c:\Code\Antigravity\Travel-Plan\google_maps_trip_import.kml"

rows = [
    {
        "Name": "【P4 停車場】新天鵝堡 (Parkplatz P4)",
        "Time": "2026-10-06 13:30 抵達",
        "Category": "🅿️ 景點停車場",
        "Address": "Alpseestraße 27, 87645 Hohenschwangau, Germany",
        "Latitude": 47.5539,
        "Longitude": 10.7362,
        "Description": "【10/6 13:30 前停妥】新天鵝堡首選停車場。離往瑪麗恩橋之接駁公車站僅步行 2 分鐘，收費 €12/6小時。停妥後搭接駁公車至瑪麗恩橋拍照，再散步至大門參加 14:55 英文導覽。下山後可順遊阿爾卑斯湖 (Alpsee)。",
        "Google_Maps_Link": "https://www.google.com/maps/place/Parkplatz+P4/@47.5539,10.7362,17z"
    },
    {
        "Name": "【著名景點/世界遺產】維斯朝聖教堂 (Wieskirche)",
        "Time": "2026-10-07 09:40 - 10:20",
        "Category": "⭐ 著名景點 / 世界遺產",
        "Address": "Wies 12, 86989 Steingaden, Germany",
        "Latitude": 47.6806,
        "Longitude": 10.9008,
        "Description": "【著名景點 / 世界文化遺產】阿爾卑斯大道最璀璨的洛可可奇蹟。外觀被群山與高山草甸牛群環繞，內部為金碧輝煌的洛可可壁畫雕刻。停放在專屬 Parkplatz Wieskirche（前 2 小時 €2.00），停留約 30-40 分鐘。",
        "Google_Maps_Link": "https://www.google.com/maps/place/Wieskirche/@47.6806,10.9008,17z"
    },
    {
        "Name": "【著名景點/高山湖泊】瓦爾興湖・凱塞爾隘口觀景台 (Walchensee Kesselberg)",
        "Time": "2026-10-07 11:00 - 11:20",
        "Category": "⭐ 著名景點 / 高山湖泊",
        "Address": "Kesselbergstraße (B11), 82431 Kochel am See, Germany",
        "Latitude": 47.6258,
        "Longitude": 11.3414,
        "Description": "【著名景點 / 高山碧湖】被譽為「巴伐利亞的馬爾地夫/加勒比海」，德國海拔最高且最深的高山湖泊之一。湖水呈現翡翠綠與寶石藍，在凱塞爾隘口 (Kesselberg Pass) 觀景停車區臨停 15-20 分鐘俯瞰震撼全景。",
        "Google_Maps_Link": "https://www.google.com/maps/place/Aussichtspunkt+Kesselberg/@47.6258,11.3414,17z"
    },
    {
        "Name": "【基姆湖停車場】Prien Hafen Stock S1",
        "Time": "2026-10-07 12:15 - 13:45",
        "Category": "🅿️ 景點停車場",
        "Address": "Seestraße 118, 83209 Prien am Chiemsee, Germany",
        "Latitude": 47.8596,
        "Longitude": 12.3664,
        "Description": "【10/7 中午停放】基姆湖普林港口碼頭 S1 超大型專屬停車場（容量極大、好停車，單日僅約 €6.50）。停好車走至港口湖畔享用午餐（推薦基姆湖白鮭）、欣賞大渡輪與百年蒸汽火車。",
        "Google_Maps_Link": "https://www.google.com/maps/place/Parkplatz+Hafen+Stock+S1/@47.8596,12.3664,17z"
    },
    {
        "Name": "【超充站】Tesla Supercharger Bernau am Chiemsee",
        "Time": "2026-10-07 12:00 (可選中繼補電)",
        "Category": "⚡ Tesla 超充站",
        "Address": "Theodor-Sanne-Straße 4, 83233 Bernau am Chiemsee, Germany",
        "Latitude": 47.8105,
        "Longitude": 12.3694,
        "Description": "【10/7 基姆湖超充站】位於 A8 高速公路交流道旁，配備 8 樁 250kW V3/V4 超充樁，旁邊有休息站、Shell 與速食店，補電 15-20 分鐘即可直達薩爾斯堡。",
        "Google_Maps_Link": "https://www.google.com/maps/place/Tesla+Supercharger+Bernau+am+Chiemsee/@47.8105,12.3694,17z"
    },
    {
        "Name": "【薩爾斯堡停車場】H+ Hotel 地下停車場 (Tiefgarage Hauptbahnhof)",
        "Time": "2026-10-07 14:45 - 15:00 抵達停妥",
        "Category": "🅿️ 飯店停車場",
        "Address": "Südtiroler Pl. 13, 5020 Salzburg, Austria",
        "Latitude": 47.8136,
        "Longitude": 13.0453,
        "Description": "【10/7 15:00 前停妥】已訂飯店 H+ Hotel Salzburg 直通之地下停車場 (Tiefgarage Hauptbahnhof / Forum 1)。車停好後搭電梯直達飯店大廳 Check-in 放行李，完全免開車進老城徒步區。步行穿過米拉貝爾花園或搭無軌電車直達老城要塞。",
        "Google_Maps_Link": "https://www.google.com/maps/place/H%2B+Hotel+Salzburg/@47.8136,13.0453,17z"
    },
    {
        "Name": "【著名景點/皇家小鎮】巴德伊舍 & 皇家甜點店 (Bad Ischl - Café Zauner)",
        "Time": "2026-10-08 10:45 - 11:30",
        "Category": "⭐ 著名景點 / 皇家小鎮",
        "Address": "Auböckplatz 5, 4820 Bad Ischl, Austria",
        "Latitude": 47.7118,
        "Longitude": 13.6234,
        "Description": "【10/8 上午停靠】哈布斯堡皇家避暑溫泉小鎮，西西公主與奧匈帝國皇帝相遇訂婚之地。停放在市中心停車場 (Parkplatz Zentrum/Kurhaus)，步行至百年皇家御用甜點店 Café Zauner 喝維也納米朗琪咖啡、品嚐經典榛果雪茄蛋糕，漫步特勞恩河畔。",
        "Google_Maps_Link": "https://www.google.com/maps/place/Caf%C3%A9+Zauner/@47.7118,13.6234,17z"
    },
    {
        "Name": "【達赫斯坦纜車停車場】Dachstein Krippenstein Seilbahn Talstation",
        "Time": "2026-10-08 12:45 前停妥",
        "Category": "🅿️ 景點停車場",
        "Address": "Winkl 34, 4831 Obertraun, Austria",
        "Latitude": 47.5337,
        "Longitude": 13.7058,
        "Description": "【10/8 12:45 前停妥】達赫斯坦山 (Dachstein Krippenstein) 纜車下站大停車場。車牌辨識系統，單日 €5.00。先在此或山下輕裝吃午餐，12:55 拿好厚外套毛帽手套，13:00 刷票搭纜車至巨型冰洞與五指觀景台。",
        "Google_Maps_Link": "https://www.google.com/maps/place/Dachstein+Krippenstein-Seilbahn+Talstation/@47.5337,13.7058,17z"
    },
    {
        "Name": "【魔法森林/辛特湖停車場】Parkplatz Seeklause (P1)",
        "Time": "2026-10-09 13:30 - 16:30",
        "Category": "🅿️ 景點停車場",
        "Address": "Hinterseer Str. 104, 83486 Ramsau bei Berchtesgaden, Germany",
        "Latitude": 47.6044,
        "Longitude": 12.8585,
        "Description": "【10/9 13:30 前停妥】辛特湖 (Hintersee) 與魔法森林 (Zauberwald) 最佳專屬停車場【Parkplatz Seeklause (P1)】。緊鄰湖泊出水口閘門 (Seeklause) 與魔法森林步道起點。停好車直接步入魔法森林享受溪流巨石芬多精，並串聯辛特湖環湖木棧道。收費約 €5-€7。",
        "Google_Maps_Link": "https://www.google.com/maps/place/Parkplatz+Seeklause/@47.6044,12.8585,17z"
    },
    {
        "Name": "【著名景點/明信片教堂】拉姆紹教堂 (Pfarrkirche St. Sebastian Ramsau)",
        "Time": "2026-10-09 16:45 - 17:15",
        "Category": "⭐ 著名景點 / 經典明信片",
        "Address": "Im Tal 82, 83486 Ramsau bei Berchtesgaden, Germany",
        "Latitude": 47.6075,
        "Longitude": 12.8943,
        "Description": "【著名景點 / 德國明信片常客】德國阿爾卑斯最具代表性的木造尖頂小教堂與小木橋溪流，背倚雪山岩壁。回程順路臨停 15-20 分鐘拍照。",
        "Google_Maps_Link": "https://www.google.com/maps/place/Pfarrkirche+St.+Sebastian/@47.6075,12.8943,17z"
    },
    {
        "Name": "【國王湖大停車場】Großparkplatz Königssee",
        "Time": "2026-10-10 08:00 前停妥",
        "Category": "🅿️ 景點停車場",
        "Address": "Seestraße 3, 83471 Schönau am Königssee, Germany",
        "Latitude": 47.5925,
        "Longitude": 12.9861,
        "Description": "【10/10 08:00 前停妥】國王湖 (Königssee) 官方大停車場。離遊船碼頭步行約 5-7 分鐘（經 Seestraße 商店街）。單日票 €9.00（支援自動繳費機刷卡/投幣/Parkster）。停妥後步行至碼頭搭乘早班電動船直奔 Salet (Obersee 內湖)。",
        "Google_Maps_Link": "https://www.google.com/maps/place/Gro%C3%9Fparkplatz+K%C3%B6nigssee/@47.5925,12.9861,17z"
    },
    {
        "Name": "【國王湖遊船碼頭】Königssee Seelände (去程搭船起點)",
        "Time": "2026-10-10 08:30 - 09:00",
        "Category": "⛴️ 景點碼頭",
        "Address": "Seestraße 55, 83471 Schönau am Königssee, Germany",
        "Latitude": 47.5878,
        "Longitude": 12.9882,
        "Description": "國王湖電動船主碼頭與售票處。在此購買或持線上票登上開往最深處 Salet 的早班船（09:00 首班），去程坐右側靠窗看回音壁小號表演與紅蔥頭教堂水上全景。",
        "Google_Maps_Link": "https://www.google.com/maps/place/K%C3%B6nigssee+Seel%C3%A4nde/@47.5878,12.9882,17z"
    },
    {
        "Name": "【國王湖內湖碼頭】Anlegestelle Salet (終點站)",
        "Time": "2026-10-10 09:55 抵達",
        "Category": "⛴️ 景點碼頭",
        "Address": "Salet, 83471 Schönau am Königssee, Germany",
        "Latitude": 47.5251,
        "Longitude": 12.9735,
        "Description": "國王湖最深處碼頭，僅在 5 月中至 10 月中開放。下船後直接進入原始保護區步道，步行 15 分鐘至上湖 (Obersee)。注意回程末班船時間（約 16:30-17:10，碼頭立牌有標示）。",
        "Google_Maps_Link": "https://www.google.com/maps/place/Anlegestelle+Salet/@47.5251,12.9735,17z"
    },
    {
        "Name": "【國王湖仙境亮點】上湖木造船屋與天空之鏡 (Bootshaus am Obersee)",
        "Time": "2026-10-10 10:15 - 10:45",
        "Category": "⭐ 著名景點 / 天空之鏡",
        "Address": "Obersee, 83471 Schönau am Königssee, Germany",
        "Latitude": 47.5193,
        "Longitude": 12.9806,
        "Description": "國王湖最具代表性的神仙倒影！百年深色木造船屋佇立在如明鏡般清澈的綠寶石湖畔，清晨平靜無風，對岸千仞山壁倒映水中，宛如懸浮空中。",
        "Google_Maps_Link": "https://www.google.com/maps/place/Bootshaus+am+Obersee/@47.5193,12.9806,17z"
    },
    {
        "Name": "【高山世外牧場】Fischunkelalm (鮮牛奶木屋)",
        "Time": "2026-10-10 11:15 - 12:00",
        "Category": "⭐ 著名景點 / 高山牧場",
        "Address": "Fischunkelalm, 83471 Schönau am Königssee, Germany",
        "Latitude": 47.5125,
        "Longitude": 12.9888,
        "Description": "Obersee 對岸世外桃源牧場。背倚千仞巨石絕壁，草甸散養阿爾卑斯乳牛（牛鈴聲清脆）。百年木屋必喝新鮮冰牛奶 (€1.5-€2，濃醇回甘，只收現金) 與牛油黑麥麵包。",
        "Google_Maps_Link": "https://www.google.com/maps/place/Fischunkelalm/@47.5125,12.9888,17z"
    },
    {
        "Name": "【德國最高瀑布】羅特巴赫瀑布 (Röthbachfall)",
        "Time": "2026-10-10 12:00 - 12:30",
        "Category": "⭐ 著名景點 / 自然奇觀",
        "Address": "Röthbachfall, 83471 Schönau am Königssee, Germany",
        "Latitude": 47.5019,
        "Longitude": 13.0122,
        "Description": "德國境內落差最大（470 公尺！）的垂直巨瀑。冰川水自阿爾卑斯峭壁頂端分兩段傾瀉而下，谷底仰望垂直岩壁極具壓迫感與壯麗美。",
        "Google_Maps_Link": "https://www.google.com/maps/place/R%C3%B6thbachfall/@47.5019,13.0122,17z"
    },
    {
        "Name": "【回程名物午餐】聖巴多羅買教堂 & 煙燻鱒魚 (St. Bartholomä & Fischer)",
        "Time": "2026-10-10 14:00 - 15:30",
        "Category": "⭐ 著名景點 / 湖中教堂",
        "Address": "St. Bartholomä 1, 83471 Schönau am Königssee, Germany",
        "Latitude": 47.5447,
        "Longitude": 12.9725,
        "Description": "國王湖湖心半島之標誌性紅蔥頭教堂。回程在此下船，參觀建於 12 世紀之古老修道院教堂，並在旁邊的「Fischer vom Königssee」品嚐國王湖產橡木桶現燻紅點鱒魚 (Steckerlfisch) 配黑麵包。",
        "Google_Maps_Link": "https://www.google.com/maps/place/St.+Bartholom%C3%A4/@47.5447,12.9725,17z"
    },
    {
        "Name": "【阿姆巴赫峽谷停車場】Parkplatz Almbachklamm (Kugelmühle)",
        "Time": "2026-10-11 09:30 - 12:00",
        "Category": "🅿️ 景點停車場",
        "Address": "Kugelmühlweg 18, 83487 Marktschellenberg, Germany",
        "Latitude": 47.6698,
        "Longitude": 13.0336,
        "Description": "【10/11 上午停泊】東側著名大峽谷阿姆巴赫峽谷 (Almbachklamm) 入口停車場（免費停放）。起點為德國現存最古老的水力「大理石彈珠磨坊 (Kugelmühle)」。步行進入木棧道與吊橋欣賞激流飛瀑，往返約 1.5-2 小時。入口旁 Gasthof Kugelmühle 週日有開，可在此吃午餐喝咖啡。",
        "Google_Maps_Link": "https://www.google.com/maps/place/Parkplatz+Almbachklamm/@47.6698,13.0336,17z"
    },
    {
        "Name": "【全景公路北收費站】Roßfeldpanoramastraße Mautstelle Nord",
        "Time": "2026-10-11 13:30",
        "Category": "🚗 景觀公路收費站",
        "Address": "Roßfeldstraße 150, 83471 Berchtesgaden, Germany",
        "Latitude": 47.6565,
        "Longitude": 13.0768,
        "Description": "【10/11 下午上山】德國最高景觀公路「北收費站」（從阿姆巴赫峽谷開車過來僅 10 分鐘！）。小客車通行費約 €9.00（全車包價，含所有觀景停車場）。付費後沿著壯麗阿爾卑斯盤山公路爬升至 1,570 公尺頂峰。",
        "Google_Maps_Link": "https://www.google.com/maps/place/Mautstelle+Nord+Ro%C3%9Ffeldpanoramastra%C3%9Fe/@47.6565,13.0768,17z"
    },
    {
        "Name": "【全景公路頂峰稜線】Aussichtspunkt Roßfeld (Scheitelstrecke)",
        "Time": "2026-10-11 14:00 - 15:30",
        "Category": "⭐ 著名景點 / 高山全景",
        "Address": "Roßfeldpanoramastraße, 83471 Berchtesgaden, Germany",
        "Latitude": 47.6253,
        "Longitude": 13.0898,
        "Description": "【德國最高公路景觀台】海拔 1,570m 稜線大停車場。沿德奧邊界稜線木棧道散步，一腳踏在德國、一腳踏在奧地利！360 度俯瞰奧地利薩爾斯堡平原、薩爾察赫河谷與遠方達赫斯坦雪峰。午後陽光順光，拍照壯觀無比。下坡動能回充 10-15% 電量。",
        "Google_Maps_Link": "https://www.google.com/maps/place/Aussichtspunkt+Ro%C3%9Ffeld/@47.6253,13.0898,17z"
    },
    {
        "Name": "【中繼咖啡/休息站】Dinzler Kaffeerösterei am Irschenberg",
        "Time": "2026-10-12 12:00 - 13:00",
        "Category": "☕ 景觀咖啡館 / 中繼休息站",
        "Address": "Wendling 15, 83737 Irschenberg, Germany",
        "Latitude": 47.8174,
        "Longitude": 11.8906,
        "Description": "【10/12 中繼休息站】A8 高速公路旁極富盛名的精品咖啡烘焙館與景觀餐廳。設有大型停車場與 Tesla 超充站（Tesla Supercharger Irschenberg）。可在此停靠 30-45 分鐘享用現磨莊園咖啡、精緻甜點或輕食午餐。",
        "Google_Maps_Link": "https://www.google.com/maps/place/Dinzler+Kaffeer%C3%B6sterei/@47.8174,11.8906,17z"
    },
    {
        "Name": "【慕尼黑心臟】瑪利亞廣場 (Marienplatz)",
        "Time": "2026-10-12 17:00 - 20:30",
        "Category": "⭐ 著名景點 / 老城市中心",
        "Address": "Marienplatz 1, 80331 München, Germany",
        "Latitude": 48.1374,
        "Longitude": 11.5755,
        "Description": "【10/12 傍晚散步】慕尼黑老城核心心臟。從 Premier Inn 飯店旁搭 S-Bahn 直達僅 8 分鐘！欣賞哥德式新市政廳木偶鐘 (Glockenspiel)、散步至聖母教堂 (Frauenkirche)、穀物市場 (Viktualienmarkt)，採購德國伴手禮與享用輕鬆晚餐。",
        "Google_Maps_Link": "https://www.google.com/maps/place/Marienplatz/@48.1374,11.5755,17z"
    },
    {
        "Name": "【返程搭機】慕尼黑機場 (Flughafen München)",
        "Time": "2026-10-13 上午",
        "Category": "✈️ 機場返程",
        "Address": "Nordallee 25, 85356 München, Germany",
        "Latitude": 48.3537,
        "Longitude": 11.7750,
        "Description": "【10/13 返台班機】德奧捷自駕 13 日圓滿終點。從飯店門口 Laim / Hirschgarten 站搭乘 S-Bahn（S1 或 S8 一車直達機場約 40 分鐘），辦理國泰航空 CX 登機、行李托運與海關退稅。",
        "Google_Maps_Link": "https://www.google.com/maps/place/Munich+Airport/@48.3537,11.7750,17z"
    },
    {
        "Name": "【取車/還車】Nextmove 慕尼黑站點",
        "Time": "2026-10-06 09:00 取車 / 10-12 16:00 還車",
        "Category": "🚗 租車取還",
        "Address": "Landsberger Str. 318D, 80687 München, Germany",
        "Latitude": 48.1408,
        "Longitude": 11.5072,
        "Description": "Tesla Model 3 RWD 取還車地點（合約 VNN-26-106734-2，車牌 W-AK 7176E）。含充電一口價 €39（免滿電還車）。",
        "Google_Maps_Link": "https://www.google.com/maps/place/nextmove+M%C3%BCnchen/@48.1408,11.5072,17z"
    },
    {
        "Name": "【第 5 晚住宿】Hotel Tessin (特辛酒店)",
        "Time": "2026-10-05 Check-in",
        "Category": "🏨 住宿",
        "Address": "Landsberger Str. 436, 81241 München, Germany",
        "Latitude": 48.1436,
        "Longitude": 11.4883,
        "Description": "慕尼黑 Laim 區，搭 FlixBus 抵達慕尼黑後的過夜飯店，鄰近 Nextmove 取車點，9/3 已扣款/預授權完成。",
        "Google_Maps_Link": "https://www.google.com/maps/place/Hotel+Tessin/@48.1436,11.4883,17z"
    },
    {
        "Name": "【第 6 晚住宿】中央城旅館 (Central City Hotel Füssen)",
        "Time": "2026-10-06 Check-in",
        "Category": "🏨 住宿",
        "Address": "Bahnhofstraße 12, 87629 Füssen, Germany",
        "Latitude": 47.5701,
        "Longitude": 10.7011,
        "Description": "富森市中心，近火車站與老街，附設電動車充電設施，新天鵝堡行程結束後下榻。",
        "Google_Maps_Link": "https://www.google.com/maps/place/Central+City+Hotel/@47.5701,10.7011,17z"
    },
    {
        "Name": "【第 7 晚住宿】H+ Hotel Salzburg",
        "Time": "2026-10-07 Check-in (15:00)",
        "Category": "🏨 住宿",
        "Address": "Südtiroler Pl. 13, 5020 Salzburg, Austria",
        "Latitude": 47.8136,
        "Longitude": 13.0453,
        "Description": "薩爾斯堡火車站旁，交通極為便利，已付清。地下直通 Tiefgarage Hauptbahnhof 停車場，可先停妥行李後漫步過河至老城要塞。",
        "Google_Maps_Link": "https://www.google.com/maps/place/H%2B+Hotel+Salzburg/@47.8136,13.0453,17z"
    },
    {
        "Name": "【第 8 晚住宿】Dormio Resort Obertraun",
        "Time": "2026-10-08 Check-in",
        "Category": "🏨 住宿",
        "Address": "Obertraun 300, 4831 Obertraun, Austria",
        "Latitude": 47.5531,
        "Longitude": 13.6896,
        "Description": "上特勞恩湖畔渡假村，具備完善充電設施，已付清。近達赫斯坦纜車站。",
        "Google_Maps_Link": "https://www.google.com/maps/place/Dormio+Resort+Obertraun/@47.5531,13.6896,17z"
    },
    {
        "Name": "【第 9-11 晚基地】Explorer Hotel Berchtesgaden",
        "Time": "2026-10-09 至 10-12 連住 3 晚",
        "Category": "🏨 住宿",
        "Address": "Hofreitstr. 7, 83471 Schönau am Königssee, Germany",
        "Latitude": 47.6046,
        "Longitude": 12.9868,
        "Description": "【第 9-11 晚大本營】位於舍瑙阿姆克尼格塞 (Schönau am Königssee)，離國王湖大停車場與碼頭僅 2.5 公里（開車 3-4 分鐘直達，完全無需進入貝希特斯加登市區！）。附設電動車充電樁與阿爾卑斯三溫暖桑拿放鬆設施。",
        "Google_Maps_Link": "https://www.google.com/maps/place/Explorer+Hotel+Berchtesgaden/@47.6046,12.9868,17z"
    },
    {
        "Name": "【第 12 晚住宿】Premier Inn München City West",
        "Time": "2026-10-12 Check-in",
        "Category": "🏨 住宿",
        "Address": "Landsberger Str. 312, 80687 München, Germany",
        "Latitude": 48.1409,
        "Longitude": 11.5085,
        "Description": "慕尼黑 Laim 區，緊鄰 Nextmove 還車站點，已付清。10/12 還車後步行直接入住，隔天直奔機場。",
        "Google_Maps_Link": "https://www.google.com/maps/place/Premier+Inn+Munich+City+West+hotel/@48.1409,11.5085,17z"
    }
]

def get_style_info(cat):
    if "停車" in cat:
        return "icon-parking", "🅿️ 景點停車場"
    elif "景點" in cat or "⭐" in cat:
        return "icon-sight", "⭐ 觀光景點"
    elif "住宿" in cat:
        return "icon-hotel", "🏨 住宿飯店"
    elif "超充" in cat:
        return "icon-charger", "⚡ Tesla 超充站"
    elif "碼頭" in cat:
        return "icon-dock", "⛴️ 景點碼頭"
    elif "咖啡" in cat:
        return "icon-cafe", "☕ 景觀咖啡館"
    elif "租車" in cat or "收費站" in cat:
        return "icon-car", "🚗 租車與公路"
    elif "機場" in cat:
        return "icon-airport", "✈️ 機場返程"
    else:
        return "icon-sight", "⭐ 觀光景點"

# Normalize Category for clean grouping in Google My Maps
for r in rows:
    style_id, std_cat = get_style_info(r["Category"])
    r["Category"] = std_cat
    r["_style_id"] = style_id

fieldnames = ["Name", "Time", "Category", "Address", "Latitude", "Longitude", "Description", "Google_Maps_Link"]

with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(rows)

print("Updated CSV written.")

# Update KML with embedded styles and distinct icons
kml_header = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>歐洲自駕旅行地圖 (Travel-Plan)</name>
    <description>德奧捷 13 日純電自駕 — 核心停車場、著名景點、充電站、住宿與站點標記</description>

    <!-- 停車場專用圖示 (藍色 P) -->
    <Style id="icon-parking">
      <IconStyle>
        <color>ffd1881e</color>
        <scale>1.2</scale>
        <Icon>
          <href>http://maps.google.com/mapfiles/kml/shapes/parking_lot.png</href>
        </Icon>
      </IconStyle>
    </Style>

    <!-- 觀光景點專用圖示 (鮮紅星號/相機) -->
    <Style id="icon-sight">
      <IconStyle>
        <color>ff2257ff</color>
        <scale>1.2</scale>
        <Icon>
          <href>http://maps.google.com/mapfiles/kml/shapes/camera.png</href>
        </Icon>
      </IconStyle>
    </Style>

    <!-- 住宿飯店專用圖示 (紫色床鋪) -->
    <Style id="icon-hotel">
      <IconStyle>
        <color>ffaa248e</color>
        <scale>1.2</scale>
        <Icon>
          <href>http://maps.google.com/mapfiles/kml/shapes/lodging.png</href>
        </Icon>
      </IconStyle>
    </Style>

    <!-- Tesla 超充站專用圖示 (綠色閃電/加油站) -->
    <Style id="icon-charger">
      <IconStyle>
        <color>ff47a043</color>
        <scale>1.2</scale>
        <Icon>
          <href>http://maps.google.com/mapfiles/kml/shapes/gas_stations.png</href>
        </Icon>
      </IconStyle>
    </Style>

    <!-- 碼頭渡輪專用圖示 (青藍碼頭/渡輪) -->
    <Style id="icon-dock">
      <IconStyle>
        <color>ffc1ac00</color>
        <scale>1.2</scale>
        <Icon>
          <href>http://maps.google.com/mapfiles/kml/shapes/marina.png</href>
        </Icon>
      </IconStyle>
    </Style>

    <!-- 景觀咖啡專用圖示 (琥珀色咖啡杯) -->
    <Style id="icon-cafe">
      <IconStyle>
        <color>ff008cfb</color>
        <scale>1.2</scale>
        <Icon>
          <href>http://maps.google.com/mapfiles/kml/shapes/coffee.png</href>
        </Icon>
      </IconStyle>
    </Style>

    <!-- 租車與公路專用圖示 (灰藍車輛) -->
    <Style id="icon-car">
      <IconStyle>
        <color>ff7a6e54</color>
        <scale>1.2</scale>
        <Icon>
          <href>http://maps.google.com/mapfiles/kml/shapes/cabs.png</href>
        </Icon>
      </IconStyle>
    </Style>

    <!-- 機場返程專用圖示 (深藍飛機) -->
    <Style id="icon-airport">
      <IconStyle>
        <color>ffab4939</color>
        <scale>1.2</scale>
        <Icon>
          <href>http://maps.google.com/mapfiles/kml/shapes/airports.png</href>
        </Icon>
      </IconStyle>
    </Style>
"""
kml_footer = """  </Document>
</kml>
"""
placemarks = []
for r in rows:
    name = r["Name"]
    time_val = r["Time"]
    desc = r["Description"]
    addr = r["Address"]
    lat = r["Latitude"]
    lon = r["Longitude"]
    link = r["Google_Maps_Link"]
    style_id = r.get("_style_id", "icon-sight")
    
    desc_html = f"""<![CDATA[
      <p><b>類別：</b>{r['Category']}</p>
      <p><b>時間：</b>{time_val}</p>
      <p><b>地址：</b>{addr}</p>
      <p><b>說明：</b>{desc}</p>
      <p><a href="{link}" target="_blank">👉 在 Google Maps 中開啟導航</a></p>
    ]]>"""
    
    pm = f"""    <Placemark>
      <name>{name}</name>
      <styleUrl>#{style_id}</styleUrl>
      <description>{desc_html}</description>
      <Point>
        <coordinates>{lon},{lat},0</coordinates>
      </Point>
    </Placemark>"""
    placemarks.append(pm)

with open(kml_path, "w", encoding="utf-8") as f:
    f.write(kml_header + "\n".join(placemarks) + "\n" + kml_footer)

print("Updated KML written.")
