class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str += f"{len(word)}#{word}"
        return encoded_str

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            length = ""
            # Parse number
            while s[i] != "#":
                length += s[i]
                i+=1
            try:
                length = int(length)
            except:
                length = 0
            i+=1
            word = s[i:i+length]
            print(word)
            strs.append(word)
            i+=length 

        return strs