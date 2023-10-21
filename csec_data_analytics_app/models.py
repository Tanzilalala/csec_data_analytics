from mongoengine import EmailField, EmbeddedDocument, IntField, EmbeddedDocumentField
from mongoengine import Document, StringField, ListField, FloatField, DateTimeField

class UserAddress(EmbeddedDocument):
    street = StringField(required=True, null=False)
    city = StringField(required=True, null=False)
    state = StringField(required=True, null=False)
    country = StringField(required=True, null=False)
    zip = IntField(required=True, null=False)


class User(Document):
    # mongoengine defaults to allow null
    first_name = StringField(required=True, null=False)
    last_name = StringField(required=True, null=False)
    email = EmailField(required=True, null=False)
    address = EmbeddedDocumentField(UserAddress, required=True)


class Vulnerability(Document):
    cve_id = StringField()
    description = StringField()
    cpe_configurations = ListField()
    cwes = ListField(StringField())
    cisa_exploitability_metric = FloatField()
    cvss = FloatField()
    published_date = DateTimeField()
    last_modified_date = DateTimeField()

    meta = {
        'collection': 'vulnerabilities'  # Optionally specify the collection name
    }


class Book(Document):
    title = StringField(required=True)
    author = StringField(required=True)
    genre = StringField(required=True)
    publication_year = IntField(required=True)
    price = FloatField(required=True)

