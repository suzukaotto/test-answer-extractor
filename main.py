import random, os, keyboard, time, pandas, json

# defalt value
numberOfQuestions = 25
questionNumber = 5
skipMode = False
ultraSkipMode = False
languageMode = 0

cursorPosY = 0

languageModeList = ["English", "한국어", "日本語", "中国語", "Русский", "Français", "Deutsch", "Nederlands", "عربي", "മലയാളം"]
languageList = {
    "한국어" : "korean",
    "English" : "english",
    "日本語" : "japanese",
    "中国語" : "chinese",
    "Русский" : "russian",
    "Français" : "french",
    "Deutsch" : "german",
    "Nederlands" : "dutch",
    "عربي" : "arabic",
    "മലയാളം" : "malayalam"
}

# min-max valuer
numberOfQuestions_minVal = 1
numberOfQuestions_maxVal = 100

questionNumber_minVal = 1
questionNumber_maxVal = 50

languageMode_minVal = 0
languageMode_maxVal = len(languageList.keys())-1

cursorPosY_minVal = 0
cursorPosY_maxVal = 4



# language file load
try:
    with open("./language.json", "r", encoding="utf-8") as languageData:
        languageData = json.load(languageData)
    
except Exception as e:
    print(f"An error occurred: {e}")
    exit(0)

def cls():
    os.system("cls")

def detect_key():
    global languageData
    while True:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_DOWN:
            return event.name

        
def raffle_page():
    global languageData
    try:
        global numberOfQuestions, questionNumber
        cls()
        result_data = {}
        
        def random_num():
            return random.randint(1, questionNumber)
            
        def print_dict_data(dictionary):
            df = pandas.DataFrame(list(dictionary.items()), columns=[languageData[languageList[languageModeList[languageMode]]]["raffle_page"]["num"], languageData[languageList[languageModeList[languageMode]]]["raffle_page"]["answer"]])
            print(df.to_string(justify="left", index=False))    

        def count_values(dictionary):
            series = pandas.Series(dictionary)
            value_counts = series.value_counts()
            sorted_counts = value_counts.sort_index()
        
            print(sorted_counts)
        
        for i in range(1, numberOfQuestions+1):
            raffle_num = random_num()
            result_data[i] = raffle_num
            
            if skipMode == False:
                cls()
                h = None
                j = 1
                for l in range(1, 9+1):
                    while True:
                        h = j
                        j = random_num()
                        if h == j and not (h == 1 and j == 1):
                            continue
                        else:
                            break
                    
                    print(f"{languageData[languageList[languageModeList[languageMode]]]["raffle_page"]["title"]}")
                    print(f"{i}. {languageData[languageList[languageModeList[languageMode]]]["raffle_page"]["sub_title"]} ({numberOfQuestions}/{i})")
                    for g in range(1, questionNumber+1):
                        if g == j:
                            print(f"[{g}] ", end="")
                        else:
                            print(f" {g}  ", end="")
                        
                    time.sleep(0.1)
                    cls()
            
            if skipMode == False:
                for l in range(1, 5+1):
                    cls()
                    print(f"{languageData[languageList[languageModeList[languageMode]]]["raffle_page"]["title"]}")
                    print(f"{i}. {languageData[languageList[languageModeList[languageMode]]]["raffle_page"]["sub_title"]} ({numberOfQuestions}/{i})")
                    for g in range(1, questionNumber+1):
                        if g == raffle_num:
                            if l % 2 == 0:
                                print(f" {g}  ", end="")
                            if l % 2 == 1:
                                print(f"[{g}] ", end="")
                                
                        else:
                            print(f" {g}  ", end="")
                            
                    time.sleep(0.2)
                time.sleep(0.5)
                
            else:
                if ultraSkipMode == False:
                    for l in range(1, 3+1):
                        cls()
                        print(f"{languageData[languageList[languageModeList[languageMode]]]["raffle_page"]["title"]}")
                        print(f"{i}. {languageData[languageList[languageModeList[languageMode]]]["raffle_page"]["sub_title"]} ({numberOfQuestions}/{i})")
                        for g in range(1, questionNumber+1):
                            if g == raffle_num:
                                    print(f"[{g}] ", end="")
                            else:
                                print(f" {g}  ", end="")
                    time.sleep(0.1)
        
        cls()
        print(f"{languageData[languageList[languageModeList[languageMode]]]["raffle_page"]["title"]}")
        
        print("<Result Data>")
        print_dict_data(result_data)
        print()
        
        print("<Sum Data>")
        count_values(result_data)
        print()
        
        print(f"{languageData[languageList[languageModeList[languageMode]]]["raffle_page"]["good_luck"]}")
        
        os.system("pause")
        
    except KeyboardInterrupt:
        cls()
        print(f"{languageData[languageList[languageModeList[languageMode]]]["raffle_page"]["title"]}")
        
        print("<Result Data>")
        print_dict_data(result_data)
        print()
        
        print("<Sum Data>")
        count_values(result_data)
        print()
        
        print(f"{languageData[languageList[languageModeList[languageMode]]]["raffle_page"]["good_luck"]}")
        
        print(f"{languageData[languageList[languageModeList[languageMode]]]["raffle_page"]["user_cancel_msg"]}")
        os.system("pause")

def set_page():
    global languageData
    global cursorPosY, numberOfQuestions, questionNumber, skipMode, ultraSkipMode
    global languageMode, languageList, languageModeList
    def print_page():
        global cursorPosY_maxVal
        print(f"{languageData[languageList[languageModeList[languageMode]]]["setting_page"]["title"]:20s}")
        print(f"{languageData[languageList[languageModeList[languageMode]]]["setting_page"]["manual"]:20s}\n")
        if cursorPosY == 0:
            print(f" >> {languageData[languageList[languageModeList[languageMode]]]["setting_page"]["menu1"]:20s} [{numberOfQuestions:^10d}]")
            print(f"    {languageData[languageList[languageModeList[languageMode]]]["setting_page"]["menu2"]:20s} [{questionNumber:^10d}]")
            print(f"    {languageData[languageList[languageModeList[languageMode]]]["setting_page"]["menu3"]:20s} [{languageModeList[languageMode]:^10s}]")
            print(f"    {languageData[languageList[languageModeList[languageMode]]]["setting_page"]["menu4"]:20s} [{skipMode:^10b}]")
            if skipMode == True:
                print(f"    {languageData[languageList[languageModeList[languageMode]]]["setting_page"]["menu5"]:20s} [{ultraSkipMode:^10b}]")
                cursorPosY_maxVal = 4
            else:
                cursorPosY_maxVal = 3
        elif cursorPosY == 1:
            print(f"    {languageData[languageList[languageModeList[languageMode]]]["setting_page"]["menu1"]:20s} [{numberOfQuestions:^10d}]")
            print(f" >> {languageData[languageList[languageModeList[languageMode]]]["setting_page"]["menu2"]:20s} [{questionNumber:^10d}]")
            print(f"    {languageData[languageList[languageModeList[languageMode]]]["setting_page"]["menu3"]:20s} [{languageModeList[languageMode]:^10s}]")
            print(f"    {languageData[languageList[languageModeList[languageMode]]]["setting_page"]["menu4"]:20s} [{skipMode:^10b}]")
            if skipMode == True:
                print(f"    {languageData[languageList[languageModeList[languageMode]]]["setting_page"]["menu5"]:20s} [{ultraSkipMode:^10b}]")
                cursorPosY_maxVal = 4
            else:
                cursorPosY_maxVal = 3
            
        elif cursorPosY == 2:
            print(f"    {languageData[languageList[languageModeList[languageMode]]]["setting_page"]["menu1"]:20s} [{numberOfQuestions:^10d}]")
            print(f"    {languageData[languageList[languageModeList[languageMode]]]["setting_page"]["menu2"]:20s} [{questionNumber:^10d}]")
            print(f" >> {languageData[languageList[languageModeList[languageMode]]]["setting_page"]["menu3"]:20s} [{languageModeList[languageMode]:^10s}]")
            print(f"    {languageData[languageList[languageModeList[languageMode]]]["setting_page"]["menu4"]:20s} [{skipMode:^10b}]")
            if skipMode == True:
                print(f"    {languageData[languageList[languageModeList[languageMode]]]["setting_page"]["menu5"]:20s} [{ultraSkipMode:^10b}]")
                cursorPosY_maxVal = 4
            else:
                cursorPosY_maxVal = 3
            
        elif cursorPosY == 3:
            print(f"    {languageData[languageList[languageModeList[languageMode]]]["setting_page"]["menu1"]:20s} [{numberOfQuestions:^10d}]")
            print(f"    {languageData[languageList[languageModeList[languageMode]]]["setting_page"]["menu2"]:20s} [{questionNumber:^10d}]")
            print(f"    {languageData[languageList[languageModeList[languageMode]]]["setting_page"]["menu3"]:20s} [{languageModeList[languageMode]:^10s}]")
            print(f" >> {languageData[languageList[languageModeList[languageMode]]]["setting_page"]["menu4"]:20s} [{skipMode:^10b}]")
            if skipMode == True:
                print(f"    {languageData[languageList[languageModeList[languageMode]]]["setting_page"]["menu5"]:20s} [{ultraSkipMode:^10b}]")
                cursorPosY_maxVal = 4
            else:
                cursorPosY_maxVal = 3
            
        elif cursorPosY == 4 and skipMode == True:
            print(f"    {languageData[languageList[languageModeList[languageMode]]]["setting_page"]["menu1"]:20s} [{numberOfQuestions:^10d}]")
            print(f"    {languageData[languageList[languageModeList[languageMode]]]["setting_page"]["menu2"]:20s} [{questionNumber:^10d}]")
            print(f"    {languageData[languageList[languageModeList[languageMode]]]["setting_page"]["menu3"]:20s} [{languageModeList[languageMode]:^10s}]")
            print(f"    {languageData[languageList[languageModeList[languageMode]]]["setting_page"]["menu4"]:20s} [{skipMode:^10b}]")
            if skipMode == True:
                print(f" >> {languageData[languageList[languageModeList[languageMode]]]["setting_page"]["menu5"]:20s} [{ultraSkipMode:^10b}]")
                cursorPosY_maxVal = 4
            else:
                cursorPosY_maxVal = 3
            
            
            
    cls()
    print_page()
    
    key = detect_key()
    
    if key == "esc":
        return 0
    
    if key == "w" or key == "W":
        cursorPosY += -1
    elif key == "s" or key == "S":
        cursorPosY += 1
    
    if key == "a" or key == "A":
        if cursorPosY == 0:
            numberOfQuestions += -1
            
        if cursorPosY == 1:
            questionNumber += -1
            
        if cursorPosY == 2:
            languageMode += -1
            
        if cursorPosY == 3:
            skipMode = False
            ultraSkipMode = False
            
        if cursorPosY == 4:
            ultraSkipMode = False
            
    elif key == "d" or key == "D":
        if cursorPosY == 0:
            numberOfQuestions += 1
            
        if cursorPosY == 1:
            questionNumber += 1
            
        if cursorPosY == 2:
            languageMode += 1
            
        if cursorPosY == 3:
            skipMode = True
            
        if cursorPosY == 4:
            ultraSkipMode = True
    
    if languageMode < languageMode_minVal:
        languageMode = languageMode_minVal
    if languageMode > languageMode_maxVal:
        languageMode = languageMode_maxVal
    
    if cursorPosY < cursorPosY_minVal:
        cursorPosY = cursorPosY_maxVal
    if cursorPosY > cursorPosY_maxVal:
        cursorPosY = cursorPosY_minVal
    
    if numberOfQuestions < numberOfQuestions_minVal:
        numberOfQuestions = numberOfQuestions_minVal
    if numberOfQuestions > numberOfQuestions_maxVal:
        numberOfQuestions = numberOfQuestions_maxVal
        
    if questionNumber < questionNumber_minVal:
        questionNumber = questionNumber_minVal
    if questionNumber > questionNumber_maxVal:
        questionNumber = questionNumber_maxVal
    
    cls()
    print_page()

def exit_page():
    global languageData
    cls()
    print(f"{languageData[languageList[languageModeList[languageMode]]]["exit_page"]["title"]}")
    print(f"{languageData[languageList[languageModeList[languageMode]]]["exit_page"]["end_msg"]}")
    exit(0)

while True:
    cls()
    print(f"""{languageData[languageList[languageModeList[languageMode]]]["main_page"]["menu"]["title"]}
          
        1. {languageData[languageList[languageModeList[languageMode]]]["main_page"]["menu"]["menu1"]}
        2. {languageData[languageList[languageModeList[languageMode]]]["main_page"]["menu"]["menu2"]}
        3. {languageData[languageList[languageModeList[languageMode]]]["main_page"]["menu"]["menu3"]}
        
>> """, end="")
    
    sel_num = detect_key()
    
    try:
        sel_num = int(sel_num)
        if not 1 <= sel_num < 4:
            ValueError()
    except:
        continue
    
    try:
        if sel_num == 1:
            raffle_page()
            
        elif sel_num == 2:
            cursorPosY = 0
            while True:
                if set_page() == 0: break
            
        elif sel_num == 3:
            exit_page()
    
    except Exception as e:
        print(f"An error occurred: {e}")
        os.system("pause")
        