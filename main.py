import tls_client, os, threading, itertools, time, json, httpx


class Joiner:
    def __init__(self) -> None:
        self.getCookies()
        self.client = tls_client.Session(client_identifier="chrome_107",ja3_string="771,4866-4867-4865-49196-49200-49195-49199-52393-52392-159-158-52394-49327-49325-49326-49324-49188-49192-49187-49191-49162-49172-49161-49171-49315-49311-49314-49310-107-103-57-51-157-156-49313-49309-49312-49308-61-60-53-47-255,0-11-10-35-16-22-23-13-43-45-51-21,29-23-30-25-24,0-1-2",h2_settings={"HEADER_TABLE_SIZE": 65536,"MAX_CONCURRENT_STREAMS": 1000,"INITIAL_WINDOW_SIZE": 6291456,"MAX_HEADER_LIST_SIZE": 262144},h2_settings_order=["HEADER_TABLE_SIZE","MAX_CONCURRENT_STREAMS","INITIAL_WINDOW_SIZE","MAX_HEADER_LIST_SIZE"],supported_signature_algorithms=["ECDSAWithP256AndSHA256","PSSWithSHA256","PKCS1WithSHA256","ECDSAWithP384AndSHA384","PSSWithSHA384","PKCS1WithSHA384","PSSWithSHA512","PKCS1WithSHA512",],supported_versions=["GREASE", "1.3", "1.2"],key_share_curves=["GREASE", "X25519"],cert_compression_algo="brotli",pseudo_header_order=[":method",":authority",":scheme",":path"],connection_flow=15663105,header_order=["accept","user-agent","accept-encoding","accept-language"])

    def getCookies(self, session=None):
        headers = {
            "accept": "*/*",
            # "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.5",
            "connection": "keep-alive",
            "host": "canary.discord.com",
            "referer": "https://canary.discord.com/",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
            "x-context-properties": "eyJsb2NhdGlvbiI6IkFjY2VwdCBJbnZpdGUgUGFnZSJ9",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyLUZSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA3LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE1NDc1MCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=",
        }
        response = httpx.get(
            "https://canary.discord.com/api/v9/experiments", headers=headers
        )
        self.dcfduid = response.cookies.get('__dcfduid')
        self.sdcfduid = response.cookies.get('__sdcfduid')
        self.cfruid = response.cookies.get('__cfruid')
        self.fingerp = response.json()["fingerprint"]


    def join(self, token, invite, bypass):
        headers = {
            'authority': 'discord.com',
            'accept': '*/*',
            'accept-language': 'fr-FR,fr;q=0.9',
            'authorization': token,
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'cookie': f'__dcfduid={self.dcfduid}; __sdcfduid={self.sdcfduid}; __cfruid={self.cfruid}; locale=en-US',
            'origin': 'https://discord.com',
            'pragma': 'no-cache',
            'referer': 'https://discord.com/channels/@me',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyLUZSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA3LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE1NDc1MCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
        }
        r = self.client.post(f'https://discord.com/api/v9/invites/{invite}', headers=headers, json={})
        if r.status_code == 200:
            print(f"(+) Joined [{invite}] - [200]")
            if bypass == True:
                self.bypassRules(token, invite, r.json()["guild"]["id"])
        elif r.status_code == 429:
            print(f"(-) RATELIMIT BY CLOUDFLARE")
            time.sleep(3)
        else:
            print(f"(-) Error [{r.status_code}]")
            
            
    def bypassRules(self, token, invcode, guildid):
        headers = {
            'authority': 'discord.com',
            'accept': '*/*',
            'accept-language': 'fr-FR,fr;q=0.9',
            'authorization': token,
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'cookie': f'__dcfduid={self.dcfduid}; __sdcfduid={self.sdcfduid}; __cfruid={self.cfruid}; locale=en-US',
            'origin': 'https://discord.com',
            'pragma': 'no-cache',
            'referer': 'https://discord.com/channels/@me',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyLUZSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA3LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE1NDc1MCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
        }
        rulereq = self.client.get(f"https://discord.com/api/v9/guilds/{guildid}/member-verification?with_guild=false&invite_code={invcode}", headers=headers).json()

        submitpayload = json.loads(rulereq)
        submitpayload["form_fields"]["response"] = True
        submitpayload = json.dumps(submitpayload)
        res = self.client.put(f"https://discord.com/api/v9/guilds/{guildid}/requests/@me", headers=headers, json=submitpayload)
        print(f"{res.status_code}")
        
        
                
    def joiner(self):
        os.system("cls")
        with open("tokens.txt", 'r')as f:
            length = len(f.readlines())
        tok = itertools.cycle(open('tokens.txt', 'r+').read().splitlines())
        inv = input("(?) Invite CODE > ")
        WAIT_AMT = int(input("(?) Join Delay > "))
        bypass = input("(?) Bypass Rules (y/N) > ")
        if bypass.lower() == "y":
            bypass = True
        else: 
            bypass = False
        print()
        do = 0
        for token in tok:
            do = do + 1
            time.sleep(WAIT_AMT)
            threading.Thread(target=self.join, args=[token, inv, bypass]).start()
            if do == int(length):
                break
        
        
if __name__ == "__main__":    
    Joiner().joiner()
