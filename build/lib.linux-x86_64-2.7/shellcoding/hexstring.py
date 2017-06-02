class HexString(object):
    def __init__(self, string, arch):
        self.string = string
        self.arch = arch
        self.blocks = self._split_data()
        self.data = [self._hex_gen(x) for x in self.blocks]
        print("[+] Generated assembly formatted-data for string '{0}'".format(self.string))
        print(self.data)

    def _split_data(self):
        """
        Split data to transform it into injectable hexadecimal data
        for little-endian systems.
        """
        data = self.string
        #  Define the architecture of CPU
        if self.arch == 32:
            y = 4
        elif self.arch == 64:
            y = 8
        else:
            return -1

        l = list()
        for x in range(0, len(data), y):
            if x+y < len(data):
                l.append(data[x:x+y][::-1])
            else:
                last_block = data[x:len(data)][::-1]
                last_block_len = len(last_block)
                diff_41 = y - last_block_len
                if diff_41 > 0:
                    last_block = last_block + ("A" * diff_41)
                l.append(last_block)
        return l[::-1]


    def _hex_gen(self, x):
        """
        Transforms a string into a hexadecimal representation
        """
        data_list = list(x)
        bs = [None] * len(data_list)
        fs = str()
        n = 0

        # Turn string into hex
        for char in data_list:
            bs[n] = hex(ord(char))
            n += 1

        fs += "0x"
        for x in bs:
            p = str(x).replace("0x", "")
            fs += p

        return fs
