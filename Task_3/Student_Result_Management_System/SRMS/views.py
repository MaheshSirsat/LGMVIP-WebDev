from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import forms
from . import models
@login_required
def listview(request):
    data=models.StudentInfo.objects.all()
    return render(request,'SRMS/list_view.html',{"data":data})
@login_required
def addstudent(request):
    form=forms.StudentInfo

    if request.method=="POST":
        form=forms.StudentInfo(request.POST)
     
        if form.is_valid():
            form.save()
            return redirect("/listview/")

    return render(request,"SRMS/Add_Student_Result.html",{"Studentinfo":form})
@login_required
def  delete_view(request,id):
    form=models.StudentInfo.objects.get(PRN_No=id)
    form.delete()
    return redirect("/listview/")
@login_required   
def  update_view(request,id):
    form=models.StudentInfo.objects.get(PRN_No=id)
    if request.method=="POST":
        form=forms.StudentInfo(request.POST,instance=form)
        if form.is_valid():
            form.save()
            return redirect("/listview/")
    return render(request,'SRMS/update_view.html',{"Studentinfo":form})
def resultview(request):
    Login=False
    user=request.user
    if user.is_authenticated:
        Login=True
    form=forms.result
    canshow=False
    if request.method=="POST":
        form=forms.result(request.POST)
        list=[]
        if form.is_valid():
            prn= form.cleaned_data.get("PRN_No")
            mother= form.cleaned_data.get("Mother")
            
            try:
                form=models.StudentInfo.objects.get(PRN_No=prn)
                if "<" not in str(form):
                    if str(form.Mother_Name).lower()==mother.lower() :
                        canshow=True
                        if str(form.Subject_Name_1)!="":
                            list.append([form.Subject_Name_1,form.Obtained_Marks_1,form.Maximum_Marks_1])
                            
                        if str(form.Subject_Name_2)!="":
                            list.append([form.Subject_Name_2,form.Obtained_Marks_2,form.Maximum_Marks_2])
                        if str(form.Subject_Name_3)!="":
                            list.append([form.Subject_Name_3,form.Obtained_Marks_3,form.Maximum_Marks_3])                                                  
                        if str(form.Subject_Name_4)!="":
                            list.append([form.Subject_Name_4,form.Obtained_Marks_4,form.Maximum_Marks_4])
                        if str(form.Subject_Name_5)!="":
                            list.append([form.Subject_Name_5,form.Obtained_Marks_5,form.Maximum_Marks_5])
                        if str(form.Subject_Name_6)!="":
                            list.append([form.Subject_Name_6,form.Obtained_Marks_6,form.Maximum_Marks_6])
                        if str(form.Subject_Name_7)!="":
                            list.append([form.Subject_Name_7,form.Obtained_Marks_7,form.Maximum_Marks_7])                       
                        if str(form.Subject_Name_8)!="":
                            list.append([form.Subject_Name_8,form.Obtained_Marks_8,form.Maximum_Marks_8])                        
                        if str(form.Subject_Name_9)!="":
                            list.append([form.Subject_Name_9,form.Obtained_Marks_9,form.Maximum_Marks_9])  
                        if str(form.Subject_Name_10)!="":
                            list.append([form.Subject_Name_10,form.Obtained_Marks_10,form.Maximum_Marks_10])                        
                        if str(form.Subject_Name_11)!="":
                            list.append([form.Subject_Name_11,form.Obtained_Marks_11,form.Maximum_Marks_11])
                                                  
                        if str(form.Subject_Name_12)!="":
                            list.append([form.Subject_Name_12,form.Obtained_Marks_12,form.Maximum_Marks_12])                    
                    return render(request, "SRMS/result_view.html",{'form':form,"canshow":canshow,"list":list,'Login':Login} )
            except :
                pass
    return render(request, "SRMS/result_view.html",{'form':form,"canshow":canshow,'Login':Login} )
    