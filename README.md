BULK SMTP Sending Script by UND3F3IND
This script facilitates the process of checking SMTP servers for their validity. It ensures whether given SMTP servers are functioning correctly by attempting to send an email through them.

┊Ｐｒｅｒｅｑｕｉｓｉｔｅｓ┊

•Python 3.x
•Required Libraries:
•sys
•time
•random
•shutil
•smtplib
•os
•concurrent.futures
•email.mime.multipart
•email.mime.text
•colorama

Make sure to have all the required libraries installed before executing the script. You can install them using pip:

BASH:
pip install colorama


【﻿Ｈｏｗ　ｔｏ　Ｕｓｅ】

1- Run the script:
BASH: python your_script_name.py
2- The script will display an animated banner and a welcoming message.
3- You will be prompted to enter the path to your SMTP list file. The expected format for each line in the SMTP list file is: HOST|PORT|USERNAME|PASSWORD
4- The script will then check each SMTP server in the list and display whether it's valid or not.
5- Valid SMTPs are saved to a file named validsmtp.txt.
6- Once completed, the script will summarize the results, showing the number of valid and invalid SMTPs, and the total time taken.

【﻿Ｆｅａｔｕｒｅｓ】
Animated intro with custom ASCII art.
Efficient SMTP checking using threading.
Clear color-coded console outputs for better readability.

【﻿Ｎｏｔｅｓ】
The script sends a test email to abc@abc.com. Ensure you replace this with your email address if you want to receive the test emails.
If you wish to adjust the number of threads used for SMTP checking, modify the max_workers value in the ThreadPoolExecutor function.

【﻿Ｄｉｓｃｌａｉｍｅｒ】
Please use this tool responsibly and ensure you have the necessary permissions when checking SMTP servers. Unauthorized use might violate terms of service or laws in some jurisdictions.

