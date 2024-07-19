#!/usr/bin/python3.10

import boto3
from botocore.exceptions import ClientError

SENDER = "Jenny & Dan's Wedding <hello@jennydan.com>"
RECIPIENT = "danomoseley@gmail.com"
#RECIPIENT = "jenniferlynnstafford@gmail.com"
#RECIPIENT = "stafford.94@gmail.com"

SUBJECT = "Please Choose Your Dinner For Our Wedding"

rsvp_uuid = "e10f5182a2c549ecbcb85b28e6b2202a"

BODY_TEXT = ( "Thank you for RSVPing to our wedding!\r\n"
              "Please choose your dinner options for our reception by visiting the following link: "
             f"https://www.jennydan.com/meal/{rsvp_uuid}\r\n"
              "Please finalize your options by August 1st.\r\n\r\n"
              "We are so happy you can make it to celebrate with us.\r\n"
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
    <title>Jenny & Dan: Please Choose Your Dinner For Our Wedding</title>
  </head>

  <body id="body" class="darkmode body body-fix" bgcolor="#ffffff" style="background-color:#ffffff;">
    <div role="article" aria-roledescription="email" aria-label="Email from Jenny & Dan" xml:lang="en" lang="en">
      <!--hidden preheader with pre-header spacer hack-->
      <!--start of email-->
      <table class="darkmode3" bgcolor="#eeeeee" cellpadding="0" cellspacing="0" border="0" role="presentation" style="width:100%;">

        <!--main content area-->
        <tr>
          <td align="center" valign="top" style="padding-top: 20px;">
            <table class="wMobile darkmode" cellpadding="0" cellspacing="0" border="0" role="presentation" style="width:600px;background-color: #ffffff;">
              <tr>
                <td align="center" valign="top" style="padding:20px 0;">
                  <!--light mode logo image-->
                  <a href="https://www.jennydan.com"><img class="light-img" src="https://www.jennydan.com/img/jennydan-1721414290.png" width="283" height="78" alt="jennydan" style="color: #4a4a4a; font-family: 'Trebuchet MS', Arial, sans-serif; text-align:center; font-weight:bold; font-size:24px; line-height:28x; text-decoration: none; padding: 0;">

                    <!--dark mode logo image-->
                    <!--[if !mso]><! -->
                    <div class="dark-img" style="display:none; overflow:hidden; width:0px; max-height:0px; max-width:0px; line-height:0px; visibility:hidden;" align="center">
                      <img src="https://www.jennydan.com/img/jennydan-dark-1721414290.png"" width="283" height="78" alt="Jenny & Dan" style="color: #4a4a4a; font-family: 'Trebuchet MS', Arial, sans-serif; text-align:center; font-weight:bold; font-size:24px; line-height:28px; text-decoration: none; padding: 0;" border="0" />
                    </div>
                    <!--<![endif]-->
                  </a>
                </td>
              </tr>
              <!--hero image-->
              <tr>
                <td align="center" valign="top">
                  <a href="https://www.jennydan.com" target="_blank"><img src="https://www.jennydan.com/img/us-1721409066.jpg" class="fadeimg" width="600" height="280" alt="A plant in a white pot on a table" style="width: 100%; max-width: 600px; height: auto;" /></a>
                </td>
              </tr>

              <!--text area-->
              <tr>
                <td class="darkmode2" align="center" valign="top" style="padding:50px 0; background-color: #d7f1ff;">
                  <table class="wInner" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:500px;">
                    <tr>
                      <td align="left" valign="top">
                        <!--headline-->
                        <h1 style="font-size: 50px; line-height: 60px; color: #0a080b; font-weight: normal;">Thank you for RSVPing to our wedding</h1>
                        <!--message-->
                        <p style="margin: 30px 0; color: #0a080b;">Please choose your dinner options for our reception by visiting the link below</p>

                        <!--CTA-->
                        <a href="https://www.jennydan.com/meal/{rsvp_uuid}" class="cta" style="background-color: #1e5786; font-size: 18px; font-family: 'Trebuchet MS', Arial, sans-serif; font-weight:bold; text-decoration: none; padding: 14px 20px; color: #ffffff; display:inline-block; mso-padding-alt:0;"><!--[if mso]><i style="letter-spacing: 25px;mso-font-width:-100%;mso-text-raise:30pt">&nbsp;</i><![endif]--><span style="mso-text-raise:15pt;">CHOOSE YOUR MEAL</span><!--[if mso]><i style="letter-spacing: 25px;mso-font-width:-100%">&nbsp;</i><![endif]--></a>
                        
                        <p style="margin: 30px 0; color: #0a080b;">Please finalize your options by August 1st.</p>
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
                          We are so happy you can make it to celebrate with us.<br/><br/>
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
    print("Email sent! Message ID:"),
    print(response['MessageId'])
