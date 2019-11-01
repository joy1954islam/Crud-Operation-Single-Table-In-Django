from django.db import models

# Create your models here.
class GovernmentEmployee(models.Model):
    GovernmentEmployeeID = models.IntegerField(primary_key=True)
    GovernmentEmployeeName = models.CharField(max_length=100)
    GovernmentEmployeeAddress = models.TextField()
    GovernmentEmployeePhnNumber = models.CharField(max_length=15)
    GovernmentEmployeeGmail = models.EmailField()
    GovernmentEmployeeDesignation = models.CharField(max_length=100)


    class Meta:
        db_table = "govermentemployee"

    def __str__(self):
        return str(self.GovernmentEmployeeName)
