import base64
from seleniumbase import SB

# Ask the user for base64 input
b_input = 'aHR0cHM6Ly9raWNrLmNvbS9icnV0YWxsZXM='
des = base64.b64decode(b_input)
sa1 = des.decode('utf-8')
with SB(uc=True, test=True) as baiit:
    url = sa1
    baiit.uc_open_with_reconnect(url, 5)
    baiit.uc_gui_click_captcha()
    baiit.sleep(2)
    baiit.uc_gui_handle_captcha()
    while(baiit.is_element_present('video#video-player')):
        baiit.sleep(10)
  
