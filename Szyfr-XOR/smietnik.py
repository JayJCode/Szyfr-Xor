# def cryptoanalysis(self) -> None:
#     with open('crypto.txt', 'r', encoding='utf-8') as f:
#         crypto_text = f.readlines()
#     self.utils.write("decrypt.txt", "")
#     array_of_results = [[ '_' for _ in range(self.line_length)] for _ in range(len(crypto_text))]
#
#     for line_index in range(len(crypto_text)-2):
#         for index in range(0, (self.line_length-1)*8, 8):
#             m1 = crypto_text[line_index][index:index + 8]
#             m2 = crypto_text[line_index +1][index:index + 8]
#             m3 = crypto_text[line_index + 2][index:index + 8]
#             if self.m1_xor_m2(m1, m2)[0:3] == '010':
#                 if m3:
#                     if self.m1_xor_m2(m2, m3)[0:3] == '010':
#                         if self.m1_xor_m2(m1, m3) == '00000000':
#                             # m1 i m3 sa spacjami
#                             # m2 jest mala litera obliczona z m1 xor m2 xor spacja
#                             array_of_results[line_index][index//8] = ' '
#                             array_of_results[line_index+2][index//8] = ' '
#                             array_of_results[line_index+1][index//8] = chr(int(self.m1_xor_m2(self.m1_xor_m2(m1, m2), self.space), 2))
#                         else:
#                             # m2 jest spacja
#                             # m1 i m3 sa mala litera obliczona z m1 | m3 xor m2 xor spacja
#                             array_of_results[line_index+1][index//8] = ' '
#                             array_of_results[line_index][index//8] = chr(int(self.m1_xor_m2(self.m1_xor_m2(m1, m2), self.space), 2))
#                             array_of_results[line_index+2][index//8] = chr(int(self.m1_xor_m2(self.m1_xor_m2(m2, m3), self.space), 2))
#                     else:
#                         # m1 jest spacja
#                         array_of_results[line_index][index//8] = ' '
#                 else:
#                     # m3 jest puste
#                     array_of_results[line_index+2][index//8] = ''
#
#
#     result = "\n".join("".join(line) for line in array_of_results)
#     self.utils.write("decrypt.txt", result)
#     self.check_correctness()


def cryptoanalysis(self) -> None:
    crypto = self.utils.read("crypto.txt")

    self.utils.write("decrypt.txt", "")
    array_of_results = [['_' for _ in range(self.line_length)] for _ in range(len(crypto_text))]

    for index in range(0, (self.line_length - 1) * 8, 8):
        self.value_check(crypto_text, array_of_results, 0, index)

    for line in array_of_results:
        for i in range(len(line)):
            if line[i] == 'K':
                line[i] = '_'
            elif line[i] == 'W':
                line[i] = '_'
            elif line[i] == 'L':
                line[i] = '_'

    result = "\n".join("".join(line) for line in array_of_results)
    self.utils.write("decrypt.txt", result)
    self.check_correctness()

    # def value_check(self, crypto_text, array_of_results, line_index, index) -> None:
    #     if line_index >= len(crypto_text) - 2:
    #         return None
    #     m1 = crypto_text[line_index][index:index + 8]
    #     m2 = crypto_text[line_index + 1][index:index + 8]
    #     if self.m1_xor_m2(m1, m2) == '00000000':
    #         # value2 = value1
    #         if ' ' == array_of_results[line_index][index // 8]:
    #             array_of_results[line_index + 1][index // 8] = ' '
    #         elif 'W' == array_of_results[line_index][index // 8]:
    #             array_of_results[line_index + 1][index // 8] = 'W'
    #         elif 'L' == array_of_results[line_index][index // 8]:
    #             array_of_results[line_index + 1][index // 8] = 'L'
    #         else:
    #             array_of_results[line_index][index // 8] = 'K'
    #             array_of_results[line_index + 1][index // 8] = 'K'
    #     elif self.m1_xor_m2(m1, m2)[0:3] == '000':
    #         # litera x2
    #         if 'K' == array_of_results[line_index][index // 8]:
    #             i = line_index
    #             while i >= 0 and array_of_results[i][index // 8] == 'K':
    #                 array_of_results[i - 1][index // 8] = 'L'
    #                 i -= 1
    #         if 'W' == array_of_results[line_index][index // 8]:
    #             array_of_results[line_index - 1][index // 8] = ' '
    #             m2_char = chr(int(self.m1_xor_m2(self.m1_xor_m2(crypto_text[line_index - 1][index:index + 8],
    #                                                             crypto_text[line_index][index:index + 8]),
    #                                              self.space), 2))
    #             array_of_results[line_index][index // 8] = m2_char
    #             m3_char = chr(int(self.m1_xor_m2(self.m1_xor_m2(crypto_text[line_index - 1][index:index + 8],
    #                                                             crypto_text[line_index + 1][index:index + 8]),
    #                                              self.space), 2))
    #             array_of_results[line_index + 1][index // 8] = m3_char
    #         else:
    #             array_of_results[line_index][index // 8] = 'L'
    #             array_of_results[line_index + 1][index // 8] = 'L'
    #     elif self.m1_xor_m2(m1, m2)[0:3] == '010':
    #         # value2 | value1 => spacja | litera
    #         if ' ' == array_of_results[line_index][index // 8]:
    #             array_of_results[line_index + 1][index // 8] = 'L'
    #         elif 'L' == array_of_results[line_index][index // 8]:
    #             array_of_results[line_index + 1][index // 8] = ' '
    #         elif 'K' == array_of_results[line_index][index // 8]:
    #             i = line_index
    #             while i >= 0 and array_of_results[i][index // 8] == 'K':
    #                 array_of_results[i - 1][index // 8] = 'W'
    #                 i -= 1
    #         else:
    #             array_of_results[line_index][index // 8] = 'W'
    #             array_of_results[line_index + 1][index // 8] = 'W'
    #     self.value_check(crypto_text, array_of_results, line_index + 1, index)

    def value_check(self, crypto_text, array_of_results, line_index, index) -> None:
        if line_index >= len(crypto_text) - 2:
            return None
        m1 = crypto_text[line_index][index:index + 8]
        m2 = crypto_text[line_index + 1][index:index + 8]
        if m1_xor_m2(m1, m2) == '00000000':
            # value2 = value1
            array_of_results[line_index][index//8]='K'
            array_of_results[line_index+1][index//8]='K'
            if ' ' == array_of_results[line_index][index//8]:
                array_of_results[line_index+1][index//8]=' '
            elif 'W' == array_of_results[line_index][index//8]:
                array_of_results[line_index+1][index//8]='W'
            elif 'L' == array_of_results[line_index][index//8]:
                array_of_results[line_index+1][index//8]='L'
        elif m1_xor_m2(m1, m2)[0:3] == '000':
            # litera x2
            if 'K' == array_of_results[line_index][index//8]:
                array_of_results[line_index-1][index//8]='L'
            if 'W' == array_of_results[line_index][index//8]:
                array_of_results[line_index-1][index//8]=' '
                m2_char = chr(int(m1_xor_m2(
                    m1_xor_m2(crypto_text[line_index - 1][index:index + 8], crypto_text[line_index][index:index + 8]), self.space), 2))
                array_of_results[line_index][index // 8]=m2_char
                m3_char = chr(int(m1_xor_m2(m1_xor_m2(crypto_text[line_index - 1][index:index + 8], crypto_text[line_index + 1][index:index + 8]), self.space), 2))
                array_of_results[line_index+1][index // 8]=m3_char
            else:
                array_of_results[line_index][index//8]='L'
                array_of_results[line_index+1][index//8]='L'
        elif m1_xor_m2(m1, m2)[0:3] == '010':
            # value2 | value1 => spacja | litera
            array_of_results[line_index][index // 8]='W'
            array_of_results[line_index + 1][index // 8]='W'
            if ' ' == array_of_results[line_index][index // 8]:
                array_of_results[line_index+1][index // 8]='L'
            elif 'L' == array_of_results[line_index][index // 8]:
                array_of_results[line_index+1][index // 8]=' '
        self.value_check(crypto_text, array_of_results, line_index + 1, index)