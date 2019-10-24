from google.cloud import vision

pics = ['https://i.imgur.com/2EUmDJO.jpg', 'https://i.imgur.com/FPMomNl.png']

client = vision.ImageAnnotatorClient()
image = vision.types.Image()

def vision_face_detection():
    result = ''
    for pic in pics:
        image.source.image_uri = pic
        response = client.face_detection(image=image)
        result += f'File: {pic}:</br>'
        for face in response.face_annotations:
            likelihood = vision.enums.Likelihood(face.surprise_likelihood)
            vertices = [f'({v.x},{v.y})' for v in face.bounding_poly.vertices]
            result += f'Face surprised: {likelihood.name}</br>'
            result += f'Face bounds: {",".join(vertices)}</br></br>'
    return result
