class Codec:
    codeDB, urlDB = defaultdict(), defaultdict()
    chars = string.ascii_letters + string.digits

    def getCode(self) -> str:
        code = ''.join(random.choice(self.chars) for i in range(6))
        return "http://tinyurl.com/" + code

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.urlDB: return self.urlDB[longUrl]
        code = self.getCode()
        while code in self.codeDB: code = getCode()
        self.codeDB[code] = longUrl
        self.urlDB[longUrl] = code
        return code
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.codeDB[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))