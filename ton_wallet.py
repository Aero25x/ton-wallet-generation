import tqdm
from tonsdk.contract.wallet import Wallets, WalletVersionEnum

# Function to create wallets and save to file
def generate_wallets(count):
    output = ""
    for i in tqdm.tqdm(range(count), desc="Generating wallets"):
        mnemonics, pub_k, priv_k, wallet = Wallets.create(WalletVersionEnum.v4r2, workchain=0)
        wallet_address = wallet.address.to_string(True, True, False)
        
        output += "\n\n" + wallet_address + "\n" + ' '.join(mnemonics) + "\n"
    
    with open("wallets.txt", "a") as f:
        f.write(output)


# Main script
if __name__ == "__main__":
    print("""
          

  _    _ _     _     _             _____          _      
 | |  | (_)   | |   | |           / ____|        | |     
 | |__| |_  __| | __| | ___ _ __ | |     ___   __| | ___ 
 |  __  | |/ _` |/ _` |/ _ \ '_ \| |    / _ \ / _` |/ _ \\
 | |  | | | (_| | (_| |  __/ | | | |___| (_) | (_| |  __/
 |_|  |_|_|\__,_|\__,_|\___|_| |_|\_____\___/ \__,_|\___|
                                                         
                       by Aero25x                                           
          
          """)
    count = input("Enter the number of wallets to generate: ")
    try:
        count = int(count)
        generate_wallets(count)
    except ValueError:
        print("Please enter a valid number.")

