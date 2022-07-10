from typing import List

input = """office, country, telephone
chicago, USA, +1 312 373 1000
Beijing, China, +86 4008 900 505
Bangalore, India, +91 80 4064 9570
"""


def acquireData(input):
    lines: List[str] = input.split("\n")
    firstLine = True
    result = []
    for line in lines:
        if firstLine:
            firstLine = False
            continue
        if line.strip() == "":
            continue
        record = line.split(',')
        if record[1].strip() == "India":
            result.append({
                'city': record[0].strip(),
                'phone': record[2].strip()
            })
    return result


def removeFirstLine(lines):
    return lines[1:]


def temp_acquireData(input):
    lines: List[str] = input.split("\n")
    lines = removeFirstLine(lines)
    lines = list(filter(lambda l: l.strip() != "", lines))
    records = list(map(lambda l: l.split(','), lines))
    india_records = list(filter(lambda record: record[1].strip() == 'India', records))
    result = list(map(lambda record: {"city": record[0].strip(), "phone": record[2].strip()}, india_records))
    return result

print(acquireData(input))
print(temp_acquireData(input))

assert acquireData(input) == temp_acquireData(input)
assert acquireData(input) is temp_acquireData(input)
