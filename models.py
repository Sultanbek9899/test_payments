from datetime import datetime
from attr import field
from marshmallow import Schema, fields
import pytz


class TransactionResponse(Shema):
    TransactionId = fields.String()
    Amount = fields.Decimal() 
    CurrencyCode = fields.Integer()
    Currency = fields.String()
    InvoiceId = fields.String()
    AccountId = fields.String()
    Email = fields.Email()
    Description = fields.String()
    JsonData = fields.Dict
    CreatedDateIso = fields.DateTime()
    AuthDateIso = fields.DateTime()
    ConfirmDateIso = fields.DateTime()
    AuthCode = fields.String()
    TestMode =  fields.Boolean()
    IpAddress = fields.IPv4()
    IpCountry = fields.String()
    IpCity = fields.String()
    IpRegion = fields.String()
    IpDistrict= fields.String()
    IpLatitude= fields.Float()
    IpLongitude= fields.Float()
    CardFirstSix= fields.String()
    CardLastFour= fields.String()
    CardExpDate= fields.String()
    CardType= fields.String()
    CardTypeCode= fields.Strin()
    Issuer=  fields.String()
    IssuerBankCountry= fields.String()
    Status= fields.String()
    StatusCode= fields.Integer()
    Reason= fields.String()
    ReasonCode= fields.Integer
    CardHolderMessage= fields.String
    Name= fields.String()
    



  