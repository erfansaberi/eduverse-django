from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Section


@receiver(post_save, sender=Section)
def set_type(sender, **kwargs):
    section = kwargs['instance']
    sec_file = section.sec_file
    sec_type = section.sec_type

    if sec_file and not sec_type:
        if sec_file.name.endswith('.pdf'):
            section.sec_type = Section.Type.PDF
        elif sec_file.name.endswith('.doc'):
            section.sec_type = Section.Type.DOC
        elif sec_file.name.endswith('.rar'):
            section.sec_type = Section.Type.RAR
        elif sec_file.name.endswith('.zip'):
            section.sec_type = Section.Type.ZIP
        else:
            section.sec_type = Section.Type.VIDEO
        
        section.save()

