from django.db import models

# Create your models here.
class BaseModel(models.Model):
    """
    All models (in other apps) should subclass BaseModel.
    This is just a convenient place to add common functionality and fields
    between models.

    FSM_FIELDS (if used) must be defined on models that inherit from BaseModel.
    This takes care of excluding those fields when calling .save on the model.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
