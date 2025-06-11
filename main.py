import os
import json
import time
import pyotp

CLEAR_COMMAND = "cls" if os.name == "nt" else "clear"

def clear():
    os.system(CLEAR_COMMAND)

def get_answer(question, choices=[]):
    formatted_choices = "\n- ".join(choices)
    while True:
        clear()
        answer = input(f"{question}\n\n> ")
        if len(choices) != 0 and answer not in choices:
            clear()
            print(f"Invalid answer, please try again. Only the following answers are avaliable:\n- {formatted_choices}")
            time.sleep(3)
            continue
        break
    return answer

def get_code(secret):
    totp = pyotp.TOTP(secret.replace(" ", "")) # Replace spaces with empty chars, just in case the user manually adds codes, which bypasses t
    return totp.now()

def read_id_file():
    return json.load(open("2fa_identifiers.json", "r"))

def write_id_file(new_dict):
    json.dump(new_dict, open("2fa_identifiers.json", "w"), indent=5)

def get_identifiers():
    ids = []
    secrets = []
    for i, s in read_id_file().items():
        ids.append(i)
        secrets.append(s)
    return ids, secrets

def Menu():
    option = get_answer("Options:\n1. Get 2FA Code\n2. Add Identifier\n3. Remove Identifier\n4. Exit", choices=["1", "2", "3", "4"])
    match option:
        case "1":
            while True:
                clear()
                otp_codes = []
                for identifier, secret in zip(get_identifiers()[0], get_identifiers()[1]):
                    otp_codes.append(f"{identifier} | {get_code(secret)}")
                option = get_answer(f"2FA Codes (Identifier | OTP Code):\n- {'\n- '.join(otp_codes)}\n\nOptions:\n1. Regenerate OTP Codes\n2. Go Back", ["1", "2"])
                if option == "1":
                    continue
                break
            Menu()
                    
        case "2":
            # Get unique ID
            while True:
                new_id = get_answer("What identifier do you want to use?")
                if new_id in get_identifiers()[0]:
                    clear()
                    print(f"Invalid answer, please try again. This Identifier already exits.")
                    time.sleep(3)
                    continue
                break
            # Get the user's auth code
            while True:
                twofa_key = get_answer("What's your 2FA Key for this identifier?")
                if not len(twofa_key) >= 32:
                    clear()
                    print(f"Invalid answer, please try again. This 2FA Key isn't 32 chars.")
                    time.sleep(3)
                    continue
                break
            
            # Add the new ID + 2fa Key to the ID json file
            id_dict = read_id_file()
            id_dict[new_id] = twofa_key
            write_id_file(id_dict)
            clear()
            print(f"Successfully added, \"{new_id}\", to the id list.")
            time.sleep(3)
            Menu()
        
        case "3":
            # Validate the ID exists
            while True:
                target_id = get_answer("What identifier do you want to remove?")
                if target_id not in get_identifiers()[0]:
                    clear()
                    print(f"Invalid answer, please try again. This Identifier doesn't exits.")
                    time.sleep(3)
                    continue
                break
            
            # Remove the ID from the ID json file
            id_dict = read_id_file()
            del id_dict[target_id]
            write_id_file(id_dict)
            clear()
            print(f"Successfully removed, \"{target_id}\", from the id list.")
            time.sleep(3)
            Menu()
        
        case "4":
            clear()
            os._exit(0)

if __name__ == "__main__":
    if not os.path.exists("2fa_identifiers.json"):
        json.dump({}, open("2fa_identifiers.json", "w"), indent=5)
    Menu()
