from .crf_form_validator import CRFFormValidator
from edc_form_validators import FormValidator
class SubjectRequisitionFormValidator(CRFFormValidator, FormValidator):

    def clean(self):
        super().clean()

        self.validate_other_specify(field='reason_not_drawn')

        self.validate_other_specify(field='item_type')

        self.required_if('urgent', field='priority', field_required='urgent_specify')
