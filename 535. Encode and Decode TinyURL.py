class Codec:
    def __init__(self):
        self.res = []

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.res.append(longUrl)
        return 'http://tinyurl.com/' + str(len(self.res) - 1)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.res[int(shortUrl.split('/')[-1])]


if __name__ == '__main__':
    codec = Codec()
    url = 'https://leetcode.com/problems/design-tinyurl'
    res = codec.decode(codec.encode(url))
    print(res)
