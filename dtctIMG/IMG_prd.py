from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='6560ad9e6b72492a9a3855faa7c307a9')
model = app.public_models.general_model


response = model.predict_by_filename('IMG/face_yan.jpg')
for i in response["outputs"][0]['data']["concepts"]:
    #print(i)
    print("Объект: ",i["name"])
