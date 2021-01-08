from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import randrange
from maintest.forms import CheckAnswers
import os 
import json
import itertools

# Create your views here.
def home(request):
    if request.session.get("date"):
        del request.session['date']    
    if request.session.get("questions"):
        del request.session['questions']
    if request.session.get('rights'): 
        del request.session['rights']
    if request.session.get('wrongs'): 
        del request.session['wrongs']
    
    return render(request, 'home.html')

def foot(request):
    if request.session.get("date"):
        del request.session['date']    
    if request.session.get("questions"):
        del request.session['questions']
    if request.session.get('rights'): 
        del request.session['rights']
    if request.session.get('wrongs'): 
        del request.session['wrongs']
    
    return render(request, 'contact.html')


def ready_for_test(request):
    questions = "True"
    
    request.session['questions'] = questions
    return render(request, 'test.html')        



def ready_for_visual_test(request):
    questions = "True"
    
    request.session['questions'] = questions
    return render(request, 'visual_test.html')        



def gen_visual_test(request):
    if not request.session.get('questions'):
        return redirect("/maintest")
     
    temp_ls = []
    
    questions_dir = os.getcwd() + "/maintest/jsons" 
    count = 1
    parsed_jsons = {}
    deleted_ques = [816, 817, 818, 884, 885]
    
    while len(temp_ls) != 20:
        val = randrange(886, 980)
        
        if not str(val) in temp_ls and not val in deleted_ques:
            temp_ls.append(str(val))
            
            with open(questions_dir + "/data_{}.text".format(val), encoding="utf-8") as text:
                json_f = json.load(text)['Problem']
                
                if not "해설:" in json_f['Question']:
                    parsed_jsons[str(count)] = json_f
                    count += 1
                else:
                    temp_ls = temp_ls[:-1]

    final_jsons = {'halves' : 20}
    final_jsons['questions'] = parsed_jsons

    request.session['date'] = ' '.join(temp_ls)
    return render(request, "test_test.html", final_jsons)


def gen_test(request):
    if not request.session.get('questions'):
        return redirect("/maintest")
     
    temp_ls = []
    
    questions_dir = os.getcwd() + "/maintest/jsons" 
    count = 1
    parsed_jsons = {}
    deleted_ques = [816, 817, 818, 884, 885]
    
    while len(temp_ls) != 40:
        val = randrange(1,900)
        
        if not str(val) in temp_ls and not val in deleted_ques:
            temp_ls.append(str(val))
            
            with open(questions_dir + "/data_{}.text".format(val), encoding="utf-8") as text:
                json_f = json.load(text)['Problem']
                
                if not "해설:" in json_f['Question']:
                    parsed_jsons[str(count)] = json_f
                    count += 1
                else:
                    temp_ls = temp_ls[:-1]

    final_jsons = {}
    final_jsons['questions'] = parsed_jsons

    request.session['date'] = ' '.join(temp_ls)
    return render(request, "test_test.html", final_jsons)



def result(request):
    if request.method == "POST":

        answers_dir = os.getcwd() + "/maintest/jsons/answers" 
        
        form = CheckAnswers(request.POST)
        
        total_correct = 0
        total_ques = 0

        if form.is_valid():
            request.session['rights'] = ''
            request.session['wrongs'] = ''
           
            if not request.session.get('date'):
                return redirect("/maintest")
                    
            questions = request.session['date'].split(' ')
            total_ques = len(questions)
            keys = list(form.cleaned_data.keys())
            
            for (each, key) in zip(questions, keys):
                if each.isdigit() == False or len(each) > 4:
                    return redirect("/maintest")
                
                ## check answers
                answers = ''.join(open(answers_dir + "/{}.txt".format(each)).read().split(",  "))
                if answers == form.cleaned_data[key]:
                    app_session_data = key[key.index("_")+1:] + ":{}:{} ".format(each,form.cleaned_data[key])
                    request.session['rights'] += app_session_data
                    total_correct += 1
                else:
                    app_session_data = key[key.index("_")+1:] + ":{}:{}:{} ".format(each,form.cleaned_data[key],answers)
                    request.session['wrongs'] += app_session_data
                    
            del request.session['date']
            
            score = total_correct / total_ques * 100
            
            score = round(score, 2)
            result = {'result': score}
            result['totalCor'] = total_correct
            result['totalQues'] = total_ques
            
            return render(request, "result.html", result) 
        
        else:
            return HttpResponse('Something went wrong')
    
    else:
        return redirect("/maintest")


def display_rights_wrongs(request):
    if not request.session.get("rights") and not request.session.get("wrongs"):
        return redirect("/maintest")
    
    questions_dir = os.getcwd() + "/maintest/jsons" 
    data = {"rights": {}, "wrongs":{}}
    
    rights = request.session['rights'].strip().split(" ")
    wrongs = request.session['wrongs'].strip().split(" ")
    current_group = str(1)
     
    data['rights'][current_group] = {}
    data['wrongs'][current_group] = {}
    
    if len(rights) == 1 and rights[0] == "":
        rights = []
    if len(wrongs) == 1 and wrongs[0] == "":
        wrongs = []
    
    del request.session['rights']
    del request.session['wrongs']

    ## For the first column - right answers ##
    for each in rights:
        split_data = each.split(':')
        question = "{}".format(split_data[0])
        file_num = split_data[1]  
        user_answer = split_data[2]
    
        data['rights'][current_group][question] = {}


        with open(questions_dir + "/data_{}.text".format(file_num), encoding="utf-8") as text:
            json_f = json.load(text)['Problem']    
            data['rights'][current_group][question]['Problem'] = json_f
    
        data['rights'][current_group][question]['Rights'] = [user_answer[0]]
        

        if len(user_answer) == 2:
            data['rights'][current_group][question]['Rights'].append(user_answer[1])


    ## For the second column - wrong answers ##
    for each in wrongs:
        split_data = each.split(':')
        question = "{}".format(split_data[0])
        file_num = split_data[1]  
        user_answer = split_data[2]
        right_answer = split_data[3]
    
        data['wrongs'][current_group][question] = {}
       

        with open(questions_dir + "/data_{}.text".format(file_num), encoding="utf-8") as text:
            json_f = json.load(text)['Problem']    
            data['wrongs'][current_group][question]['Problem'] = json_f
    
        data['wrongs'][current_group][question]['Rights'] = [right_answer[0]]
       

        if len(right_answer) == 2:
            data['wrongs'][current_group][question]['Rights'].append(right_answer[1])
        
        data['wrongs'][current_group][question]['UserInput'] = []


        for answer in user_answer:
            data['wrongs'][current_group][question]['UserInput'].append(answer)
    

    return render(request, "check_orig.html", data)

