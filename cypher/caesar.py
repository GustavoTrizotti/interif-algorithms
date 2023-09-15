from string import ascii_letters

def encrypt(input_string: str, key: int, alphabet: str | None = None) -> str:
    alpha = alphabet or ascii_letters
    result = ""
    for character in input_string:
        if character not in alpha:
            result += character
        else:
            new_key = (alpha.index(character) + key) % len(alpha)
            result += alpha[new_key]
    return result

def decrypt(input_string: str, key: int, alphabet: str | None = None) -> str:
    key *= -1
    return encrypt(input_string, key, alphabet)

def brute_force(input_string: str, key: int, alphabet: str | None = None) -> dict[int, str]:
    alpha = alphabet or ascii_letters
    brute_force_data = {}
    for key in range(1, len(alpha) + 1):
        brute_force_data[key] = decrypt(input_string, key, alpha)
    return brute_force_data

s = "Texto secreto"
sEncrypt = encrypt(s, 13)
sDecrypt = decrypt(sEncrypt, 13)
sBruteForce = brute_force(sEncrypt, 13)

print(sEncrypt + "\n" + sDecrypt)
print(sBruteForce)

# >>> grKGB FrpErGB
#     Texto secreto
'''
    {1: 'fqJFA EqoDqFA', 2: 'epIEz DpnCpEz', 3: 'doHDy ComBoDy', 4: 'cnGCx BnlAnCx', 5: 'bmFBw AmkzmBw', 6: 'alEAv zljylAv', 7: 'ZkDzu ykixkzu', 8: 'YjCyt xjhwjyt', 9: 'XiBxs wigvixs', 10: 'WhAwr vhfuhwr', 11: 'Vgzvq ugetgvq', 12: 'Ufyup tfdsfup', 13: 'Texto secreto', 14: 'Sdwsn rdbqdsn', 15: 'Rcvrm qcapcrm', 16: 'Qbuql pbZobql', 17: 'Patpk oaYnapk', 18: 'OZsoj nZXmZoj', 19: 'NYrni mYWlYni', 20: 'MXqmh lXVkXmh', 21: 'LWplg kWUjWlg', 22: 'KVokf jVTiVkf', 23: 'JUnje iUShUje', 24: 'ITmid hTRgTid', 25: 'HSlhc gSQfShc', 26: 'GRkgb fRPeRgb', 27: 'FQjfa eQOdQfa', 28: 'EPieZ dPNcPeZ', 29: 'DOhdY cOMbOdY', 30: 'CNgcX bNLaNcX', 31: 'BMfbW aMKZMbW', 32: 'ALeaV ZLJYLaV', 33: 'zKdZU YKIXKZU', 34: 'yJcYT XJHWJYT', 35: 'xIbXS WIGVIXS', 36: 'wHaWR VHFUHWR', 37: 'vGZVQ UGETGVQ', 38: 'uFYUP TFDSFUP', 39: 'tEXTO SECRETO', 40: 'sDWSN RDBQDSN', 41: 'rCVRM QCAPCRM', 42: 'qBUQL PBzOBQL', 43: 'pATPK OAyNAPK', 44: 'ozSOJ NzxMzOJ', 45: 'nyRNI MywLyNI', 46: 'mxQMH LxvKxMH', 47: 'lwPLG KwuJwLG', 48: 'kvOKF JvtIvKF', 49: 'juNJE IusHuJE', 50: 'itMID HtrGtID', 51: 'hsLHC GsqFsHC', 52: 'grKGB FrpErGB'}
'''