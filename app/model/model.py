

from doctr.io import DocumentFile
from doctr.models import ocr_predictor
__version__ = "0.1.0"

model = ocr_predictor(pretrained=True)



def process_image(image_path):
    document = DocumentFile.from_images(image_path)
    result = model(document)
    json_response = result.export()
    return json_response

def convert_to_lines(ocr_data):
    lines = []
    for page in ocr_data['pages']:
        for block in page['blocks']:
            for line in block['lines']:
                line_text = " ".join(f"{word['value']} (Confidence: {word['confidence']})" for word in line['words'])
                lines.append(line_text)
    return lines