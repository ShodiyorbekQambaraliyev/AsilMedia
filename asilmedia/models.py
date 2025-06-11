from django.db import models

class CKino(models.Model):
    categorykino = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.categorykino

class CDavlati(models.Model):
    cdavlati = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.cdavlati
    
class CTili(models.Model):
    ctili = models.CharField(max_length=100, unique=True)
    def __str__(self):
        
        return self.ctili
    
class CJanr(models.Model):
    cjanr = models.CharField(max_length=1000, unique=True)
    def __str__(self):
        return self.cjanr

class Media(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    banner =models.ImageField(upload_to='meida/')
    release_date = models.DateField()
    video = models.FileField(upload_to='videos/') 
    sarlavha = models.CharField(max_length=200)
    categoryjanr = models.ForeignKey(CJanr, blank=True, null=True, on_delete=models.SET_NULL)
    categorykinolar = models.ForeignKey(CKino, blank=True, null=True, on_delete=models.SET_NULL)
    categorydavlati = models.ForeignKey(CDavlati, blank=True, null=True, on_delete=models.SET_NULL)
    categorytili = models.ForeignKey(CTili, blank=True, null=True, on_delete=models.SET_NULL)
    
    
    