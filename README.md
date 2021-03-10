<img src="data/image2.jpg" width = 95% height = 25% >

# 🔹 Auto Medical Diagnosis 
🚨 _Created for InnovateNSUT 2021_
> An NLP based API to predict what ailments a person may be experiencing given how they are currently feeling.

## 🔸Overview
- This API is supposed to be of one of endpoints for [MedApp](https://med-app-nsut.netlify.app) in determining beforehand how a person is feeling and what are their symptoms without reading the whole description that the patient provides.

- `process` endpoint serves as a link to the original MedApp to provide ailments classified according to the query.
 

## 🔸Basis of Model
- This API is based on **NLP** and uses **Random Forest Classification**, behind the scenes, to classify a person's textual description into one of the many ailments present in the dataset. 

- This dataset is currently limited to the following ailments -
> Emotional pain, Hair falling out, Head hurts, Infected wound, Foot achne, Shoulder pain, Injury from sports, Skin issue, Stomach ache, Knee pain, Joint pain, Hard to breath, Head ache, Body feels weak, Feeling dizzy, Back pain, Open wounds, Internal pain, Blurry vision, Acne, Muscle pain, Neck pain, Cough, Ear ache, Feeling cold


## 🔸Query Structure 
- This API consists of one end point with the name **process** and two parameters `query` and `train`

 - **query** : This parameter is used to send the actual information to the API for processing and is of `string` type
    
- 🌟**train**🌟 : This is a quite different parameter for the API and its values denote whether to 🏋️ **train the model again at the end of processing or not** 

> train = 0 : No training is done when 0 
            
> train = 1 : Training is done when 1

- This API returns a list of top three matching ailments which would be classified according to the query parameter you provided.

## 🔸Query Example 
- Passing the `query="I have been feeling sad and dejected for quite some time now "` results in the model returning the following list of ailments - 
            - **`["emotional pain","feeling dizzy","body feels weak"]`**
- Try for [yourself!](https://medical-nlp.herokuapp.com/process?query=%22i%20have%20been%20feeling%20sad%20and%20dejected%20for%20quite%20some%20time%20now%22&train=0)

## Additions 🚧
- This model is currently reliant on *~ 800 data points* and thus would not be very rich in terms vocabulary. This problem would be overcome as the model is populated with more data overtime

- Another feature that we look to implement is *automatic training calls* to our API. Currently `train` parameter is a *manual* parameter which we need to pass to train our model at the server. We aim to make this automated in the future.

## Team Repositories and App
- The main application is hosted at [MedApp](https://med-app-nsut.netlify.app)
- If you want to see the frontend repository go at [Front End - MedApp](https://github.com/VatD/MedApp)
- For the backend repository go to [Back End - MedApp](https://github.com/Abhishek-7139/MedAppAPI)
- For usage document go to the following [Document](https://drive.google.com/file/d/1vHvobvnBGQDlPTc-K89k81ZHIavu370_/view) 
