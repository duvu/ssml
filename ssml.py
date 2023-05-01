import re
import xml.etree.ElementTree as ET

# define a list of acronym and their expansions, to be used in the SSML tags sub
acronyms = {
    'UBND': 'Ủy ban nhân dân',
    'HĐND': 'Hội đồng nhân dân',
    'UB': 'Ủy ban',
    'HĐ': 'Hội đồng',
    'TP': 'Thành phố',
    'MTTQ': 'Mặt trận tổ quốc',
    'ĐBQH': 'Đại biểu quốc hội',
    'TW': 'Trung ương',
    'NHNN': 'Ngân hàng nhà nước',
    'TP.HCM': 'Thành phố Hồ Chí Minh',
    'TP HCM': 'Thành phố Hồ Chí Minh',
    'TPHCM': 'Thành phố Hồ Chí Minh',
    'TP. HCM': 'Thành phố Hồ Chí Minh',
}

def build_ssml(text):
    # Create the root element with the SSML namespace
    root = ET.Element('speak', xmlns='http://www.w3.org/2001/10/synthesis')

    # Split the text into sentences
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=[.?])\s', text)

    # Create a "say-as" element for each sentence
    for sentence in sentences:
        # Split the sentence into phrases using commas
        phrases = sentence.split(', ')
        # Create a "say-as" element for each phrase
        for i, phrase in enumerate(phrases):
            # Check if the phrase contains a date(ddMMyyyy) or time (hh:mm)
            if re.search(r'\d{1,2}/\d{1,2}/\d{2,4}|\d{1,2}:\d{2}(?:am|pm)?', phrase):
                say_as = ET.SubElement(root, 'say-as', {'interpret-as': 'date'})
            else:
                say_as = ET.SubElement(root, 'say-as', {'interpret-as': 'text'})
            say_as.text = phrase.strip()
            # Create a "break" element with a duration of 200ms after each phrase
            if phrase != phrases[-1]:
                pause = ET.SubElement(root, 'break', time='150ms')

        # Create a "break" element with a duration of 400ms after each sentence
        if sentence != sentences[-1]:
            pause = ET.SubElement(root, 'break', time='400ms')

        # Convert the ElementTree object to an XML string
    return ET.tostring(root, encoding='utf8', method='xml').decode('utf8')


if __name__ == '__main__':
    text = 'Theo tờ The Sun, Hải quân Hoàng gia Anh đã mở một cuộc điều tra về vụ sơ đồ của tàu ngầm HMS Anson trị giá 1.6 tỷ USD bị thất lạc nơi công cộng.'
    ssml = build_ssml(text)
    print(ssml)
