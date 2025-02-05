from django.db import models

class PartnerApplication(models.Model):
    company_name = models.CharField(max_length=255)
    company_field = models.CharField(max_length=255)
    company_size = models.CharField(max_length=50)
    company_linkedin = models.URLField(blank=True, null=True)
    company_website = models.URLField(blank=True, null=True)
    contact_person_name = models.CharField(max_length=255)
    contact_person_email = models.EmailField()
    contact_person_phone = models.CharField(max_length=20)
    reason_for_applying = models.TextField()

    def __str__(self):
        return self.company_name
