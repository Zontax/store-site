from django.forms import Form, CharField, ChoiceField

from phonenumber_field.formfields import PhoneNumberField

        
class CreateOrderForm(Form):
    first_name = CharField()
    last_name = CharField()
    phone_number = PhoneNumberField(region="UA")
    
    requires_delivery = ChoiceField(
        choices=[
            ("0", False),
            ("1", True),
            ],
        )
    
    delivery_address = CharField(required=False)
    
    payment_on_get = ChoiceField(
        choices=[
            ("0", 'False'),
            ("1", 'True'),
            ],
        )
    
    
    def clean_phone_number(self):
        data = str(self.cleaned_data['phone_number'])

        # if not data.isdigit():
        #     raise ValidationError("Номер телефону повинен містити тольки цифри")
        
        #pattern = re.compile(r'^\d{12}$')
        
        #if not pattern.match(str(data)):
        #    raise ValidationError("Неправильний формат номеру")
        
        return str(data)
    
    
    # first_name = CharField(
    #     widget=TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введіть ваше ім'я",
    #         }
    #     )
    # )

    # last_name = CharField(
    #     widget=TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введітт ваше прізвище",
    #         }
    #     )
    # )

    # phone_number = CharField(
    #     widget=TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Номер телефону",
    #         }
    #     )
    # )

    # requires_delivery = ChoiceField(
    #     widget=RadioSelect(),
    #     choices=[
    #         ("0", False),
    #         ("1", True),
    #     ],
    #     initial=0,
    # )

    # delivery_address = CharField(
    #     widget=Textarea(
    #         attrs={
    #             "class": "form-control",
    #             "id": "delivery-address",
    #             "rows": 2,
    #             "placeholder": "Введіть адресу доставки",
    #         }
    #     ),
    #     required=False,
    # )

    # payment_on_get = ChoiceField(
    #     widget=RadioSelect(),
    #     choices=[
    #         ("0", 'False'),
    #         ("1", 'True'),
    #     ],
    #     initial="card",
    # )
    