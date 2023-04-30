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
        for phrase in phrases:
            # Check if the phrase contains a date(ddMMyyyy) or time (hh:mm)
            if re.search(r'\d{1,2}/\d{1,2}/\d{2,4}|\d{1,2}:\d{2}(?:am|pm)?', phrase):
                say_as = ET.SubElement(root, 'say-as', {'interpret-as': 'date'})
            else:
                # create a "say-as" element with the interpret-as attribute set to "text"
                say_as = ET.SubElement(root, 'say-as', interpret_as='text')
            say_as.text = phrase.strip()

            # Create a "break" element with a duration of 200ms after each phrase
            if phrase != phrases[-1]:
                pause = ET.SubElement(root, 'break', time='200ms')

            # Create a "break" element with a duration of 400ms after each sentence
            if sentence != sentences[-1]:
                pause = ET.SubElement(root, 'break', time='400ms')

        # Convert the ElementTree object to an XML string
    ssml_b = ET.tostring(root, encoding='utf8', method='xml')
    ssml_str = ssml_b.decode('utf8')
    return ssml_str


if __name__ == '__main__':
    text = 'Hello, my name is John. I was born on 12/12/1990. I live in New York City.'
    ssml = build_ssml(text)
    print(ssml)
