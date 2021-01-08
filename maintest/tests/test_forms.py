from maintest.forms import CheckAnswers
from django.test import TestCase

class CheckAnswersFormTest(TestCase):
    def test_answers_not_required(self):
        form = CheckAnswers()
        
        for each in range(1,41):
            self.assertTrue(form.fields['answer_{}'.format(each)].required == False)    

    
    def test_validated_form(self):
        data = {}

        for each in range(1,41):
            data[f'answer_{each}'] = "2 CD"
        
        form = CheckAnswers(data = data)
        self.assertTrue(form.is_valid())


    def test_invalidated_form(self):
        data = {}

        for each in range(1,41):
            data[f'answer_{each}'] = "  12 CD"
      
        form = CheckAnswers(data = data)
        self.assertFalse(form.is_valid())
