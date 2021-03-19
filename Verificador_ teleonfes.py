#pip install phonenumbers

import phonenumbers

from phonenumbers import geocoder

phone = '+55' + input('Digite o celular no formato Ex: (11957770543) ou Telefone Fixo no formato EX (1143651955): ')

phone_number = phonenumbers.parse(phone)

print('Telefone Registrado no Estado Em : ' + geocoder.description_for_number(phone_number, 'pt'))