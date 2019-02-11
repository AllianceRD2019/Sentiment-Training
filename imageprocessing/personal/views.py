from django.shortcuts import render
from django.conf import settings
import math

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from personal.models import Document
from personal.forms import DocumentForm

import json
# from watson_developer_cloud import CompareAndComplyV1

from django.conf import settings
from zipfile import *

import zipfile
import sys
import os ,shutil
from django.core.files import File

import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
import Features, EntitiesOptions, KeywordsOptions ,SentimentOptions ,CategoriesOptions , ConceptsOptions ,MetadataOptions
from watson_developer_cloud import DiscoveryV1




############################ Discovery Credentials ################################################################################################


discovery = DiscoveryV1(
    version='2018-12-03',
    iam_apikey='ncluLlhb8DTi23hb52iIP3UeZHnco3QroCmeWUvxAJvG',
    url='https://gateway.watsonplatform.net/discovery/api'
)
############################ Discovery Credentials ################################################################################################

############################ NLU Credentials ######################################################################################################
naturalLanguageUnderstanding = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    iam_apikey='5ghRvFGuoW0H1TyBf8ME4HKVR_rJ4osTbBcnH73FH3Qe',
    url='https://gateway.watsonplatform.net/natural-language-understanding/api')
############################ NLU Credentials ######################################################################################################

collection_id='87c5ac7e-27fd-4805-a06e-de2563be793a',
config_id='3f2a7f68-5746-40aa-9368-025eb5714220',
env_id='79457914-e36a-4e70-be50-9be661c665d3'


############################ Discovery  ######################################################################################################

def home(request):
    return render (request, 'personal/home.html')

#environments
def environments(request):

    return render (request, 'personal/home.html')


def add_env(request):
    response = discovery.create_environment(name="New environment",description="My environment").get_result()
    print(json.dumps(response, indent=2))


    envID=response['environment_id']
            
    print (envID)

    return render (request, 'personal/home.html')

#configurations

def add_config(request):
    with open(os.path.join(os.getcwd(), 'personal/config.json')) as config_data:
        data = json.load(config_data)
        new_config = discovery.create_configuration(env_id, data['name'], data['description'], data['conversions'], data['enrichments'], data['normalizations']).get_result()
        print(json.dumps(new_config, indent=2))
    return render (request, 'personal/home.html')


#collection

def add_collection(request):
    new_collection = discovery.create_collection(environment_id='11a03822-2233-4000-a2dd-111eda210637', configuration_id='3242600e-7cc3-4129-b848-4ef0064a8725', name='Sample Collection', description='Sample Collection ').get_result()
    print(json.dumps(new_collection, indent=2))
    return render (request, 'personal/home.html')


def list_collection(request):
    collections = discovery.list_collections('11a03822-2233-4000-a2dd-111eda210637').get_result()
    print(json.dumps(collections, indent=2))
    return render (request, 'personal/home.html')

def update_collection(request):
    updated_collection = discovery.update_collection(environment_id='11a03822-2233-4000-a2dd-111eda210637', collection_id='09a43b2b-6e5e-4cb1-a0c4-db9623119c1a', configuration_id='3242600e-7cc3-4129-b848-4ef0064a8725', name='updated collection', description='update collection').get_result()
    print(json.dumps(updated_collection, indent=2))
    return render (request , 'personal/home.html')

def delete_collection(request):                            #environment_id                              #collection_id
    delete_collection = discovery.delete_collection('11a03822-2233-4000-a2dd-111eda210637', '09a43b2b-6e5e-4cb1-a0c4-db9623119c1a').get_result()
    print(json.dumps(delete_collection, indent=2))
    return render (request , 'personal/home.html')

def list_collection(request):                            #environment_id                              #collection_id
    collection_fields = discovery.list_collection_fields('11a03822-2233-4000-a2dd-111eda210637', '09a43b2b-6e5e-4cb1-a0c4-db9623119c1a').get_result()
    print(json.dumps(collection_fields, indent=2))
    return render (request , 'personal/home.html')

#document

def add_document(request):

    filePath = os.path.join(r'C:\Users\Owner\Desktop\Research and development\ADS\imageprocessing\media\data\file.pdf')
    filed  = open(filePath , 'rb')
    
                                              #environment_id                              #collection_id
    add_doc = discovery.add_document('11a03822-2233-4000-a2dd-111eda210637', '09a43b2b-6e5e-4cb1-a0c4-db9623119c1a', file=filed).get_result()
    print(json.dumps(add_doc, indent=2))
    return render (request , 'personal/home.html')

def get_document(request):                            #environment_id                              #collection_id                             #collection_id
    doc_info = discovery.get_document_status('11a03822-2233-4000-a2dd-111eda210637', '09a43b2b-6e5e-4cb1-a0c4-db9623119c1a', '2c82c910-307e-475a-9288-4a46a1b06398').get_result()
    print(json.dumps(doc_info, indent=2))
    return render (request , 'personal/home.html')

def update_document(request):  
    filePath = os.path.join(r'C:\Users\Owner\Desktop\Research and development\ADS\imageprocessing\media\data\update.pdf')
    filed  = open(filePath , 'rb')
                                              #environment_id                              #collection_id                       #document ID
    add_doc = discovery.update_document('11a03822-2233-4000-a2dd-111eda210637', '09a43b2b-6e5e-4cb1-a0c4-db9623119c1a', '2c82c910-307e-475a-9288-4a46a1b06398', file=filed).get_result()
    print(json.dumps(add_doc, indent=2))
    return render (request , 'personal/home.html')


def delete_document(request):  
                                              #environment_id                              #collection_id                       #document ID
    delete_doc = discovery.delete_document('11a03822-2233-4000-a2dd-111eda210637', '09a43b2b-6e5e-4cb1-a0c4-db9623119c1a', '2c82c910-307e-475a-9288-4a46a1b06398') .get_result()
    print(json.dumps(delete_doc, indent=2))
    return render (request , 'personal/home.html')


#training




############################ discovery  ######################################################################################################


############################ NLU  ######################################################################################################

def nlu(request):
    vPos=Document.objects.order_by('uploaded_at')
    form=DocumentForm()
    return render(request, 'personal/nlu.html', { 'Pos':vPos ,'form':form })


def dataset(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            vFormTemporal = form.save(commit=False)
            label , score , category, conText ,conRel ,conSource, entityText ,entityType ,mdTitle, mdDate = interface(request.POST['url'])           
            vFormTemporal.label=label
            vFormTemporal.score=score
            vFormTemporal.catLabel=category
            vFormTemporal.conText=conText
            vFormTemporal.conRel=conRel
            vFormTemporal.conSource=conSource
            vFormTemporal.entityText=entityText
            vFormTemporal.entityType=entityType
            vFormTemporal.mdTitle=mdTitle
            vFormTemporal.mdDate=mdDate
            vFormTemporal.save()
            return redirect ('nlu')
    else:
        form = DocumentForm
        return render (request, 'personal/success.html',{
            'form' : form
        })

def interface(Purl ):
    response = naturalLanguageUnderstanding.analyze(
    url=Purl,
    features=Features(sentiment=SentimentOptions(),
    categories=CategoriesOptions(limit=1),
    concepts=ConceptsOptions(limit=1),
    entities=EntitiesOptions(limit=1),
    metadata=MetadataOptions()
    )).get_result()
    result=json.dumps(response, indent=2)
    
#Sentiment
    vLabel =response['sentiment']['document']['label']
    score =response['sentiment']['document']['score']
    
    mdTitle= response['metadata']['title']
    mdDate = response['metadata']['publication_date']
    vScore= math.ceil (float(score) * 100)

#category 
    try:
        for category in response['categories']:
            categoryLabel = category['label']

        for concept in response['concepts']:
            conceptText = concept['text']
            conceptRelevance = str(concept['relevance'])
            conceptSource = concept['dbpedia_resource']

        for entity in response['entities']:
                entityText= entity['text']
                entityType = entity['type']

                

    except:
            vScore = "ERROR"
            vLabel = "ERROR"
            categoryLabel = "ERROR"
            conceptText = "ERROR"
            conceptRelevance = "ERROR"
            conceptSource = "ERROR"
            entityText = "ERROR"
            entityType = "ERROR"
            mdTitle = "ERROR"
            mdDate = "ERROR"

    print (response)
  

    return vLabel, vScore ,categoryLabel, conceptText, conceptRelevance, conceptSource ,entityText ,entityType ,mdTitle ,mdDate

############################NLU######################################################################################################
    
    
def charts(request):
      
    return render(request, 'personal/charts.html')



        






    
    
    

    





















