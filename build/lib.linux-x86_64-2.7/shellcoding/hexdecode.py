#!/usr/bin/env python

class HexDecode(object):
    def __init__(self, data):
        self.data = self._format_data(data)

    @staticmethod
    def _format_data(data):
        data = data.replace("0x", "")
        return data

    def _convert(self):
        hex_out = list()
        for i in range(0, len(self.data), 2):
            hex_out.append(int(self.data[i: i+2], 16))
        return ''.join([chr(x) for x in hex_out])[::-1]


