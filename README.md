<img src="data/image2.jpg" width = 700 height = 300>

# backend-MedApp 
> An NLP based API to predict what ailments a person is experiencing given how they are currently feeling.

## Overview
- This API is supposed to be a helper to the day to day doctor in determining beforehand how a person is feeling and what are their symptoms without reading the whole description that the patient provides.
- This shall save time and effort on the side of the doctor and let them focus more on preparing in the directions of the *ailments predicted*
- `process` endpoint serves as a link to the original MedApp to provide ailments classified according to the query.

## Basis of Model
- This API is based on **NLP** and uses **Random Forest Classification**, behind the scenes, to classify a person's textual description into one of the many ailments present in the dataset. 
- This dataset is currently limited to the following ailments -
> Emotional pain, Hair falling out, Head hurts, Infected wound, Foot achne, Shoulder pain, Injury from sports, Skin issue, Stomach ache, Knee pain, Joint pain, Hard to breath, Head ache, Body feels weak, Feeling dizzy, Back pain, Open wounds, Internal pain, Blurry vision, Acne, Muscle pain, Neck pain, Cough, Ear ache, Feeling cold

- 
## Query Structure 
- This API consists of one end point with the name **process** and two parameters `query` and `train`

    - **query** : This parameter is used to send the actual information to the API for processing and is of `string` type
    
    - **train** : This is a quite different parameter for the API and its values denote whether to **train the model again at the end of processing or not** 🏋️

> train = 0 : No training is done when 0 
>
                 
> train = 1 : Training is done when 1
