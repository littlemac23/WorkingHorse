from django import forms


class CreateHorseForm(forms.ModelForm):

    class Meta:
        name = models.TextField(max_length=500, primary_key=True)
        acquisitionDate = models.DateField()
        totalAcquisitionAmount = models.IntegerField()
        type = models.TextField(max_length=500)
        place = models.TextField(max_length=500)
        dispersmentClaim_Sale = models.IntegerField()
        dispersmentDate = models.DateField()
            class Meta:
                model = HorseStuff
                fields = ['body']
