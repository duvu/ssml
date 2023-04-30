import re
import xml.etree.ElementTree as ET


def build_ssml(text):
    # Create the root element with the SSML namespace
    root = ET.Element('speak', xmlns='http://www.w3.org/2001/10/synthesis')

    # Split the text into sentences
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=[.?])\s', text)

    ssml_str = ''
    # Create a "say-as" element for each sentence
    for sentence in sentences:
        # Split the sentence into phrases using commas
        phrases = sentence.split(',')

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
                pause = ET.SubElement(root, 'break', time='200ms')

        # Create a "break" element with a duration of 400ms after each sentence
        if sentence != sentences[-1]:
            pause = ET.SubElement(root, 'break', time='400ms')

        # Convert the ElementTree object to an XML string
    return ET.tostring(root, encoding='utf8', method='xml').decode('utf8')


if __name__ == '__main__':
    text = 'Trong đơn kiến nghị, Chủ tịch Tập đoàn đầu tư Địa ốc Nova (Novaland) Bùi Thành Nhơn cho biết tại Đồng Nai, các công ty thuộc Novaland là chủ đầu tư của 9 dự án. Đây là thành phần của Khu đô thị kinh tế mở Long Hưng (gồm khu dân cư Long Hưng, khu đô thị WaterFront, Aqua City) và dự án khu đô thị dịch vụ thương mại cao cấp cù lao Phước Hưng. Loạt dự án này đều thuộc phân khu C4, thành phố Biên Hòa, có nguồn gốc từ việc tách dự án hoặc Novaland nhận chuyển nhượng một phần dự án từ các chủ đầu tư cấp một.'
    ssml = build_ssml(text)
    print(ssml)
