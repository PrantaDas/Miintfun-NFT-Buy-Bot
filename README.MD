## MINTFUN NFT minting Bot.

Mintfun Bot is a web3 nft minting bot that [https://mint.fun](https://mint.fun) mints the NFT from the reference website depending on multiple conditions. It basically trgets the Tokens that are on [Base](https://docs.base.org/) chain and the Tokens that are not reported by the community. The bot search for the lowest price and minimum minting quantity of the collection and after satisfying the conditions the complete the transaction and save the collection info with the transaction ID to prevent the duplication of minting process for the same collection.

When the requirements of the project was given to us we were instructed to automate the website for completing the minting process with selenium,that involves the browser automation and the Metamask automation. That seems quite difficult to us cause we never automated the Metamask before and the content of the website changes frquently as they are long polling in a REST API endpoint to update their latest collection. So we were searching for different apporaches. We were gathering information about [Mintfun](https://mint.fun) and came to know that their APIs is provided by [https://reservoir.tools/](https://reservoir.tools/) .So we started searching for minting option so that we can minimize the effort and time. Finally we got an REST API endpoint that allows us to initiate transactions.The all we need to provide the `contract` address,the `taker` (the receiver of the token) ,`quantity` and the `source` (mint.fun). After requesting we got a signed `Object` later that we used to `sendTransaction`.With this approach we were able to complete our first transaction in test net.But later on shifing on mainnet we were facing the `nonce` and `gassLimit` estimation issue. Because we are making multiple transactions in a row withing a `30 sec ` interval. After providing the  `nonce` and `gassLimit` parameters we were able to complete a successful transaction in mainnet. Within 40 sec we were able to mint 9 Tokens that is far better than automating the process.

### Table of Contents
- [Features](#features)
- [How it works](#how-it-works)
- [Installation](#installation)
- [Minimum Requirements](#minimum-requirements)
- [Technologies](#technologies)
- [Run Locally](#run-locally)
- [License](#license)

## Features:
* The bot starts only 2 days in a week through a scheduler.
* Target for the whietelisted NFTs.
* Purchase the NFTs that are free to mint or have the lowest cost with different quantity.
* Save the transaction into the DB for avoiding duplicate transactions.

### How it works
* The bot gathers collection information from a api `https://mint.fun/api/mintfun/feed/free?range=30m&chain=8453` provided by the `mintfun` with 30 seconds intervals.

* Then it filter outs the Blacklisted tokens from the collection and returns the rest of the data.
* Then we iterate over the collection and send it for further processing where we gather necessary information for completig the transactiona and the after successful processing we save the collection info in `DB`.

### Installation

1. Clonse the repository

```shell
git clone https://github.com/PrantaDas/mintfun-NFTBot.git
```
2. Change the directory

```shell
cd mintfun-bot
```

3. Provide all the env variables
```js
SDK_API_KEY = "your_reservior_api_key"
SDK_BASE_URL = "https://api-base.reservoir.tools"
RPC_URL = "your_rpc_url"
PRIVATE_KEY = "your_private_key"
WALLET_ADDRESS = "your_wallet_address"
INTERVAL = 'adjust_interval'
GASS_LIMIT = 'adjust_gass_limit'
MNEMONIC_PHRASE = "your_mnemonic_phrase"
MONGODB_URL = "your_mongodb_url"
SECRET_KEY = "your_secret_key"
MINT_FUN_BASE_URL = "https://mint.fun/api/mintfun/feed/free?range=30m&chain=8453"
TRANSACTION_INFO_BASE_URL = "https://mint.fun/api/mintfun/contract"
DAYS_TO_RUN = [1,4] //days to run adjust as you want
START_HOUR = 'start_hour in number'
START_MINUTE = 'start_minute in number'
```
4. Install all the dependencies
```shell
pip install -r requirements.txt
```

5. Start the bot
```shell
python src/app.py
```

### Minimum Requirements
* Python3
* Web3.py
* PIP

### Technologies
- [Python](https://www.python.org/)
- [Web3.py](https://web3py.readthedocs.io/en/stable/index.html)
- [Requests](https://pypi.org/project/requests/)

### Run locally (Start RPC Server)
```shell
ganache -f your_node_url -m "your_mnemonic_phrase"
```
Then run 

```shell
python src/app.py
```

### License
[MIT](https://github.com/PrantaDas/mintfun-NFTBot.git)