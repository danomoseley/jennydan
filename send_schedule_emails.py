#!/usr/bin/python3.10

import boto3
from botocore.exceptions import ClientError

import configparser
import requests
import sys

config = configparser.RawConfigParser()
config.read('config.cfg')

cloudflare_api_token = config.get('cloudflare_d1', 'api_token')
cloudflare_account_id = config.get('cloudflare_d1', 'account_id')
cloudflare_database_id = config.get('cloudflare_d1', 'database_id')

endpoint = f"https://api.cloudflare.com/client/v4/accounts/{cloudflare_account_id}/d1/database/{cloudflare_database_id}/query"
data = {"sql": "SELECT email FROM rsvp where attending;"}
headers = {"Authorization": f"Bearer {cloudflare_api_token}", "Content-Type": "application/json"}

response = requests.post(endpoint, json=data, headers=headers).json()

# DELETE THIS TO DO IT LIVE
response = {
    'success': True,
    'result': [
        {
            'results': [
                {
                    'email': 'jenniferlynnstafford@gmail.com'
                },
                {
                    'email': 'danomoseley@gmail.com',
                }
            ]
        }
    ]
}

if response['success']:
    results = response['result'][0]['results']

    for result in results:
        SENDER = "Jenny & Dan's Wedding <hello@jennydan.com>"
        RECIPIENT = result['email']
        SUBJECT = "Wedding Weekend Details"

        BODY_TEXT = ( "Get Ready!\r\n"
                      "We are incredibly excited to see you this weekend and to have you witness our wedding! We have a few updates to the schedule and some final details to pass along.\r\n\r\n"
                      "It looks like we may have a rainy weekend. Please bring umbrellas and do an anti-rain dance! Our rain plan venue is the Cornwall Church located in the Farmer’s Museum. Should we decide to move forward with the rain plan we will send out another email.\r\n\r\n"
                      "For those of you attending brunch on Sunday, please park at our neighbor’s farm at 7163 State Highway 80. Follow signs for parking. Brunch will be held at the Moseley Camps on Steamboat Lane.\r\n\r\n"
                      "There will be guest trolly pickup and dropoff on Saturday at four main locations in / around Cooperstown. For those of you staying in the village of Cooperstown - please meet at the Otesaga pickup point. This way most of you won’t have to drive to and from the wedding and can focus on having a good time. Drop off locations will adapt should we move forward with the rain plan. We will also have the trolly taking guests home at the end of the night. As a reminder there is very limited rideshare (Taxi/Uber/Lyft) services in Cooperstown. Please refer to the schedules below:\r\n\r\n"
                      "Wedding Guest Pickup:\r\n"
                      "2:00 PM Amanda & Charlie Stafford + Stafford Family\r\n"
                      " - Pickup: 207 Co Rd 43 Schenevus NY\r\n"
                      " - Dropping Off: The Otesaga Hotel\r\n\r\n"
                      "3:15 PM\r\n"
                      " - Pickup: Steamboat Lane\r\n"
                      " - Dropping Off: Ceremony Venue\r\n\r\n"
                      "3:45 PM\r\n"
                      " - Pickup: Lake ‘n Pines Motel\r\n"
                      " - Dropping Off: Ceremony Venue\r\n\r\n"
                      "4:10 PM\r\n"
                      " - Pickup: The Otesaga Hotel\r\n"
                      " - Dropping Off: Ceremony Venue\r\n\r\n"
                      "5:00 PM\r\n"
                      " - Post ceremony the trolley will be available to take guests to the cocktail hour across the street\r\n\r\n"
                      "Wedding Guet Dropoff:\r\n"
                      " - Leaving reception at 9:00 PM, 10:00 PM, and 11:00 PM\r\n"
                      " - Dropping Off: All Locations\r\n\r\n"
                      "We have updated the wedding website with all of this information as well. www.jennydan.com/schedule\r\n\r\n"
                      "Cheers!\r\n"
                      "Jenny & Dan"
                    )

        BODY_HTML = f"""<!DOCTYPE html>
        <html xml:lang="en" lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
          <head>
            <!--Help character display properly.-->
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <!--Set the initial scale of the email.-->
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <!--Force Outlook clients to render with a better MS engine.-->
            <meta http-equiv="X-UA-Compatible" content="IE=Edge">
            <!--Help prevent blue links and autolinking-->
            <meta name="format-detection" content="telephone=no, date=no, address=no, email=no">
            <!--prevent Apple from reformatting and zooming messages.-->
            <meta name="x-apple-disable-message-reformatting">

            <!--target dark mode-->
            <meta name="color-scheme" content="light dark">
            <meta name="supported-color-schemes" content="light dark only">

            <!-- Allow for better image rendering on Windows hi-DPI displays. -->
            <!--[if mso]>
        <noscript>
            <xml>
              <o:OfficeDocumentSettings>
                <o:AllowPNG/>
                <o:PixelsPerInch>96</o:PixelsPerInch>
              </o:OfficeDocumentSettings>
            </xml>
        </noscript>
        <![endif]-->

            <!--to support dark mode meta tags-->
            <style type="text/css">
              :root {{
                color-scheme: light dark;
                supported-color-schemes: light dark;
              }}
            </style>

            <!--webfont code goes here-->
            <!--[if (gte mso 9)|(IE)]><!-->
            <!--webfont <link /> goes here-->
            <style>
              /*Web font over ride goes here
               h1, h2, h3, h4, h5, p, a, img, span, ul, ol, li {{ font-family: 'webfont name', Arial, Helvetica, sans-serif !important; }} */
            </style>
            <!--<![endif]-->

            <style type="text/css">
              * {{ box-sizing: border-box; }}
              .body-fix {{
                height: 100% !important;
                margin: 0 auto !important;
                padding: 0 !important;
                width: 100% !important;
                -webkit-text-size-adjust: 100%;
                -ms-text-size-adjust: 100%;
                -webkit-font-smoothing: antialiased;
                  word-spacing: normal;
              }}
              
              div[style*="margin:16px 0"] {{
                margin: 0 !important;
              }}
              
              table,
              td {{
                border-collapse: collapse !important;
                mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
                -webkit-text-size-adjust: 100%;
                -ms-text-size-adjust: 100%;
              }}
              
              img {{
                border: 0;
                line-height: 100%;
                outline: none;
                text-decoration: none;
                display: block;
              }}
              
              p,
              h1,
              h2,
              h3 {{
                padding: 0;
                margin: 0;
                font-family:'Trebuchet MS', Arial, sans-serif;
              }}
              p {{ font-size: 18px; line-height: 28px;  }}
              li,b {{ font-size: 18px; line-height: 28px; }}
              
              a[x-apple-data-detectors] {{
                color: inherit !important;
                text-decoration: none !important;
                font-size: inherit !important;
                font-family: inherit !important;
                font-weight: inherit !important;
                line-height: inherit !important;
              }}
              
              u+#body a {{
                color: inherit;
                text-decoration: none;
                font-size: inherit;
                font-family: inherit;
                font-weight: inherit;
                line-height: inherit;
              }}
              
              #MessageViewBody a {{
                color: inherit;
                text-decoration: none;
                font-size: inherit;
                font-family: inherit;
                font-weight: inherit;
                line-height: inherit;
              }}
              
              a:hover, .link:hover {{
                text-decoration: none !important;
              }}
              
              /*image hover effects for linked images*/
              .fadeimg {{
                transition: 0.3s !important;
                opacity: 1 !important;
              }}
              
              .fadeimg:hover {{
                transition: 0.3s !important;
                opacity: 0.5 !important;
              }}
              
              /* start CTA HOVER EFFECTS */
              .cta {{ transition: 0.3s !important; }}
              .cta span{{ transition: 0.3s !important; }}
              .cta:hover {{ transition: 0.5s !important; background-color: #004265 !important; transform: scale(1.05);}}
              .cta:hover span {{ transition: 0.3s !important; }}
              .cta-border:hover {{ border-bottom: 3px solid transparent !important; }}
              /* end CTA HOVER EFFECTS */
              
              /*hides mobile content on desktop*/
              .mobile {{
                display: none;
              }}
              
              
            </style>

            <!--mobile styles-->
            <style>
              @media screen and (max-width:600px) {{
                /*sets widths for mobile devices*/
                  .wMobile {{ width: 95% !important; }}
                  .wInner {{  width: 90% !important; }}
                  .wFull {{ width: 100% !important; }}
                  .imgFull {{ width: 100% !important; height: auto !important; }}
                
                /*changes visibility for content on mobile*/
                  .desktop {{ width: 0 !important; display: none !important; }}
                  .mobile {{ display: block !important; }}
                
                /*updates padding for mobile*/
                  .lPad-0 {{ padding-left: 0 !important; }}
                  .tPad-0 {{ padding-top: 0 !important; }}
                  .tPad-20 {{ padding-top: 20px !important; }}
                  .bPad-20 {{ padding-bottom: 20px !important; }}
                
                /*changes text alignment on mobile*/
                .lTxt {{ text-align: left !important; }}
              }}
            </style>

            <!--dark mode styles-->
            <!--these are just example classes that can be used.-->
            <style>
              @media (prefers-color-scheme: dark) {{
              
                /* Shows Dark Mode-Only Content, Like Images */
                .dark-img {{
                  display: block !important;
                  width: auto !important;
                  overflow: visible !important;
                  float: none !important;
                  max-height: inherit !important;
                  max-width: inherit !important;
                  line-height: auto !important;
                  margin-top: 0px !important;
                  visibility: inherit !important;
                }}
              
                /* Hides Light Mode-Only Content, Like Images */
                .light-img {{
                  display: none;
                  display: none !important;
                }}
              
                /* Custom Dark Mode Background Color */
                .darkmode {{
                  background-color: #0E0E0E !important;
                }}
                .darkmode2 {{
                  background-color: #093A52 !important;
                }}
                .darkmode3 {{
                  background-color: #262524 !important;
                }}
              
                /* Custom Dark Mode Font Colors */
                h1, h3, p, span, a, li {{
                  color: #fdfdfd !important;
                }}
                  h2, h2 a {{ color: #028383 !important; }}
                  
              
                /* Custom Dark Mode Text Link Color */
                .link {{ color: #028383 !important; }}
                .footer a.link{{ color: #fdfdfd !important; }}
              }}
              
              /* Copy dark mode styles for android support */
              /* Shows Dark Mode-Only Content, Like Images */
              [data-ogsc] .dark-img {{
                display: block !important;
                width: auto !important;
                overflow: visible !important;
                float: none !important;
                max-height: inherit !important;
                max-width: inherit !important;
                line-height: auto !important;
                margin-top: 0px !important;
                visibility: inherit !important;
              }}
              
              /* Hides Light Mode-Only Content, Like Images */
              [data-ogsc] .light-img {{
                display: none;
                display: none !important;
              }}
              
              /* Custom Dark Mode Background Color */
              [data-ogsc] .darkmode {{
                background-color: #100E11 !important;
              }}
              [data-ogsc] .darkmode2 {{
                background-color: #000000 !important;
              }}
              [data-ogsc] .darkmode3 {{
                background-color: #1b181d !important;
              }}
              
              /* Custom Dark Mode Font Colors */
              [data-ogsc] h1, [data-ogsc] h3, [data-ogsc] p, [data-ogsc] span, [data-ogsc] a, [data-ogsc] li {{
                color: #fdfdfd !important;
              }}
                [data-ogsc] h2, [data-ogsc] h2 a {{ color: #028383 !important; }}
              
              /* Custom Dark Mode Text Link Color */
              [data-ogsc] .link {{ color: #028383 !important; }}
                
              [data-ogsc] .footer a.link {{ color: #fdfdfd !important; }}
            </style>

            <!--correct superscripts in Outlook-->
            <!--[if (gte mso 9)|(IE)]>
                <style>
                  sup{{font-size:100% !important;}}
                </style>
                <![endif]-->
            <title>Jenny & Dan: Wedding Transportation Schedule</title>
          </head>

          <body id="body" class="darkmode body body-fix" bgcolor="#ffffff" style="background-color:#ffffff;">
            <div role="article" aria-roledescription="email" aria-label="Email from Jenny & Dan" xml:lang="en" lang="en">
              <!--hidden preheader with pre-header spacer hack-->
              <div class="litmus-builder-preview-text" style="display:none;">
                Information about the guest transportation to and from our wedding and final details.&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
              </div>
              <!--start of email-->
              <table class="darkmode3" bgcolor="#eeeeee" cellpadding="0" cellspacing="0" border="0" role="presentation" style="width:100%;">

                <!--main content area-->
                <tr>
                  <td align="center" valign="top" style="padding-top: 20px;">
                    <table class="wMobile darkmode" cellpadding="0" cellspacing="0" border="0" role="presentation" style="width:600px;background-color: #ffffff;">
                      <tr>
                        <td align="center" valign="top" style="padding:20px 0;">
                          <!--light mode logo image-->
                          <a href="https://www.jennydan.com"><img class="light-img" src="https://www.jennydan.com/img/jennydan-1721414290.png" width="283" height="78" alt="Jenny & Dan" style="color: #4a4a4a; font-family: 'Trebuchet MS', Arial, sans-serif; text-align:center; font-weight:bold; font-size:24px; line-height:28x; text-decoration: none; padding: 0;">

                            <!--dark mode logo image-->
                            <!--[if !mso]><! -->
                            <div class="dark-img" style="display:none; overflow:hidden; width:0px; max-height:0px; max-width:0px; line-height:0px; visibility:hidden;" align="center">
                              <img src="https://www.jennydan.com/img/jennydan-dark-1721414290.png"" width="283" height="78" alt="Jenny & Dan" style="color: #4a4a4a; font-family: 'Trebuchet MS', Arial, sans-serif; text-align:center; font-weight:bold; font-size:24px; line-height:28px; text-decoration: none; padding: 0;" border="0" />
                            </div>
                            <!--<![endif]-->
                          </a>
                        </td>
                      </tr>
                      <!--text area-->
                      <tr>
                        <td class="darkmode2" align="center" valign="top" style="padding:50px 0; background-color: #d7f1ff;">
                          <table class="wInner" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:500px;">
                            <tr>
                              <td align="left" valign="top">
                                <!--headline-->
                                <h1 style="font-size: 50px; line-height: 60px; color: #0a080b; font-weight: normal;">Get Ready!</h1>
                                <!--message-->
                                <p style="margin: 30px 0; color: #0a080b;">We are incredibly excited to see you this weekend and to have you witness our wedding! We have a few updates to the schedule and some final details to pass along.</p>
                                <p style="margin: 30px 0; color: #0a080b;">It looks like we may have a rainy weekend. Please bring umbrellas and do an anti-rain dance! Our rain plan venue is the Cornwall Church located in the Farmer’s Museum. Should we decide to move forward with the rain plan we will send out another email.</p>
                                <p style="margin: 30px 0; color: #0a080b;">For those of you attending brunch on Sunday, please park at our neighbor’s farm at 7163 State Highway 80. Follow signs for parking. Brunch will be held at the Moseley Camps on Steamboat Lane.</p>
                                <p style="margin: 30px 0; color: #0a080b;">There will be guest trolly pickup and dropoff on Saturday at four main locations in / around Cooperstown. For those of you staying in the village of Cooperstown - please meet at the Otesaga pickup point. This way most of you won’t have to drive to and from the wedding and can focus on having a good time. Drop off locations will adapt should we move forward with the rain plan. We will also have the trolly taking guests home at the end of the night. As a reminder there is very limited rideshare (Taxi/Uber/Lyft) services in Cooperstown. Please refer to the schedules below:</p>
                                <hr/>
                                <h2 style="font-size: 30px; line-height: 60px; color: #0a080b; font-weight: normal;">Wedding Guest Pickup</h2>
                                <p>
                                  <b>2:00pm</b>
                                  <ul>
                                    <li>Amanda & Charlie Stafford + Stafford Family</li>
                                    <li>Pickup: 207 Co Rd 43 Schenevus NY</li>
                                    <li>Dropping Off: The Otesaga Hotel</li>
                                  </ul>
                                  <b>3:15pm</b>
                                  <ul>
                                    <li>Pickup: Steamboat Lane</li>
                                    <li>Dropping Off: Ceremony Venue</li>
                                  </ul>
                                  <b>3:45pm</b>
                                  <ul>
                                    <li>Pickup: Lake ‘n Pines Motel</li>
                                    <li>Dropping Off: Ceremony Venue</li>
                                  </ul>
                                  <b>4:10pm</b>
                                  <ul>
                                    <li>Pickup: The Otesaga Hotel</li>
                                    <li>Dropping Off: Ceremony Venue</li>
                                  </ul>
                                  <b>5:00pm</b>
                                  <ul>
                                    <li>Post ceremony the trolley will be available to take guests to the cocktail hour across the street </li>
                                  </ul>
                                </p>
                                <h2 style="font-size: 30px; line-height: 60px; color: #0a080b; font-weight: normal;">Wedding Guest Dropoff</h2>
                                <p>
                                  <ul>
                                    <li>Leaving reception at 9:00 PM, 10:00 PM, and 11:00 PM</li>
                                    <li>Dropping Off: All Locations</li>
                                  <ul>
                                </p>
                                <p style="margin-top:40px;">
                                  We have updated the wedding website with all of this information as well: <a href="https://www.jennydan.com/schedule">www.jennydan.com</a>
                                </p>
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                      <tr>
                        <td align="center" valign="top">
                          <table class="wInner" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:500px;">
                            <tr>
                              <td align="center" valign="top" style="padding: 50px 0;">
                                <p class="lTxt" style="color:#0a080b; margin:0 0 0px;">
                                  Cheers!<br/>
                                  Jenny & Dan
                                </p>
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
                <!--footer-->
                <tr>
                  <td class="footer" align="center" valign="top" style="padding:50px 0;">
                    <p style="font-family: 'Trebuchet MS', Arial, sans-serif;font-size:14px;line-height:24px;mso-line-height-rule:exactly;color:#0a080b;margin-bottom:20px;">
                      <a href="https://www.jennydan.com/schedule" class="link" target="_blank" style="color: #0a080b; text-decoration: underline;">Schedule</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="https://www.jennydan.com/travel" class="link" target="_blank" style="color: #0a080b; text-decoration: underline;">Getting Here</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="https://www.jennydan.com/faq" class="link" target="_blank" style="color: #0a080b; text-decoration: underline;">FAQ</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="https://www.jennydan.com/things-to-do" class="link" target="_blank" style="color: #0a080b; text-decoration: underline;">Things To Do</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="https://www.jennydan.com/registry" class="link" target="_blank" style="color: #0a080b; text-decoration: underline;">Registry</a>
                    </p>
                  </td>
                </tr>
              </table>
            </div>

            <!--analytics-->

          </body>

        </html>
        """

        CHARSET = "UTF-8"

        client = boto3.client('ses', region_name="us-east-1")

        try:
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        RECIPIENT,
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': CHARSET,
                            'Data': BODY_HTML,
                        },
                        'Text': {
                            'Charset': CHARSET,
                            'Data': BODY_TEXT,
                        },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                    },
                },
                Source=SENDER
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent!:")
            print(RECIPIENT)
            print(response['MessageId'])
