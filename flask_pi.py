from flask import Flask

index_html='''Flask pi control<br>
<button onclick="window.location.href=\'/left\'">모터 왼쪽으로</button>
<button onclick="window.location.href=\'/right\'">모터 오른쪽으로</button>
<button onclick="window.location.href=\'/led_on\'">LED 켜기</button>
<button onclick="window.location.href=\'/led_off\'">LED 끄기</button>

'''
app = Flask(__name__)

@app.route("/")
def hello():
    #처음 접속 화면
    return index_html

@app.route("/left")
def turn_left():
    #서보 모터 제어 코드 추가

    a = index_html+"왼쪽으로"
    return a

@app.route("/right")
def turn_right():
    #서보 모터 제어 코드 추가
    
    a = index_html+"오른쪽으로"
    return a

@app.route("/led_on")
def led_on():
    #LED제어 코드 추가
    
    a = index_html+"LED켜기"
    return a

@app.route("/led_off")
def led_off():
    #LED제어 코드 추가
    
    a = index_html + "LED끄기"
    return a

app.run(host='0.0.0.0', port=80, debug=True)

