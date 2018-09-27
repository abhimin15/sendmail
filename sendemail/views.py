from django.shortcuts import render_to_response
from django.conf import settings
import os
from django.core.mail import send_mail
import pandas as pd
from glob import glob
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
filepath = os.path.join(BASE_DIR, 'csvs/quiz1.csv')
file1 = pd.read_csv(filepath,index_col='Email Address')
file1 = file1[['Score']]

filepath = os.path.join(BASE_DIR, 'csvs/quiz2.csv')
file2 = pd.read_csv(filepath,index_col='Email Address')
file2 = file2[['Score']]

filepath = os.path.join(BASE_DIR, 'csvs/quiz3.csv')
file3 = pd.read_csv(filepath,index_col='Email Address')
file3 = file3[['Score']]

filepath = os.path.join(BASE_DIR, 'csvs/quiz4.csv')
file4 = pd.read_csv(filepath,index_col='Email Address')
file4 = file4[['Score']]

files1 = pd.merge(file1,file2,how='outer',on='Email Address')

files2 = pd.merge(file3,file4,how='outer',on='Email Address')

files = pd.merge(files1,files2,how='outer',on='Email Address')
files = files.fillna('0')
files.columns = ['day1','day2','day3','day4']
files['day1'] = files['day1'].apply(lambda x :eval(str(x)))
files['day2'] = files['day2'].apply(lambda x :eval(x))
files['day3'] = files['day3'].apply(lambda x :eval(x))
files['day4'] = files['day4'].apply(lambda x :eval(str(x)))

files['mean'] = files.sum(axis=1)
files = files[['day1','day2','day3','day4','mean']].sort_values('mean')
files.to_csv('quiz_results.csv')

def index(request):
    return render_to_response('index.html',{})

def sendmail(request):
    for i in range(length):
        participants(request,file['Email Address'][i],file['Score'][i])
        print('ok')
    return render_to_response('thanks.html',{})

def participants(request,email,number):
    subject = 'Online Quiz Result Day 4'
    body = '''Thanks for participating in the online quiz of Minovation.
Your score in the quiz is '''+str(number)+''' .
Keep visiting our website for information about other events.Thanks for participating in the quizzes

Regards,
Team Minovation 2018
IITBHU, Varanasi
'''


    from_email = settings.EMAIL_HOST_USER
    to_email = [email, ]
    send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=body, fail_silently=False)

def submission(request,email):
    subject = 'ABSTRACT SUBMISSION MINOVATION'
    body = '''Greetings From Minovation,
This mail is just a general reminder, if you have registered for the events Paper Presentation, Intrigue, and Innotech. The mentioned events required a submission of abstract so kindly send the corresponding abstracts of each event as early as possible. The deadline for the submission is 25th of September. For more details about the events visit our website minovation.in . Problem statement of Intrigue/Case Studies is available at https://drive.google.com/file/d/1R-Io-6GPg6gAYRm-uz7BGBAQhEHGLoxW/view.
Thank you
Team Minovation
'''
    from_email = settings.EMAIL_HOST_USER
    to_email = [email, ]
    send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=body, fail_silently=False)

def abstarct(request):
    for i in range(120,length):
        submission(request, file['Email'][i])
        print('Done')
    return  render_to_response('thanks.html',{})