import machine
import time
from machine import Pin, I2C
import ssd1306
import urequests
import network

# 定義紅外線接收器、蜂鳴器和OLED的引腳
ir_receiver_pin = 33  # 根據ESP32配置調整
buzzer_pin = 14  # 根據ESP32配置調整
oled_sda_pin = 21  # 根據ESP32配置調整
oled_scl_pin = 22  # 根據ESP32配置調整

# Line Notify Token
LINE_TOKEN = "qeq7lgasR3Fdit2SlhUnHUqnnM42Fpx112Szy8VJHMi"

# 初始化紅外線接收器、蜂鳴器和OLED
ir = machine.Pin(ir_receiver_pin, machine.Pin.IN)
buzzer = machine.PWM(machine.Pin(buzzer_pin), freq=4000, duty=0)  # 初始化PWM
i2c = I2C(-1, scl=Pin(oled_scl_pin), sda=Pin(oled_sda_pin))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Wi-Fi連接設定
ssid = 'N的iPhone'
passwd = '0985376648'

def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)  # Initializes the station interface
    wlan.active(True)  # Activates the WLAN interface
    connected = wlan.isconnected()  # Check if the connection was successful

    if not connected:  # if it is not connected
        print(f'Trying to connect to {ssid}')  # Display a message indicating an attempt to connect
        wlan.connect(ssid, passwd)  # Attempt to connect to the Wi-Fi network again
        for _ in range(200):  # Try to connect 100 times, waiting 0.1 seconds each time
            connected = wlan.isconnected()  # Check if the connection was successful
            if connected:
                break  # Break out of the loop if connected
            time.sleep(0.1)  # Wait for 0.1 seconds before checking again
            print('.', end='')  # Print progress dots to indicate ongoing connection attempts

    if connected:  # If connected successfully
        # Display successful connection and network configuration
        print(f'\nConnected to ssid {ssid}. Network config: {wlan.ifconfig()}')
    else:  # If the connection failed
        print(f'\nFailed. Not Connected to: {ssid}')  # Display a failure message

# 连接到Wi-Fi
connect_to_wifi()

def detect_motion(pin):
    print("Danger")
    play_family_song()
    send_line_notify("Danger!")
    oled.text("Danger!", 50, 20)
    oled.show()
def play_family_song():
    notes = [330, 262, 196, 262, 294, 392, 294, 330, 294, 196, 262]
    for note in notes:
        buzzer.freq(note)
        buzzer.duty(512)  # 蜂鳴器音量
        time.sleep(0.5)   # 播放每個音符的持續時間
        buzzer.duty(0)    # 關閉蜂鳴器
        time.sleep(0.1)   # 添加一點延遲，避免音符之間的干擾

def display_message(message):
    oled.fill(1)  # 清空OLED顯示
    oled.text("Danger!", 0, 0)
    oled.show()

def send_line_notify(message):
    if not message:
        print("Error: Message is empty.")
        return

    url = 'https://notify-api.line.me/api/notify'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer ' + LINE_TOKEN
    }
    data = {'message': message}
    response = urequests.post(url, headers=headers, data='message=' + message)

    print('Line Notify Response:', response.text)

# 設置中斷處理函數
ir.irq(trigger=machine.Pin.IRQ_RISING, handler=detect_motion)

# 主循環
while True:
    time.sleep(1)
