import sys
import time
import random
import shutil
import smtplib
import os
import concurrent.futures
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import colorama
from colorama import init, Fore, Back, Style


VALIDS = 0
INVALIDS = 0
toaddr = "abc@abc.com"  #### YOUR EMAIL ADRESSE HERE #####

if os.name == 'nt':
    os.system('cls')

init()


def interpolate_rgb(rgb1, rgb2, ratio):
    r = rgb1[0] + (rgb2[0] - rgb1[0]) * ratio
    g = rgb1[1] + (rgb2[1] - rgb1[1]) * ratio
    b = rgb1[2] + (rgb2[2] - rgb1[2]) * ratio
    return (r, g, b)

green = (0, 1, 0)
white = (1, 1, 1)
black = (0, 0, 0)

segments = 8
ratios = [i/segments for i in range(segments)]

colors = []
for ratio in ratios[:4]:
    colors.append(interpolate_rgb(green, black, ratio * 2))

for ratio in ratios[4:]:
    colors.append(interpolate_rgb(black, white, (ratio - 0.5) * 2))


colorama_colors = [Fore.GREEN, Fore.GREEN, Fore.GREEN, Fore.WHITE, Fore.WHITE, Fore.WHITE, Fore.WHITE, Fore.WHITE]

lines = [
    "888     888 888b    888 8888888b.   .d8888b.  8888888888  .d8888b.  8888888 888b    888 8888888b.",
    "888     888 8888b   888 888  \"Y88b d88P  Y88b 888        d88P  Y88b   888   8888b   888 888  \"Y88b",
    "888     888 88888b  888 888    888      .d88P 888             .d88P   888   88888b  888 888    888",
    "888     888 888Y88b 888 888    888     8888\"  8888888        8888\"    888   888Y88b 888 888    888",
    "888     888 888 Y88b888 888    888      \"Y8b. 888             \"Y8b.   888   888 Y88b888 888    888",
    "888     888 888  Y88888 888    888 888    888 888        888    888   888   888  Y88888 888    888",
    "Y88b. .d88P 888   Y8888 888  .d88P Y88b  d88P 888        Y88b  d88P   888   888   Y8888 888  .d88P",
    "\"Y88888P\"  888    Y888 8888888P\"   \"Y8888P\"  888         \"Y8888P\"  8888888 888    Y888 8888888P\""


]



columns, rows = shutil.get_terminal_size()


def centered_text(text, total_columns):
    left_padding = (total_columns - len(text)) // 2
    return ' ' * left_padding + text


top_padding = (rows - len(lines)) // 4


intro_text = ''
for _ in range(top_padding):
    intro_text += '\n'  

for line, color in zip(lines, colorama_colors):
    left_padding = (columns - len(line)) // 2  
    intro_text += ' ' * left_padding + f'{color}{line}\n'


welcome_text = centered_text(f'{Back.WHITE + Fore.BLACK}Welcome to the {Fore.GREEN}BULK SMTP Sending Script by {Fore.BLACK}UND3F3IND! {Back.BLACK + Fore.MAGENTA}\n\n Lets Get Started.{Style.RESET_ALL}', columns)
welcome_delay = 0.08  


def animate_intro(text, delay=0.003):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)


animate_intro(intro_text)
print()  
animate_intro(welcome_text, welcome_delay)
print(Fore.BLUE + Back.WHITE + "" + Style.RESET_ALL)



def check(smtp):
    global VALIDS, INVALIDS

    try:
        HOST, PORT, usr, pas = smtp.strip().split('|')
        server = smtplib.SMTP(HOST, int(PORT), timeout=10)
        server.ehlo()
        server.starttls()
        server.login(usr, pas)
        msg = MIMEMultipart()
        msg['Subject'] = "Hurray! SMTP WORKED"
        msg['From'] = usr
        msg['To'] = toaddr
        msg.add_header('Content-Type', 'text/html')
        data = f"""

        
        <h2 style="text-align:center"><!-- x-tinymce/html --></h2>

<h2 style="text-align:center">✔ SMTP Test Email&nbsp;✔</h2>

<p>This is a test email sent from your SMTP checker tool.&nbsp;</p>

<ul>
	<li><strong>SMTP Host:</strong>&nbsp;{HOST}</li>
	<li><strong>SMTP Port:</strong>&nbsp;{PORT}</li>
	<li><strong>Username:</strong>&nbsp;{usr}</li>
	<li><strong>Password:</strong>&nbsp;{pas}</li>
</ul>


        """
        msg.attach(MIMEText(data, 'html', 'utf-8'))
        server.sendmail(usr, [msg['To']], msg.as_string())
        print(f"{Fore.GREEN}[+]SMTP WORK {HOST}{Fore.RESET}")
        with open('validsmtp.txt', 'a') as f:
            f.write(smtp + "\n")
        VALIDS += 1
        title_update = "title [+] SMTP WORKED - VALIDS : {} , INVALIDS : {}".format(VALIDS, INVALIDS)
        os.system(title_update)
    except smtplib.SMTPException as e:
        INVALIDS += 1
        print(f"{Fore.RED}[-]SMTP NOT WORK {smtp}. Error: {e}{Fore.RESET}")


if __name__ == '__main__':
    try:
       

        smtp_file = input('\n\n ┌╼[Enter the path of the SMTP list file: ')
        with open(smtp_file, 'r') as sites:
            smtp_list = sites.readlines()

        print("[*] Checking SMTP servers...\n")
        start_time = time.time()

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(check, smtp_list)

        end_time = time.time()
        total_time = end_time - start_time

        print("\n[+] SMTP Check completed!")
        print(f"[+] Total SMTPs checked: {len(smtp_list)}")
        print(f"[+] Valid SMTPs found: {VALIDS}")
        print(f"[+] Invalid SMTPs found: {INVALIDS}")
        print(f"[+] Total time taken: {total_time:.2f} seconds")

        if VALIDS > 0:
            print("[+] Valid SMTPs are saved in validsmtp.txt file.")

        print("\n[+] Exiting...")

    except KeyboardInterrupt:
        print("\n[!] Script interrupted by user. Exiting immediately.")
        sys.exit(0)