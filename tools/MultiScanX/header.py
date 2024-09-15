#!/usr/bin/env python
import requests
def SecurityHeader():
 print("""	
 *-------------------------------------------------------------------------*
 * Valid Url Example:- https://www.facebook.com/profile.php?id=100024869...*
 *                  :- https://www.youtube.com/channel/UC0XeF90vczK........*
 *                  :- https://mail.google.com/mail/u/0/#sent/Ktbx.........*
 *                  :- https://github.com/Dipenluitel/Linux-Electrons------*
 *-------------------------------------------------------------------------*
 """)
 site = input("Enter The Url:- ")
 headers = requests.get(site).headers
 print(headers)
 print("\n\n ::::::Connection Sucessfully Established:::::::::::")
 print("\n\tCookies with Expired Date Captured")
 print("\n\t X-Frame-Options Captured")
 print("\n\t X-Content-Type-Options Captured")
 input("\n\nPress Enter To Exit")
SecurityHeader()
