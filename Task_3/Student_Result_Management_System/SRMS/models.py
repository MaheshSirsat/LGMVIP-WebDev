from django.db import models
class StudentInfo(models.Model):
    Full_Name=models.CharField(max_length=30,default="")
    PRN_No=models.CharField(max_length=20,default="",primary_key=True)
    Mother_Name=models.CharField(max_length=13,default="")
    Contact_Number=models.IntegerField()
    Subject_Name_1=models.CharField(max_length=20,default="",blank=True)
    Obtained_Marks_1=models.CharField(default="",max_length=3,blank=True)
    Maximum_Marks_1=models.CharField(default="",max_length=3,blank=True)
    Subject_Name_2=models.CharField(max_length=20,default="",blank=True)
    Obtained_Marks_2=models.CharField(default="",max_length=3,blank=True)
    Maximum_Marks_2=models.CharField(default="",max_length=3,blank=True)
    Subject_Name_3=models.CharField(max_length=20,default="",blank=True)
    Obtained_Marks_3=models.CharField(default="",max_length=3,blank=True)
    Maximum_Marks_3=models.CharField(default="",max_length=3,blank=True)
    Subject_Name_4=models.CharField(max_length=20,default="",blank=True)
    Obtained_Marks_4=models.CharField(default="",max_length=3,blank=True)
    Maximum_Marks_4=models.CharField(default="",max_length=3,blank=True)
    Subject_Name_5=models.CharField(max_length=20,default="",blank=True)
    Obtained_Marks_5=models.CharField(default="",max_length=3,blank=True)
    Maximum_Marks_5=models.CharField(default="",max_length=3,blank=True)
    Subject_Name_6=models.CharField(max_length=20,default="",blank=True)
    Obtained_Marks_6=models.CharField(default="",max_length=3,blank=True)
    Maximum_Marks_6=models.CharField(default="",max_length=3,blank=True)
    Subject_Name_7=models.CharField(max_length=20,default="",blank=True)
    Obtained_Marks_7=models.CharField(default="",max_length=3,blank=True)
    Maximum_Marks_7=models.CharField(default="",max_length=3,blank=True)
    Subject_Name_8=models.CharField(max_length=20,default="",blank=True)
    Obtained_Marks_8=models.CharField(default="",max_length=3,blank=True)
    Maximum_Marks_8=models.CharField(default="",max_length=3,blank=True)
    Subject_Name_9=models.CharField(max_length=20,default="",blank=True)
    Obtained_Marks_9=models.CharField(default="",max_length=3,blank=True)
    Maximum_Marks_9=models.CharField(default="",max_length=3,blank=True)
    Subject_Name_10=models.CharField(max_length=20,default="",blank=True)
    Obtained_Marks_10=models.CharField(default="",max_length=3,blank=True)
    Maximum_Marks_10=models.CharField(default="",max_length=3,blank=True)
    Subject_Name_11=models.CharField(max_length=20,default="",blank=True)
    Obtained_Marks_11=models.CharField(default="",max_length=3,blank=True)
    Maximum_Marks_11=models.CharField(default="",max_length=3,blank=True)
    Subject_Name_12=models.CharField(max_length=20,default="",blank=True)
    Obtained_Marks_12=models.CharField(default="",max_length=3,blank=True)
    Maximum_Marks_12=models.CharField(default="",max_length=3,blank=True)
    
    
    def __str__(self):
       
        return str(self.Full_Name)