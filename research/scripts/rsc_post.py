"""Extract the full post object from an Inspora post page's RSC (self.__next_f) payload."""
import json, re, sys

def extract_post(html):
    chunks = re.findall(r'self\.__next_f\.push\(\[1,(".*?")\]\)</script>', html, re.S)
    payload = ''.join(json.loads(c) for c in chunks)
    i = payload.find('"post":{')
    if i < 0:
        return None
    start = i + len('"post":')
    depth, j, ins, esc = 0, start, False, False
    while j < len(payload):
        ch = payload[j]
        if ins:
            if esc: esc = False
            elif ch == '\\': esc = True
            elif ch == '"': ins = False
        else:
            if ch == '"': ins = True
            elif ch == '{': depth += 1
            elif ch == '}':
                depth -= 1
                if depth == 0:
                    return json.loads(payload[start:j + 1])
        j += 1
    return None

if __name__ == '__main__':
    print(json.dumps(extract_post(open(sys.argv[1]).read()), indent=1))
