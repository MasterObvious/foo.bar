import base64

MESSAGE = '''
FkIeEA4GCBYeQk1fTUIKFwgEGUJBRUoGAgkBAAwCGABKRVdFSgAeEQgAAAAJQkFFSgALAwIXGRZK RVdFSgwDBh8ACQwPCQhCQUVKBA4NBAAbAAAAAxFKRVdFShADCQIGBgAJQkFFShcMBw8MGRZKRVdF ShYMAwhCQUVKAwIKSkVXRUoSBAtMQhA=
'''

KEY = 'me'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(ord(c) ^ ord(KEY[i % len(KEY)])))

print ''.join(result)
